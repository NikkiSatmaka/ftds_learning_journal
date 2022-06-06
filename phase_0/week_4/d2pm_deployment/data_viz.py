#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from streamlit.elements import pyplot

def app():
    st.header('Data Vizualisation')

    st.subheader('Graph 1')
    data = np.random.randn(10, 1)
    st.line_chart(data)

    st.subheader('Graph 2')
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    fig = plt.figure()
    plt.plot(chart_data)
    st.pyplot(fig)