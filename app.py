import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.page_house_price_study import page_house_price_study_body
from app_pages.page_prediction import page_prediction_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_predict_sale_price import page_predict_sale_price_body

# Create an instance
app = MultiPage(app_name="Iowa House Prices")

# Add your app pages here using .add_page()
app.app_page("Project Summary", page_summary_body)
app.app_page("House Price Study", page_house_price_study_body)
app.app_page("Prediction of Sale Price", page_prediction_body)
app.app_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.app_page("ML: Predict Sale Price", page_predict_sale_price_body)

app.run()