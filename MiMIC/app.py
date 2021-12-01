import flask
from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk
from MiMIC.summary import Summarize

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["GET"])
def test_get():
    response = flask.jsonify({'text':'This is a test API call!'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/post', methods=["POST"])
def test_post():
    input_json = request.get_json(force=True)
    dictToReturn = {'text': input_json['text']}
    return jsonify(dictToReturn)


@app.route('/summarize', methods=["POST", "GET"])
def summarize():
    input_text = request.get_json(force=True)["text"]
    summarized_text = Summarize(text=input_text, lang="english").summarize()
    result_dict = flask.jsonify({'summarizedText': summarized_text})
    result_dict.headers.add('Access-Control-Allow-Origin', '*')
    return result_dict


# @app.route('/numSent', methods=["POST", "GET"])
# def get_num_sent():
#     #get the number of sentences returned
#     input_text = request.get_json(force=True)["text"]
#     num_sent = len(nltk.sent_tokenize(input_text))
#     result_dict = {'Number of sentences': num_sent}
#     return jsonify(result_dict)

#ability to choose extractive/abstractive

if __name__ == '__main__':
    app.run(debug=True)
