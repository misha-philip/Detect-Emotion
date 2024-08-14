"""
Flask application for emotion detection
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector as detect_emotion

app = Flask("Emotion Detection")

@app.route("/")
def index():
    """
    Renders the index page of the application.
    """
    return render_template("index.html")

@app.route('/emotionDetector', methods=["GET"])
def emotion_detector():
    """
    Processes the emotion detection for the given text.

    Returns:
        str: A message with the emotion detection result or an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    if text_to_analyze:
        response = detect_emotion(text_to_analyze)
        if response['dominant_emotion'] is None:
            return "Invalid text! Please try again!.", 400

        dominant_emotion = response.pop('dominant_emotion')  # Retrieve the dominant emotion
        response_text = ", ".join([f"{key}: {value}" for key, value in response.items()])
        return (
            f"For the given statement, the system response is: {response_text}. "
            f"The dominant emotion is {dominant_emotion}"
        )

    return "No text to analyze, Please enter some Text", 400

@app.errorhandler(400)
def invalid_text(_):
    """
    Handles 400 Bad Request errors.

    Returns:
        dict: A dictionary containing an error message and a 400 status code.
    """
    return {"message": "Invalid text! Please try again!."}, 400

if __name__ == "__main__":
    app.run(host="127.0.0.0", port=5000)
    