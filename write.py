import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')
st.subheader('Testing initial features!')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
    'Days': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    'Temperature (in Degrees)': [24, 22, 18, 20, 26]
})

st.write(df)

# Example 4
# Pass in multiple arguments:

st.write('Below is a DataFrame:', df, 'Above is a DataFrame')

# Example 5
# Display plots as well by passing it to a variable as follows:

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size ='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
