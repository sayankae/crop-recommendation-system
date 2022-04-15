import streamlit as st
import pandas as pd
import numpy as np
import random

import matplotlib.pyplot as plt
import seaborn as sns

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

colorarr = ['#0592D0','#Cd7f32', '#E97451', '#Bdb76b', '#954535', '#C2b280', '#808000','#C2b280', '#E4d008', '#9acd32', '#Eedc82', '#E4d96f',
           '#32cd32','#39ff14','#00ff7f', '#008080', '#36454f', '#F88379', '#Ff4500', '#Ffb347', '#A94064', '#E75480', '#Ffb6c1', '#E5e4e2',
           '#Faf0e6', '#8c92ac', '#Dbd7d2','#A7a6ba', '#B38b6d']


@st.cache
def load_data():
	cropdf = pd.read_csv("Crop_recommendation.csv")
	return cropdf


cropdf = load_data()

def show_explore_page():
	st.title("Data Visualization")


	crop_summary = pd.pivot_table(cropdf,index=['label'],aggfunc='mean')
	crop_summary_N = crop_summary.sort_values(by='N', ascending=False)
  
	fig = make_subplots(rows=1, cols=2)

	top = {
	    'y' : crop_summary_N['N'][0:10].sort_values().index,
	    'x' : crop_summary_N['N'][0:10].sort_values()
	}

	last = {
	    'y' : crop_summary_N['N'][-10:].index,
	    'x' : crop_summary_N['N'][-10:]
	}

	fig.add_trace(
	    go.Bar(top,
	           name="Most nitrogen required",
	           marker_color=random.choice(colorarr),
	           orientation='h',
	          text=top['x']),
	    
	    row=1, col=1
	)

	fig.add_trace(
	    go.Bar(last,
	           name="Least nitrogen required",
	           marker_color=random.choice(colorarr),
	           orientation='h',
	          text=last['x']),
	    row=1, col=2
	)
	fig.update_traces(texttemplate='%{text}', textposition='inside')
	fig.update_layout(title_text="Nitrogen (N)",
	                  plot_bgcolor='white',
	                  font_size=12, 
	                  font_color='black',
	                 height=500)

	fig.update_xaxes(showgrid=False)
	fig.update_yaxes(showgrid=False)

	st.plotly_chart(fig, use_container_width=True)

	crop_summary_P = crop_summary.sort_values(by='P', ascending=False)
  
	fig = make_subplots(rows=1, cols=2)

	top = {
	    'y' : crop_summary_P['P'][0:10].sort_values().index,
	    'x' : crop_summary_P['P'][0:10].sort_values()
	}

	last = {
	    'y' : crop_summary_P['P'][-10:].index,
	    'x' : crop_summary_P['P'][-10:]
	}

	fig.add_trace(
	    go.Bar(top,
	           name="Most phosphorus required",
	           marker_color=random.choice(colorarr),
	           orientation='h',
	          text=top['x']),
	    
	    row=1, col=1
	)

	fig.add_trace(
	    go.Bar(last,
	           name="Least phosphorus required",
	           marker_color=random.choice(colorarr),
	           orientation='h',
	          text=last['x']),
	    row=1, col=2
	)
	fig.update_traces(texttemplate='%{text}', textposition='inside')
	fig.update_layout(title_text="Phosphorus (P)",
	                  plot_bgcolor='white',
	                  font_size=12, 
	                  font_color='black',
	                 height=500)

	fig.update_xaxes(showgrid=False)
	fig.update_yaxes(showgrid=False)

	st.plotly_chart(fig, use_container_width=True)


	crop_summary_K = crop_summary.sort_values(by='K', ascending=False)
  
	fig = make_subplots(rows=1, cols=2)

	top = {
	    'y' : crop_summary_K['K'][0:10].sort_values().index,
	    'x' : crop_summary_K['K'][0:10].sort_values()
	}

	last = {
	    'y' : crop_summary_K['K'][-10:].index,
	    'x' : crop_summary_K['K'][-10:]
	}

	fig.add_trace(
	    go.Bar(top,
	           name="Most potassium required",
	           marker_color=random.choice(colorarr),
	           orientation='h',
	          text=top['x']),
	    
	    row=1, col=1
	)

	fig.add_trace(
	    go.Bar(last,
	           name="Least potassium required",
	           marker_color=random.choice(colorarr),
	           orientation='h',
	          text=last['x']),
	    row=1, col=2
	)
	fig.update_traces(texttemplate='%{text}', textposition='inside')
	fig.update_layout(title_text="Potassium (K)",
	                  plot_bgcolor='white',
	                  font_size=12, 
	                  font_color='black',
	                 height=500)

	fig.update_xaxes(showgrid=False)
	fig.update_yaxes(showgrid=False)

	st.plotly_chart(fig, use_container_width=True)

	fig = go.Figure()
	fig.add_trace(go.Bar(
	    x=crop_summary.index,
	    y=crop_summary['N'],
	    name='Nitrogen',
	    marker_color='indianred'
	))
	fig.add_trace(go.Bar(
	    x=crop_summary.index,
	    y=crop_summary['P'],
	    name='Phosphorous',
	    marker_color='lightsalmon'
	))
	fig.add_trace(go.Bar(
	    x=crop_summary.index,
	    y=crop_summary['K'],
	    name='Potash',
	    marker_color='crimson'
	))

	fig.update_layout(title="N, P, K values comparision between crops",
	                  plot_bgcolor='white',
	                  barmode='group',
	                  xaxis_tickangle=-45)

	st.plotly_chart(fig, use_container_width=True)


	fig = px.bar(crop_summary, x=crop_summary.index, y=["rainfall", "temperature", "humidity"])
	fig.update_layout(title_text="Comparision between rainfall, temerature and humidity",
	                  plot_bgcolor='white',
	                 height=500)

	fig.update_xaxes(showgrid=False)
	fig.update_yaxes(showgrid=False)

	st.plotly_chart(fig, use_container_width=True)


	