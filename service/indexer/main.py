import json

from flask import Flask, jsonify, request

import config
import db
import ml_core


app = Flask(__name__)


@app.route("/get_answer", methods=["POST"])
def get_answer():
    q = json.loads(request.json)["question"]
    answer = ml_core.find_answer(q, db.answer_emb, db.ind2answer)
    return jsonify(answer=answer)

if __name__ == "__main__":
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT)
