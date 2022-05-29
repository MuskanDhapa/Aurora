from ast import arguments
from flask import Flask, render_template, jsonify, request
import processor


app = Flask(__name__)

#app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'

@app.route('/')
def index():
    return "<h1> Deployed to Heroku</h1>"


@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():

    if request.method == 'GET':
        arguments = request.args
        the_question = arguments.get("question")

        response = processor.chatbot_response(the_question)

        return jsonify({"response": response })
    
    else:
        response = "Hi! I'm Aurora."
        return jsonify({"response": response })



if __name__ == '__main__':
    app.run(debug=True)
