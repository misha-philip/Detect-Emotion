import requests
import json
'''
'{"emotionPredictions":[{"emotion":{"anger":0.01364663, "disgust":0.0017160787, "fear":0.008986978,
 "joy":0.9719017, "sadness":0.055187024}, "target":"", "emotionMentions":[{"span":{"begin":0, "end":27
 , "text":"I love this new technology."}, "emotion":{"anger":0.01364663, "disgust":0.0017160787,
  "fear":0.008986978, "joy":0.9719017, "sadness":0.055187024}}]}], "producerId":{"name":"Ensemble Aggregated Emotion Workflow",
   "version":"0.0.1"}}'
'''

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=obj, headers=headers)
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant_emotion
    return emotions

