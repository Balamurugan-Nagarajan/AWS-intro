import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Feedback

# Connect to the database
engine = create_engine('sqlite:///feedbacks.db')
Session = sessionmaker(bind=engine)
session = Session()

# Streamlit UI
st.title('Feedback Form')

# Form elements
user_name = st.text_input('User name')
gender = st.radio('Gender', ['Male', 'Female', 'Other'])
review = st.text_area('Review')
rating = st.slider('Rating', min_value=0, max_value=10, step=1)

# Submit button
if st.button('Submit'):
    # Store values in the database
    feedback = Feedback(user_name=user_name, gender=gender, review=review, rating=rating)
    session.add(feedback)
    session.commit()
    st.success('Feedback submitted successfully!')

# Display the table
st.subheader('Feedbacks')
feedbacks = session.query(Feedback).all()
for feedback in feedbacks:
    st.write(f"User: {feedback.user_name}, Gender: {feedback.gender}, Review: {feedback.review}, Rating: {feedback.rating}")
