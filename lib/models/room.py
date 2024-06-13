from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    hostel_id = Column(Integer, ForeignKey('hostels.id'))
    room_number = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    hostel = relationship('Hostel', back_populates='rooms')
    bookings = relationship('Booking', back_populates='room', cascade='all, delete-orphan')

    def __repr__(self):
        return f"Room(id={self.id}, room_number={self.room_number}, capacity={self.capacity})"

    @classmethod
    def create(cls, session, hostel_id, room_number, capacity):
        room = cls(hostel_id=hostel_id, room_number=room_number, capacity=capacity)
        session.add(room)
        session.commit()
        return room

    @classmethod
    def delete(cls, session, room_id):
        room = session.query(cls).filter_by(id=room_id).one_or_none()
        if room:
            session.delete(room)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, room_id):
        return session.query(cls).filter_by(id=room_id).one_or_none()
