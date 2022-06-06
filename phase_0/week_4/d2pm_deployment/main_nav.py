#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import data_viz, hypo_test
import streamlit as st

PAGES = {
    'Data Visualization': data_viz,
    'Hypothesis Testing': hypo_test
}

selected = st.sidebar.selectbox(
    'Select Page:',
    options=PAGES.keys()
)

page = PAGES[selected]

page.app()