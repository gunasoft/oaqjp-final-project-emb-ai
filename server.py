"""Importing required libraries and functions
   fromEmotionDetection pacakage"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emo_detector():
    '''This function is to retrieve the text and return the formatted text'''
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!."
    return f"For the given statement, the system response is 'anger': {anger},"\
           f" 'digust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}."\
           f" The dominant emotion is {dominant_emotion}."

@app.route('/')
def render_index_page():
    '''This function should simply run the render_template function on the HTML template'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
    