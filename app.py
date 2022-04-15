import streamlit as st
from recommend import show_recommend_page
from explore import show_explore_page

page = st.sidebar.selectbox("Explore or Recommend", ("Recommend", "Explore"))

if page == "Recommend":
	show_recommend_page()
else:
	show_explore_page()