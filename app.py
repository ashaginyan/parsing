from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=["GET"])
def hello_page():
    dictToReturn = {'text': {'This is hello page': ['1', '2']}}
    return jsonify(dictToReturn)

@app.route('/post', methods=["POST"])
def testpost():
     input_json = request.get_json(force=True)
     dictToReturn = {'text':input_json['test json']}
     return jsonify(dictToReturn)