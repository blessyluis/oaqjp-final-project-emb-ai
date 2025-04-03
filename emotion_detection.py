''' This module is to run the emotion detection function named emotion_detector.
The argument of the function is "text_to_analyze" which is a variable \
that holds the actual written text that needs to be analyzed.
'''
import json
import requests

def emotion_detector(text_to_analyze):
    ''' Executing this function runs the emotion_detector function and returns the response as a text.
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1'\
    '/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header, timeout=15)
    formatted_response = json.loads(response.text)
    return formatted_response