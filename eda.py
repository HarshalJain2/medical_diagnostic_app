import streamlit as st
st.title("The EDA Page")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)
plt.style.use('fivethirtyeight')

### Step2. Load and View the data

data=pd.read_csv('data.csv')
st.subheader('Data View')
st.write(data.head())

st.subheader('Descriptives')
st.write(data.describe().T)

data.hist()
st.subheader('Histograms')
plt.tight_layout()
st.pyplot()
