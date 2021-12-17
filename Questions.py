import requests
import random

difficulty = ['easy','medium','hard']

parameters = {
    'amount': 50,
    'difficulty': random.choice(difficulty),
    'type': 'boolean'
}

response = requests.get('https://opentdb.com/api.php',params=parameters)
response.raise_for_status()
questions = response.json()
data = questions['results']
