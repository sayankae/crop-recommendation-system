import streamlit as st
import pickle
import numpy as np



def load_model():
	with open('saved_steps.pkl', 'rb') as file:
		data = pickle.load(file)

	return data

def load_image(newdata):
	image_address = {"apple":"./crop_pic/apple.jpg","banana":"./crop_pic/banana.jpg","blackgram":"./crop_pic/blackgram.jpg","chickpea.jpg":"./crop_pic/chickpea.jpg","coconut":"./crop_pic/coconut.jpg",
					"coffee":"./crop_pic/coffee.jpg","cotton":"./crop_pic/cotton.jpg","grapes":"./crop_pic/grapes.jpg","jute":"./crop_pic/jute.jpg","kidneybeans":"./crop_pic/kidneybeans.jpg",
					"lentil":"./crop_pic/lentil.jpg","maize":"./crop_pic/maize.jpg","mango":"./crop_pic/mango.jpg","mothbean":"./crop_pic/mothbean.jpg","mungbean":"./crop_pic/mungbean.jpg",
					"muskmelon":"./crop_pic/muskmelon.jpg","orange":"./crop_pic/orange.jpg","papaya":"./crop_pic/papaya.jpg","pigeonpeas":"./crop_pic/pigeonpeas.jpg","pomegranate":"./crop_pic/pomegranate.jpg",
					"rice":"./crop_pic/rice.jpg","watermelon":"./crop_pic/watermelon.jpg"}

	if newdata[0] in image_address:
		return image_address[newdata[0]]
	else:
		return None

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
		if load_image(newdata) is not None:
			st.image(load_image(newdata))
