import json
import requests

from flask import Flask, jsonify, request
import numpy as np

import config
import db
import ml_core


app = Flask(__name__)


def get_embedding(question: str, url: str) -> list:
    r = requests.post(url, json={"instances": [question]})
    vec = r.json()['predictions']
    return vec


def get_answer(question: np.array, url: str) -> str:
    r = requests.post(url, json=json.dumps({"question": question}))
    return r.json()["answer"]
    

@app.route('/return_answer', methods=['POST'])
def return_answer():
    question = json.loads(request.json)['question']
    vec = get_embedding(question, config.EMBEDDER_URL)
    cl_id = ml_core.find_cluster(vec, db.centroids)
    answer = get_answer(vec, f'{config.INDEXER_URL}{cl_id}/get_answer')

    return jsonify(answer=answer, cluster=cl_id)


if __name__ == "__main__":
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT)
