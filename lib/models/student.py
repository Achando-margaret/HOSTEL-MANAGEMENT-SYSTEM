from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    bookings = relationship('Booking', back_populates='student', cascade='all, delete-orphan')

    def __repr__(self):
        return f"Student(id={self.id}, name={self.name}, age={self.age}, gender={self.gender})"

    @classmethod
    def create(cls, session, name, age, gender):
        student = cls(name=name, age=age, gender=gender)
        session.add(student)
        session.commit()
        return student

    @classmethod
    def delete(cls, session, student_id):
        student = session.query(cls).filter_by(id=student_id).one_or_none()
        if student:
            session.delete(student)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, student_id):
        return session.query(cls).filter_by(id=student_id).one_or_none()
