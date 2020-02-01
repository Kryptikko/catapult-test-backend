from src.models import sess
from src.models.Shifts import Shift
from src.models.Contractors import Contractor


class ShiftController:

    def get_all(self):
        return sess.query(Shift).all()

    def get_shift_contractors(self, shift_id):
        pass

shift_controller = ShiftController()
