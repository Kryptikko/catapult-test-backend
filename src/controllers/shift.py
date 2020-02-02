from datetime import time
from src.models import sess
from src.models.Shifts import Shift
from src.models.Contractors import Contractor


class ShiftController:

    def find(self, request):
        query = sess.query(Shift)

        if request.startTime:
            if request.startTime == "AM":
                query = query.filter(
                        Shift.start_time.between(time(0,0,0), time(12,0,0)))
            if request.startTime == "PM":
                query = query.filter(
                        Shift.start_time.between(time(12,0,0), time(23,59,0)))

        if request.jobType:
            query = query.filter(
                    Shift.job_type.like(request.jobType))

        return query.all()

    def get_shift_contractors(self, shift_id):
        shift = sess.query(Shift).filter_by(role_id=shift_id).first()
        return shift.contractors

shift_controller = ShiftController()
