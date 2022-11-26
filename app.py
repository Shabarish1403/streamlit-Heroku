import streamlit as st

st.write("""
# Multiplication of two Numbers
""")

#Get Input
st.header('User Input Parameters')

def user_input_features():
    num1 = st.number_input("Number 1",min_value=0,max_value=999999999,step=1.0)
    num2 = st.number_input("Number 2",min_value=0,max_value=999999999,step=1.0)

    return f'Multiplication of {num1} and {num2} is {num1*num2}'

result = user_input_features()

st.subheader('Result')
st.write(result)
