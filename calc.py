import streamlit as st

st.header("welcome to my calculator")

x=st.number_input('input your first number')
y=st.number_input('input your second number')

if st.button('Add'):
    z=x+y
    st.write(z)
if st.button('subtract'):
    z=x-y
    st.write(z)
