from flask import Flask, jsonify
import json

app = Flask(__name__)


with open('data.json', 'r') as json_file:
    sample_data = json.load(json_file)

@app.route('/jsondata', methods=['GET'])
def get_json_data():
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(debug=True)￼
