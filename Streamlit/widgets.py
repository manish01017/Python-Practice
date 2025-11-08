import streamlit as st

##Text Input widget
st.title('Strealit Text Input')
name=st.text_input('Enter your name:', 'Type here...')

if name:
    st.write(f'Hello, {name}!')
else:
    st.write('Please enter your name above.')

##Slider widget
age=st.slider('Select your age:', 0, 100, 25) # slider(comment,min,max,default ( the value it will show initially))
st.write(f'You are {age} years old.')

##Selectbox widget
options= ['Java', 'Python', 'C++', 'JavaScript']
language=st.selectbox('Select your favorite programming language:', options)
st.write(f'Your favorite programming language is {language}.')

##upldoad file widget
uploaded_file=st.file_uploader('Choose a csv file:',type='csv')
if uploaded_file is not None:
    import pandas as pd
    df=pd.read_csv(uploaded_file)
    st.write('Uploaded File:')
    st.write(df)