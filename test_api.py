import requests
import json

params = {
    'sequence': ['application-window-opened', 'session_start']
}
response = requests.post('https://localhost:5000/api/v1/predict', json=params)

print(response.json())