''' Executing this module initiates the application of emotion detection
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created
from EmotionDetection.emotion_detection import emotion_detector
#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotion's along with their score and also
        the dominant emotion
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
    return f"For the given statement, the system response is " \
    f"'anger': {response['anger']}, 'disgust': {response['disgust']}, " \
    f"'fear': {response['fear']}, 'joy': {response['joy']} and " \
    f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    #This functions executes the flask app and deploys it on localhost:5000
    app.run(host='localhost', port=5000, debug=True)
