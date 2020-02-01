# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from src.controllers import shift_controller
from src.entities.GetShiftsResponse import GetShiftsResponse
from src.lib.sqlalchemyencoder import encode

app = Flask(__name__)


@app.route("/shifts")
def get_shifts():
    shifts = shift_controller.get_all()
    response = map(encode, shifts)
    return jsonify(response)


@app.route("/shifts/:id/contracts")
def get_shift_contracts(shift_id):
    contractors = shift_controller.get_shift_contracts(shift_id)
    #TODO parse contractors
    return shift_id
