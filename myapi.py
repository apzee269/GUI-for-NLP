import paralleldots as pd


class API:

    def __init__(self):
        pd.set_api_key('tEuDn256gd4cwxTYDdiwW6u8OblSVKVHm1oTPanzwjs')
    def sentiment_analysis(self,text):
        response = pd.sentiment(text);
        return response

    def ner(self,text):
        response = pd.ner(text)
        return response

    def emotion_prediction(self,text):
        response = pd.emotion(text)
        return response