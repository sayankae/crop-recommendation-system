import streamlit as st
import pickle
import numpy as np



def load_model():
	with open('saved_steps.pkl', 'rb') as file:
		data = pickle.load(file)

	return data

data = load_model()

model = data["model"]

def show_recommend_page():
	st.title("Crop Recommendation System")

	st.write("""### We need some information to recommend the best possible Crop""")

	nitrogen = st.slider("Nitrogen in Soil kg/ha",0, 200, 20)
	phosphorus = st.slider("Phosphorus in Soil kg/ha",0, 200, 20)
	potassium = st.slider("Potassium in Soil kg/ha",0, 200, 20)
	temperatue = st.slider("Temperature in celcius",10, 45, 1)
	humidity = st.slider("Relative humidty in %",0, 100, 5)
	pH = st.slider("pH level of soil",5.0, 8.0, 0.1)
	rainfall = st.slider("Rainfall in mm",0, 400, 25)

	ok = st.button("Recommend Crop")

	if ok:
		data = [[nitrogen,phosphorus,potassium,temperatue,humidity,pH,rainfall]]
		newdata = model.predict(np.array(data,dtype=float))
		st.subheader(f"The best possible crop for this soil type is {newdata[0]}.")