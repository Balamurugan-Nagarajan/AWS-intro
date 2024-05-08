from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Feedback(Base):
    __tablename__ = 'feedbacks'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(40))
    gender = Column(String(10))
    review = Column(String(300))
    rating = Column(Integer)

# Create SQLite database
engine = create_engine('sqlite:///feedbacks.db')
Base.metadata.create_all(engine)
