import streamlit as st
import datetime


st.title(" Age Calcualtor")
name = st.text_input('Enter your name :')
dob = st.date_input('Enter your DOB :',value=None, min_value=("2000-01-01"), max_value=datetime.datetime.today(), width=210, format='DD/MM/YYYY')
button = st.button('Calculate')
if button and name and dob:
    today = datetime.date.today()
    cur_year, birth_year = today.year, (dob.year-1)
    no_of_lyear = round(((cur_year/4)-(cur_year/100)+(cur_year/400)) - ((birth_year/4)-(birth_year/100)+(birth_year/400)))
    age = today - dob
    days = age.days - no_of_lyear
    yrs = (days)//365
    month = (days % 365)//30
    day = (days%365)%30
    st.write(f'{name}, Your age is :')
    st.badge(f'{yrs} years and {month} month {day} days.', color='green')
elif button:
    st.badge('Value missing...',color='red')