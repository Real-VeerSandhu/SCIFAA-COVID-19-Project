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
    nav = st.selectbox('Navigation', ['Home', 'Analysis Charts', 'Data Model'])
    if nav == 'Home':
        st.markdown('### Welcome')
        st.write('This app contains all developments in the Canada v.s. USA COVID-19 Analysis. The project was done by Veer Sandhu as a Data Science intern at SCI FAA')
        st.markdown('*Write-Up (To Be Attached)*')
    elif nav == 'Analysis Charts':
        combined = pd.read_csv('App/Data/out-data.csv')
        
        figW = px.line(combined, x='Date', y='Cases', color='Country', title = "Confirmed Cases Over Time in the USA vs Canada")
        figW2 = px.line(combined, x='Date', y='Deaths', color='Country', title = "Confirmed Deaths Over Time in the USA vs Canada")
        fig1 = px.line(combined, x='Date', y='Cases/Population', color='Country', title = "Cases per 100 People in the USA vs Canada", labels={'Cases/Population': 'Cases per 100 People'})
        fig2 = px.line(combined, x='Date', y='Diff Cases/Population', color='Country', title = "Increase/Decrease in Cases per 100 People in the USA vs Canada", labels={'Diff Cases/Population': 'Change in Cases per 100 People'})
        fig3 = px.line(combined, x='Date', y='Deaths/Cases', color='Country', title = "Deaths per 100 Cases in the USA vs Canada", labels={'Deaths/Cases': 'Deaths per 100 Cases'})
        fig4 = px.line(combined, x='Date', y='Tests/Cases', color='Country', title = "Tests per Case in the USA vs Canada", labels={'Tests/Cases': 'Tests per Case'})

        col1, col2 = st.beta_columns([1,1])
        with col1:
            st.plotly_chart(figW)
            st.plotly_chart(fig1)
        with col2:
            st.plotly_chart(figW2)
            st.plotly_chart(fig2)

        col3, col4 = st.beta_columns([1,1])
        with col3:
            st.plotly_chart(fig3)
        with col4:
            st.plotly_chart(fig4)
    elif nav == 'Data Model':
        st.write('Data Modelling with Machine Learning and AI')

    


    

if __name__ ==  '__main__':
    main()