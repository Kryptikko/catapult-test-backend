import json
from os import system
from src.models import sess, Base, engine
from src.models.Shifts import Shift
from src.models.Contractors import Contractor
import datetime

def serve():
    system("FLASK_APP=src/app.py FLASK_ENV=development flask run")


def drop_db():
    Base.metadata.drop_all(engine)
    sess.commit()


def bootstrap_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    api = ""
    with open("api.json", "r") as api_file:
        api = json.load(api_file)

    contractors = {}
    shifts = {}


    for contractor_data in api["invited_contracts_list"]:

        role_id = contractor_data.pop("role_id")
        contractor_model = Contractor(**contractor_data)
        for role in role_id:
            if not role in contractors:
                contractors[role] = []
            contractors[role].append(contractor_model)


    for shift_data in api["shifts_list"]:
        role_id = shift_data["role_id"]
        # convert the string time values to python datetime objects
        # so they are copatible with the sqlalchemy TIME type
        for field in ["start_time", "end_time"]:
            value = shift_data[field]
            value = map(int, value.split(":"))
            shift_data[field] = datetime.time(*value)

        shift_model = Shift(**shift_data)

        if role_id in contractors:
            for contractor_model in contractors[role_id]:
                shift_model.contractors.append(contractor_model)
                contractor_model.shifts.append(shift_model)

        sess.add(shift_model)

    sess.commit()
