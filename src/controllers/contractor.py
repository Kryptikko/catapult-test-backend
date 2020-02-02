# -*- coding: utf-8 -*-
from sqlalchemy import func
from src.models import sess
from src.models.Shifts import Shift
from src.models.Contractors import Contractor
from src.models.ShiftInvitations import ShiftInvitations


class ContractorController:

    def find(self, query):
        return sess.query(Contractor).all()

    def get_invited(self):
        contractors = sess \
            .query(Contractor) \
            .filter(Contractor.shifts.any()) \
            .all()

        return contractors

contractor_controller = ContractorController()
