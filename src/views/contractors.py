# -*- coding: utf-8 -*-
from flask import jsonify
from src.app import app
from src.controllers.contractor import contractor_controller
from src.lib.sqlalchemyencoder import encode


def _invited_contractors_encode(contractor):
    base = encode(contractor)
    base["shifts"] = map(lambda shift: shift.role_id, contractor.shifts)
    return base


@app.route("/contractors", methods=["GET"])
def get_contractors():
    contractors = contractor_controller.get_all()
    response = map(encode, contractors)
    return jsonify(response)


@app.route("/contractors/invited", methods=["GET"])
def get_invited_contractors():
    contractors = contractor_controller.get_invited()
    response = map(_invited_contractors_encode, contractors)

    return jsonify(response)
