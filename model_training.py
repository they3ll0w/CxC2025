# Import libraries
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from collections import defaultdict
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from sklearn.model_selection import train_test_split
import pickle

# Data Loading
data = pd.read_csv('data/raw_data/new_amplitude_export_2025_chunk_0_100000.csv')

# Convert string datetime fields to datetime objects
date_columns = ['client_event_time', 'client_upload_time', 'event_time', 
                'processed_time', 'server_received_time', 'server_upload_time']
for col in date_columns:
    data[col] = pd.to_datetime(data[col], errors='coerce')

# Parse JSON field safely
def parse_json(s):
    try:
        return json.loads(s.replace("'", '"'))
    except Exception as e:
        return {}

# Parse JSON fields in the dataset
data['event_properties_parsed'] = data['event_properties'].apply(parse_json)
data['user_properties_parsed'] = data['user_properties'].apply(parse_json)

# Basic Overview of the Data
print("Unique Users in this Chunk:", data['user_id'].nunique())
print("Unique Sessions in this Chunk:", data['session_id'].nunique())

# Session Duration Distribution
data_sorted = data.sort_values(by=['session_id', 'client_event_time'])
data_sorted.to_csv('data/data_sorted.csv', index=False)

# Modeling using RNN
# %%
data_sorted = pd.read_csv('data/data_sorted.csv')
session_events = data_sorted.groupby('session_id')['event_type'].apply(list).tolist()

input_sequences = []
target_events = []
min_sequence_length = 5

for seq in session_events:
    if len(seq) < min_sequence_length:
        continue
    for i in range(1, len(seq)):
        input_sequences.append(seq[i:])
        target_events.append(seq[i])

print(input_sequences[:5])
print(target_events[:5])

# Tokenize the event sequences.
tokenizer = Tokenizer()
tokenizer.fit_on_texts(input_sequences + target_events)
vocab_size = len(tokenizer.word_index) + 1

# Convert input sequences and target events to integer sequences.
input_sequences_int = tokenizer.texts_to_sequences(input_sequences)
target_sequences_int = np.array([tokenizer.texts_to_sequences([te])[0][0] for te in target_events])

# Pad the input sequences to have the same length.
max_length = max(len(seq) for seq in input_sequences_int)
print(max_length)
input_sequences_padded = pad_sequences(input_sequences_int, maxlen=max_length, padding='pre')

print(f"\nTotal training samples: {len(input_sequences_padded)}")
print(f"Vocabulary Size: {vocab_size}, Maximum sequence length: {max_length}")

# Split the dataset into training and validation sets.
X_train, X_val, y_train, y_val = train_test_split(input_sequences_padded, target_sequences_int, 
                                                  test_size=0.2, random_state=42)

# Build an RNN model using Keras.
embedding_dim = 50
model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length),
    LSTM(50),
    Dense(vocab_size, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

history = model.fit(X_train, y_train, epochs=1, validation_data=(X_val, y_val))

# Testing the model
val_loss, val_accuracy = model.evaluate(X_val, y_val, verbose=0)
print(f"Validation Loss: {val_loss}")
print(f"Validation Accuracy: {val_accuracy}")
print(f"Validation Error (1 - accuracy): {1 - val_accuracy}")

pickle.dump(model, open('model.pkl','wb'))
with open('tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)

# Real Time Recommendations

def predict_next_event(model, tokenizer, sequence, max_length):
    """
    Given a list of events (sequence), predict the next event.
    """
    # Convert the current sequence of events to integers.
    seq_int = tokenizer.texts_to_sequences([sequence])
    seq_int = pad_sequences(seq_int, maxlen=max_length, padding='pre')
    # Predict probabilities over the vocabulary.
    pred_prob = model.predict(seq_int, verbose=0)
    pred_int = np.argmax(pred_prob, axis=1)[0]
    # Reverse lookup: get the event name corresponding to the integer.
    for event, index in tokenizer.word_index.items():
        if index == pred_int:
            return event
    return None

def real_time_recommendation(event_stream, model, tokenizer, max_length):
    """
    Simulates receiving events one by one and provides a recommendation for the next event.
    """
    current_sequence = []
    for event in event_stream:
        current_sequence.append(event)
        recommended_event = predict_next_event(model, tokenizer, current_sequence, max_length)
        print(f"Current sequence: {current_sequence} -> Recommended next event: {recommended_event}")

# Example: Simulate a stream of events.
sample_stream = ['application-window-opened', 'page-view', 'button-click']
print("\nReal-Time Recommendation Simulation:")
real_time_recommendation(sample_stream, model, tokenizer, max_length)


# Prediction using Markov Chains
# transition_counts = defaultdict(lambda: defaultdict(int))

# for session_id, group in data_sorted.groupby('session_id'):

#     events = group['event_type'].tolist()
#     for i in range(len(events) - 1):
#         current_event = events[i]
#         next_event = events[i+1]
#         transition_counts[current_event][next_event] += 1

# transition_prob = {}
# for current_event, next_events in transition_counts.items():
#     total = sum(next_events.values())
#     transition_prob[current_event] = {ne: count/total for ne, count in next_events.items()}

# # Function to predict the next action given the current event
# def predict_next_action(current_event, transition_prob_dict):
#     if current_event in transition_prob_dict:
#         return max(transition_prob_dict[current_event], key=transition_prob_dict[current_event].get)
#     else:
#         return None

# # Example of prediction
# current_event_example = 'application-window-opened'
# predicted_next = predict_next_action(current_event_example, transition_prob)
# print(f"Predicted next action for '{current_event_example}': {predicted_next}")

# # Use graph to represent the connections between events

# G = nx.DiGraph()

# for current, next_events in transition_prob.items():
#     for next_event, prob in next_events.items():
#         G.add_edge(current, next_event, weight=prob)

# plt.figure(figsize=(10, 8))
# pos = nx.spring_layout(G, k=0.5)
# edges = G.edges(data=True)
# weights = [edge[2]['weight']*5 for edge in edges]  # scale weights for visibility

# nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, 
#         arrowsize=20, edge_color=weights, edge_cmap=plt.cm.Blues)
# plt.title("User Event Transition Graph")
# plt.show()


# Use a model for prediction

# Extract user-level features
# user_features = data.sort_values(by='client_event_time').groupby('user_id').agg(
#     total_events=('event_type', 'count'),
#     first_event=('client_event_time', 'min'),
#     last_event=('client_event_time', 'max')
# ).reset_index()

# user_features['active_days'] = (user_features['last_event'] - user_features['first_event']).dt.days + 1
# user_features['events_per_day'] = user_features['total_events'] / user_features['active_days']
# print("User-level Features Sample:")
# print(user_features.head())

# session_features = data_sorted.groupby('session_id')['client_event_time'].agg(['min', 'max']).reset_index()
# session_features['session_duration_sec'] = (session_features['max'] - session_features['min']).dt.total_seconds()
# print("\nSession-level Features Sample:")
# print(session_features.head())