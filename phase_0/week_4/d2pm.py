import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='nikki awesome app',
    # page_icon=,
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': 'https://google.com',
        'Report a bug': 'https://google.com',
        'About': '# AWE-SUUMMMM!!'
    }
)

'''
# My App
## Media
'''

img = Image.open('./data/2-4.jpg')

st.image(img, caption='Eiffel Tower')

#################### Column  ####################
col1, col2, col3 = st.columns(3)

with col1:
    st.header('A cat')
    # st.image("https://static.streamlit.io/examples/cat.jpg")
    st.image(img, caption='Eiffel Tower')
with col2:
    st.subheader('A dog')
    st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
    st.header('An owl')
    st.image("https://static.streamlit.io/examples/owl.jpg")

#################### Column using variable  ####################
col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader('A wide column with a chart')
col1.line_chart(data)

col2. subheader('A narrow column with the data')
col2.write(data)


#################### Image inside st.expander  ####################
st.line_chart({'data': [1, 5, 2, 6, 2, 1]})

with st.expander('See explanation'):
    st.write(
        '''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
        '''
    )

    st.image("https://static.streamlit.io/examples/dice.jpg")


#################### Container using with notation  ####################
with st.container():
    st.write('This is inside container')
    st.bar_chart(np.random.randn(50, 3))

