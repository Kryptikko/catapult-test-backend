from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from src.models import Base
from src.models.ShiftInvitations import ShiftInvitations


class Contractor(Base):
    __tablename__ = 'contractors'
    id = Column(Integer, primary_key=True)
    candidate_name = Column(String)
    shifts = relationship(
        "Shift",
        back_populates="contractors",
        # lazy="dynamic"
        secondary=ShiftInvitations)

    def __repr__(self):
        return "<Contractor(name='%s', shifts='%s')>" % (self.candidate_name, len(self.shifts))
