import streamlit as st
import pandas as pd

st.title('My first app')

height = st.slider('Select your height(in cm)', 150, 200, 170)
weaight = st.slider('Select your weight(in kg)', 40, 100, 60)

bmi = weaight / (height/100)**2

st.write(f'Your BMI is {bmi}')

if bmi < 18.5:
    st.write('Underweight')
elif bmi >= 18.5 and bmi < 25:
    st.write('Normal weight')
elif bmi >= 25 and bmi < 30:
    st.write('Overweight')
else:
    st.write('Obesity')

