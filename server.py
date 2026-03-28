"""
Flask application for Emotion Detection.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

APP = Flask(__name__)


@APP.route("/")
def index():
    """
    Render the homepage.
    """
    return render_template("index.html")


@APP.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Handle emotion detection request and return formatted response.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response_text = (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)

