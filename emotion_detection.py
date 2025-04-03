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
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness'])
    dominant_emotion = max(formatted_response['emotionPredictions'][0]['emotion'], \
    key=formatted_response['emotionPredictions'][0]['emotion'].get)
    return {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion
    }
    