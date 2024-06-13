from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Hostel(Base):
    __tablename__ = 'hostels'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    rooms = relationship('Room', back_populates='hostel', cascade='all, delete-orphan')

    def __repr__(self):
        return f"Hostel(id={self.id}, name={self.name}, address={self.address})"

    @classmethod
    def create(cls, session, name, address):
        hostel = cls(name=name, address=address)
        session.add(hostel)
        session.commit()
        return hostel

    @classmethod
    def delete(cls, session, hostel_id):
        hostel = session.query(cls).filter_by(id=hostel_id).one_or_none()
        if hostel:
            session.delete(hostel)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, hostel_id):
        return session.query(cls).filter_by(id=hostel_id).one_or_none()
