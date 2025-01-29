# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 09:24:03 2024

@author: B
"""

import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Title heading")

st.write("Hello, Streamlit!")

st.header("Sample Data")

data = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})

# Display the data in the Streamlit app
st.write(data)

# Create a Plotly figure
fig = px.line(data, x="x", y="y", title="Simple Plotly Example")

# Display the plot in the Streamlit app
st.plotly_chart(fig)

st.title("Hello, Streamlit!")

st.title("NEVER USE SPACES IN FOLDER NAMES")

st.write("Beating my drum")

number = st.slider("You picked a number.",1,100)

st.write(f"You picked {number}")
# -*- coding: utf-8 -*-


