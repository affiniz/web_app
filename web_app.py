# import streamlit as st
# st.title("Hello Streamlit")
# # header
# st.header("Welcome to the my data analytics app")

# # code
# code = '''
# def add(a,b):
#     print("a+b = ", a+b)
# '''
# st.code(code, language="python")

# # toggle
# toggle_on = st.toggle('Show something')

# if toggle_on:
#     st.write('This is something')

import pandas as pd
import streamlit as st
import plotly.express as px

# data = pd.read_csv('iris_data.csv')

# fig = px.scatter(data, x="SepalLengthCm", y="SepalWidthCm", color="Species",
#                  size='SepalLengthCm', hover_data=['SepalWidthCm'])

# st.plotly_chart(fig, use_container_width=True)

import pandas as pd
data = pd.read_csv("iris_data.csv")

import plotly.express as px
fig = px.scatter(data, x="SepalLengthCm", y="SepalWidthCm", color="Species")
st.plotly_chart(fig, use_container_width=True)
