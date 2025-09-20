import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_house_price_records_data

def page_predict_sale_price_body():

    st.write("### ML Pipeline: Predict Sale Price")
    # display pipeline training summary conclusions
    st.info(
        f"* A Regressor model  was fitted"
        )
    st.write("---")

   