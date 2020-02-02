# -*- coding: utf-8 -*-
from flask import jsonify, request
from schematics.exceptions import ModelValidationError

from src.app import app
from src.entities.FilterShiftsRequest import FilterShiftsRequest
from src.controllers.shift import shift_controller
from src.entities.GetShiftsResponse import GetShiftsResponse
from src.lib.sqlalchemyencoder import encode


@app.route("/shifts", methods=["GET"])
def get_shifts():
    query = FilterShiftsRequest(request.args)

    try:
        query.validate()
    except ModelValidationError as err:
        return jsonify(err.to_primitive()), 400

    shifts = shift_controller.find(query)
    response = map(encode, shifts)
    return jsonify(response)


@app.route("/shifts/<int:shift_id>/contracts", methods=["GET"])
def get_shift_contracts(shift_id):
    contractors = shift_controller.get_shift_contractors(shift_id)
    response = map(encode, contractors)
    return jsonify(response)


@app.route("/shifts", methods=["GET"])
def filter_shifts():
    req = FilterShiftRequest(request.args)
    print req.validate()
    return jsonify(req.to_primitive)
