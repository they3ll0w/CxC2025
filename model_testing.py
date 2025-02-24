import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

# Load the model and the tokenizer
model = load_model('model.h5')
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

max_length = 10

def predict_next_event(sequence):
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

sequence = ['application-window-opened', 'session_start', 'triaged-submission-list:my-book::view']

# Example Usage
while(True):
    print("Enter the sequence of events (type 'exit' to quit): ")
    new_input = input()
    if new_input == 'exit':
        break
    sequence.append(new_input)
    predicted_event = predict_next_event(sequence)
    print(f"Predicted next event: {predicted_event}")
