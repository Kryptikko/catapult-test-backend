from flask import Flask, request, jsonify
from marshmallow import Schema, fields

from src.controllers import shift_controller
from src.entities.GetShiftsResponse import GetShiftsResponse

app = Flask(__name__)


@app.route("/shifts")
def get_shifts():
    shifts = shift_controller.get_all()
    def _format_output(shift):
        return dict(shift)
        # return shift.__dict__
        # return shift.to_dict()
        # return jsonify(shift)
    # response = [dict(r) for r in shifts]
    response = map(_format_output, shifts)
    print(response)
    # return response
    return jsonify({"response": response})

@app.route("/shifts/:id/contracts")
def get_shift_contracts(shift_id):
    contractors = shift_controller.get_shift_contracts(shift_id)
    #TODO parse contractors
    return shift_id
