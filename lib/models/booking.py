from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Booking(Base):
    __tablename__ = 'bookings'
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    room_id = Column(Integer, ForeignKey('rooms.id'))
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    student = relationship("Student", back_populates="bookings")
    room = relationship("Room", back_populates="bookings")

    def __repr__(self):
        return f"Booking(id={self.id}, student_id={self.student_id}, room_id={self.room_id}, start_date={self.start_date}, end_date={self.end_date})"

    @classmethod
    def create(cls, session, student_id, room_id, start_date, end_date):
        booking = cls(student_id=student_id, room_id=room_id, start_date=start_date, end_date=end_date)
        session.add(booking)
        session.commit()
        return booking

    @classmethod
    def delete(cls, session, booking_id):
        booking = session.query(cls).filter_by(id=booking_id).one_or_none()
        if booking:
            session.delete(booking)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, booking_id):
        return session.query(cls).filter_by(id=booking_id).one_or_none()
