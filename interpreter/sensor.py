import json
import sys

from subprocess import check_output
from datetime import datetime as dt

import interpreter.transcribe
import interpreter.interpret

def extract_route_from_audio(audio_file):
    language = 'es-MX'
    sound_output = interpreter.transcribe.transcribe(audio_file,language)
    print(sound_output)
    transcription = sound_output["results"][0]["alternatives"][0]["transcript"]
    interpretation = interpreter.interpret.process(transcription)
    origin = get_entity_for_value(interpretation, "origin")
    destination = get_entity_for_value(interpretation, "destination")

    return origin, destination

def get_entity_for_value(interpretation, value):
    try:
        entities = interpretation["entities"]
        entity_value = [entity["entity"] for entity in entities if entity["type"] == value][0]
    except:
        entity_value = "None"
    return entity_value