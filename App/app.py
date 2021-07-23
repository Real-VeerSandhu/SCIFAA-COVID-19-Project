import streamlit as st 
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = "notebook"


st.markdown("""
# Hello
Double Click for Original Zoom
""")


df = px.data.gapminder().query("country=='Canada'")
df

fig0 = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
st.plotly_chart(fig0)
st.write('yes Yes')