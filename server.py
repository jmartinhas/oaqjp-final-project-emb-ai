""" Flask application that provides an endpoint for emotion analysis."""
from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector as emo_detect

app = Flask(__name__)

@app.route("/emotionDetector", methods=['POST'])
def emotion_detector():
    """
    Analyzes the emotion expressed in a given text.

    This endpoint receives a JSON payload containing text and returns an analysis of the emotion.
    
    :param text: The text to analyze for emotion. (Type: str)
    :return: A string containing the system response and dominant emotion. (Type: str)
    """
    data = request.json
    text_to_analyze = data.get('text')
    result = emo_detect(text_to_analyze)
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!."
    output = "For the given statement, the system response is "
    for k,v in result.items():
        if k != "dominant":
            output += f"'{k}': {v}"
    output += f".\nThe dominant emotion is {result['dominant_emotion']}"
    return output

if __name__ == '__main__':
    app.run(debug=True, port=5000)
