import os
import flask
import json
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from flask_cors import CORS

# Load the model and the tokenizer
model = load_model('model.h5')
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

def predict_next_event(sequence):
    """
    Given a list of events, predict the next event and the probablity of end_session.
    """
    seq_int = tokenizer.texts_to_sequences([sequence])
    seq_int = pad_sequences(seq_int, maxlen=100, padding='pre')
    pred_prob = model.predict(seq_int, verbose=0)
    pred_int = np.argmax(pred_prob, axis=1)[0]
    
    max_event = ''
    prob_event = 0
    prob_end_session = 0

    for event, index in tokenizer.word_index.items():
        if index == pred_int:
            max_event = event
            prob_event = pred_prob[0][index]
        if event == 'end_session':
            prob_end_session = pred_prob[0][index]

    return max_event, prob_event, prob_end_session

app = flask.Flask(__name__)
<<<<<<< HEAD

=======
CORS(app, supports_credentials=True)
>>>>>>> frontend

"""
To call the API, you can use the following code snippet:

params = {'sequence': ['application-window-opened', 'session_start', 'triaged-submission-list:my-book::view']}
response = requests.get('http://localhost:5000/api/v1/predict', json=params)

"""


@app.route('/api/v1/predict', methods=['GET', 'POST'])
def predict():
    params = flask.request.json
    if params is None:
        params = flask.request.args

    if 'sequence' in params:
        sequence = params['sequence']
        predicted_event, prob_event, prob_end_session = predict_next_event(sequence)
        data = {
            'predicted_event': predicted_event,
<<<<<<< HEAD
            'prob_event': prob_event,
            'prob_end_session': prob_end_session
        }

    return flask.jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
=======
            'prob_event': str(prob_event),
            'prob_end_session': str(prob_end_session)
        }

    response = flask.jsonify(data)

    return response

if __name__ == '__main__':
    app.run(debug=True, port=4000)
>>>>>>> frontend
