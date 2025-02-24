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
print("Unique Type of Event:", data['event_type'].nunique())

# Event Type Distribution
event_types = data['event_type']
session_events = []
current_session = []

for event in event_types[::-1]:
    current_session.append(event)
    if event == 'session_end':
        session_events.append(current_session)
        current_session = []

input_sequences = []
target_events = []
min_sequence_length = 5

for seq in session_events:
    if len(seq) < min_sequence_length or len(seq) > 100:
        continue
    for i in range(3, len(seq)):
        input_sequences.append(seq[:i])
        target_events.append(seq[i])

five_int = np.random.randint(0, len(input_sequences), 5)
print("\nExample Input Sequences:")
for i in five_int:
    break
    print(input_sequences[i], '->', target_events[i])
#print(target_events)

# Tokenize the event sequences.
tokenizer = Tokenizer(filters='', split='\n')
tokenizer.fit_on_texts(input_sequences + target_events)
vocab_size = len(tokenizer.word_index) + 1
print(tokenizer)

# Convert input sequences and target events to integer sequences.
input_sequences_int = tokenizer.texts_to_sequences(input_sequences)
target_sequences_int = np.array([tokenizer.texts_to_sequences([te])[0][0] for te in target_events])

# Pad the input sequences to have the same length.
max_length = 100
input_sequences_padded = pad_sequences(input_sequences_int, maxlen=max_length, padding='pre')

print(f"\nTotal training samples: {len(input_sequences_padded)}")
print(f"Vocabulary Size: {vocab_size}, Maximum sequence length: {max_length}")

# Split the dataset into training and validation sets.
X_train, X_val, y_train, y_val = train_test_split(input_sequences_padded, target_sequences_int, 
                                                  test_size=0.2, random_state=42)

# Build an RNN model using Keras.
embedding_dim = 100
model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length),
    LSTM(100),
    Dense(vocab_size, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

history = model.fit(X_train, y_train, epochs=30, validation_data=(X_val, y_val))

# Testing the model
val_loss, val_accuracy = model.evaluate(X_val, y_val, verbose=0)
print(f"Validation Loss: {val_loss}")
print(f"Validation Accuracy: {val_accuracy}")
print(f"Validation Error (1 - accuracy): {1 - val_accuracy}")

model.save('model.h5')
with open('tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)

# Real Time Recommendations

def predict_next_event(model, tokenizer, sequence, max_length):
    """
    Given a list of events (sequence), predict the next event.
    """
    seq_int = tokenizer.texts_to_sequences([sequence])
    seq_int = pad_sequences(seq_int, maxlen=max_length, padding='pre')
    pred_prob = model.predict(seq_int, verbose=0)
    pred_int = np.argmax(pred_prob, axis=1)[0]
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
