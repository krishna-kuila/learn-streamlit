import streamlit as st
import datetime


st.title(" Age Calcualtor")
name = st.text_input('Enter your name :')
dob = st.date_input('Enter your DOB :',value=None, min_value=("2000-01-01"), max_value=datetime.datetime.today(), width=210, format='DD/MM/YYYY')
button = st.button('Calculate')
if button and name and dob:
    today = datetime.date.today()
    age = today - dob
    yrs = int((age.days)/365)
    month = int((age.days % 365)/30)
    day = (age.days % 365)%30
    st.write(f'{name}, Your age is :')
    st.badge(f'{yrs} years and {month} month', color='green')
else:
    st.badge('Value missing...',color='red')