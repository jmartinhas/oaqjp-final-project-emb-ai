import requests
import json
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    json_doc = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = json_doc, headers=header)
    data = json.loads(response.text)

    anger_score = data['emotionPredictions'][0]['emotion']['anger']
    disgust_score = data['emotionPredictions'][0]['emotion']['disgust']
    fear_score = data['emotionPredictions'][0]['emotion']['fear']
    joy_score = data['emotionPredictions'][0]['emotion']['joy']
    sadness_score = data['emotionPredictions'][0]['emotion']['sadness']
    dominant_emotion = max(data['emotionPredictions'][0]['emotion'], key=lambda k: data['emotionPredictions'][0]['emotion'][k])
    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }
