from sqlalchemy import (
    Integer,
    Column,
    String,
    Table,
    ForeignKey)
from sqlalchemy.orm import relationship
from . import Base
from .ShiftInvitations import ShiftInvitations


class Shift(Base):
    __tablename__ = 'shifts'

    role_id = Column(Integer, primary_key=True)
    staff_required = Column(Integer)
    # TODO: seprate unique table for job_types?
    job_type = Column(String)
    shift_date = Column(String)
    start_time = Column(String)
    end_time = Column(String)
    contractors = relationship(
        "Contractor",
        back_populates="shifts",
        # lazy="dynamic"
        secondary=ShiftInvitations)

    def __repr__(self):
        return "<Shift(id='%s', job_type='%s')>" % (self.role_id, self.job_type)
