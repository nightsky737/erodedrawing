import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import matplotlib.pyplot as plt
from rivereroder import *

st.write("Welcome to dig a trench simulator!")
st.write("Draw on the canvas below to dig a trench!")

data = st_canvas(
    fill_color="rgba(255, 165, 0, 1)", 
    stroke_width=1,
    stroke_color="#000000",
    background_color="#FFFFFF",
    update_streamlit=True,
    height=500,
    width=500,
    drawing_mode="freedraw",
    key="canvas",
)

if st.button("Click to make the river from ur image!"):
    if data is not None and data.image_data is not None:
        img_data = data.image_data #is 255. 
        overlayed_img = overlay_img(img_data)
        raster_grid, flow_accumulator, eroder = make_simulation(overlayed_img)
        st.write("Pre erosion river")
        fig, ax = plt.subplots()
        ax.imshow(overlayed_img)

        st.session_state["prefig"] = fig
        st.session_state.grid = raster_grid
        st.session_state.flow_accumulator = flow_accumulator
        st.session_state.eroder = eroder
        st.session_state.overlayed_img =overlayed_img

if st.session_state.get("prefig") != None:
    st.write("showing")
    st.pyplot(st.session_state.get("prefig"))

        
if st.button("Click to erode the river!"):
    if st.session_state.get("flow_accumulator") == None:
        st.write("Please make the river first!")
    else:
        run_simulation(st.session_state.flow_accumulator, st.session_state.eroder)
        st.write("Post erosion")
        fig, ax = plt.subplots()
        ax.imshow(st.session_state.grid.at_node["topographic__elevation"].reshape(st.session_state.overlayed_img.shape))
        st.pyplot(fig)

