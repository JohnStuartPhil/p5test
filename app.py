import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.study import study_body
from app_pages.page_prospect import page_prospect_body
from app_pages.page4 import page4_body
from app_pages.page5 import page5_body

# Create an instance
app = MultiPage(app_name="Iowa House Prices")

# Add your app pages here using .add_page()
app.app_page("Project Summary", page_summary_body)
app.app_page("Study", study_body)
app.app_page("Prospect Page", page_prospect_body)
app.app_page("Page 4 (currently blank)", page4_body)
app.app_page("Page 5 (currently blank)", page5_body)

app.run()