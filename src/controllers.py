from src.models import sess, Base, engine
from src.models.Shifts import Shift
from src.models.Contractors import Contractor
import json

# Base.metadata.create_all(engine)
# sess.commit()
#
# api = ""
# with open("api.json", "r") as api_file:
#     api = json.load(api_file)

class ShiftController:
    def get_all(self):
        return sess.query(Shift).all()

    def get_shift_contractors(shift_id):
        pass

shift_controller = ShiftController()
