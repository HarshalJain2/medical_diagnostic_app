import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pickle
st.title('Medical Diagnostic Preduction App')
st.markdown('Does the person had Diabetes?')

# Step1: Load the pickled/trained model
model = open('rfc_pickle', 'rb') # rb - read binary format;
clf = pickle.load(model)
model.close()

# Step2: Get the user input from front end
pregs = st.number_input('Pregnancies',0, 20, step=1) 
glucose = st.slider('Glucose',40, 200, 40) 
bp = st.slider('BloodPressure',20, 140, 20) 
skin = st.slider('SkinThickness',7, 99, 7)
insulin = st.slider('Insulin',14, 850, 14)
bmi = st.slider('BMI',18, 70, 18) 
dpf = st.slider('DiabetesPedigreeFunction',0.05, 2.5, 0.05) 
age = st.slider('Age',21, 90, 21)

# Step 3: Convert user input to model input
data = {
    'Pregnancies':pregs, 
    'Glucose':glucose,
    'BloodPressure':bp, 
    'SkinThickness':skin,
    'Insulin':insulin,
    'BMI':bmi,
    'DiabetesPedigreeFunction':dpf,
    'Age':age
    }
input_data = pd.DataFrame([data])

# Step 4: Get the predictions and print the result
prediction = clf.predict(input_data)[0]
if st.button('Predict'):
    if prediction==0:
        st.write('The person is Healthy')
    if prediction==1:
        st.write('The person is Diabetes')
