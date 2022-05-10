import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title('My First App')

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame(
    {
        'first_column': [1, 2, 3, 4],
        'second_column': [10, 20, 30, 40]
    }
))

"""
# My First App
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame(
    {
        'first_column': [1, 2, 3, 4],
        'second_column': [10, 20, 30, 40]
    }
)

df

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )

    chart_data

option = st.selectbox(
    'Which number do you like best?',
    df['first_column'],
    key=1234
)

'You selected:', option

option = st.sidebar.selectbox(
    'Which number do you like best?',
    df['first_column'],
    key='option2'
)

'You selected:', option

left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write('Woohoo!')

expander = st.expander('FAQ')
expander.write('Here you could put in some really, really long explanations...')

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.001)

"...and now we're done!"

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')
csv = convert_df(df)
st.download_button(
    label='Download data as CSV',
    data=csv,
    file_name='large_df.csv',
    mime='text/csv'
)

fig = plt.figure()
# fig, ax = plt.subplots()
df['first_column'].plot()
st.pyplot(fig)
# st.plotly_chart(fig)
