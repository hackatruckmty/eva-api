import requests
import os

luis_url = os.environ["LUIS_URL"]

def process(utterance):
  interpretation = requests.get(luis_url + utterance).json()
  return interpretation
