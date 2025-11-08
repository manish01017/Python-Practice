import streamlit as st
import pandas as pd
import numpy as np


## Title of the application
st.title("Hello Streamlit!")

## Display a simple text
st.write("This is a simple text")

##create a data frame
df = pd.DataFrame({'first column': [1, 2, 3, 4],
                   'second column': [10, 20, 30, 40]})
df.to_csv('sample_data.csv', index=False)

## Display the data frame
st.write("Here is a simple DataFrame:")
st.write(df)

## Display a line chart
chart_data =  pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

