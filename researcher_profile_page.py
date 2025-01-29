#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:58:13 2025

@author: donavanrooi
"""

import streamlit as st
import pandas as pd

# Title of the app
st.title("Researcher Profile Page")

st.image("https://media.geeksforgeeks.org/wp-content/uploads/20231130180326/Physiology.webp",
        width=300)

# Collect basic information
name = "Donavan Rooi"
field = "Cardiovascular Physiology"
institution = "North-West university"
research_biography= "Donavan's specific interests include large artery stiffness and early vascular aging"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")
st.write(f"**Research interest** {research_biography}")

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "27515230@mynwu.ac.za"
st.write(f"You can reach {name} at {email}.")
