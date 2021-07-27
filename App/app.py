import streamlit as st 
import plotly.express as px
import pandas as pd


st.set_page_config(page_title="COVID-19 Graph App", page_icon="📈", layout='wide', initial_sidebar_state="collapsed")

st.markdown("""
# Canada v.s. USA COVID-19 Analysis
""")
st.write("""
        [Full Project](https://github.com/Real-VeerSandhu/SCIFAA-COVID-19-Project)
        """)
st.write('----')

def main():
    combined = pd.read_csv('Data/out-data.csv')

    fig1 = px.line(combined, x='Date', y='Cases/Population', color='Country', title = "Cases per Person in the USA vs Canada", labels={'Cases/Population': 'Cases per Person'})
    fig2 = px.line(combined, x='Date', y='Cases', color='Country', title = "Total Cases in the USA vs Canada (Simple)")
    fig3 = px.line(combined, x='Date', y='Deaths/Cases', color='Country', title = "Deaths per Case in the USA vs Canada", labels={'Deaths/Cases': 'Deaths per Case'})
    fig4 = px.line(combined, x='Date', y='Tests/Cases', color='Country', title = "Tests per Case in the USA vs Canada", labels={'Tests/Cases': 'Tests per Case'})


    col1, col2 = st.beta_columns([1,1])
    with col1:
        st.plotly_chart(fig1)
    with col2:
        st.plotly_chart(fig2)

    col3, col4 = st.beta_columns([1,1])
    with col3:
        st.plotly_chart(fig3)
    with col4:
        st.plotly_chart(fig4)
    


    

if __name__ ==  '__main__':
    main()