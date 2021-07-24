import streamlit as st 
import plotly.express as px
import pandas as pd



st.markdown("""
# Canda v.s. the US COVID-19 Analysis
Double Click for Original Zoom
""")
st.write('Comparing how metrics on how the countries dealt with the pandemic and measurment the damages caused')


combined = pd.read_csv('Data/out-data.csv')

fig0 = px.line(combined, x='Date', y='Cases/Population', color='Country', template = "plotly_dark", title = "Cases per Person in the USA vs Canada", labels={'Cases/Population': 'Cases per Person'})
fig1 = px.line(combined, x='Date', y='Deaths/Cases', color='Country', template = "plotly_dark", title = "Deaths per Case in the USA vs Canada", labels={'Deaths/Cases': 'Deaths per Case'})
fig2 = px.line(combined, x='Date', y='Tests/Cases', color='Country', template = "plotly_dark", title = "Tests per Case in the USA vs Canada", labels={'Tests/Cases': 'Tests per Case'})

st.plotly_chart(fig0)
st.plotly_chart(fig1)
st.plotly_chart(fig2)

