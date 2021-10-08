from flask import Flask, request, jsonify
import nltk
from MiMIC.summary import Summarize

app = Flask(__name__)


@app.route('/', methods=["GET"])
def test_get():
    return 'This is a test API call!'


@app.route('/post', methods=["POST"])
def test_post():
    input_json = request.get_json(force=True)
    dictToReturn = {'text': input_json['text']}
    return jsonify(dictToReturn)


@app.route('/summarize', methods=["POST", "GET"])
def summarize():
    input_text = request.get_json(force=True)["text"]
    summarized_text = Summarize(text=input_text, lang="english").summarize()
    result_dict = {'summarized text': summarized_text}
    return jsonify(result_dict)


@app.route('/numSent', methods=["POST", "GET"])
def get_num_sent():
    input_text = request.get_json(force=True)["text"]
    num_sent = len(nltk.sent_tokenize(input_text))
    result_dict = {'Number of sentences': num_sent}
    return jsonify(result_dict)


if __name__ == '__main__':
    app.run(debug=True)
