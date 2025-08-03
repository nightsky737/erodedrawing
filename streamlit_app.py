import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import matplotlib.pyplot as plt
from rivereroder import *

st.write("Draw on the canvas below! Each stroke represents a trench being cut into a slightly sloped terrain!")

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

if st.button("Click to make terrain from your image!"):
    if data is not None and data.image_data is not None:
        img_data = data.image_data #is 255. 
        overlayed_img = overlay_img(img_data)
        raster_grid, flow_accumulator, eroder = make_simulation(overlayed_img)
        fig, ax = plt.subplots()
        im = ax.imshow(overlayed_img, cmap="gist_earth")
        ax.set_title("Pre erosion figure")
        color_bar = plt.colorbar(im, ax=ax)
        color_bar.set_label('Elevation')
        ax.set_axis_off()
        st.session_state["prefig"] = fig
        st.session_state.grid = raster_grid
        st.session_state.flow_accumulator = flow_accumulator
        st.session_state.eroder = eroder
        st.session_state.overlayed_img =overlayed_img

if st.session_state.get("prefig") != None:
    st.pyplot(st.session_state.get("prefig"))

        
if st.button("Click to erode the terrain!"):
    if st.session_state.get("flow_accumulator") == None:
        st.write("Please make the river first!")
    else:
        run_simulation(st.session_state.flow_accumulator, st.session_state.eroder)
        fig, ax = plt.subplots()
        im = ax.imshow(st.session_state.grid.at_node["topographic__elevation"].reshape(st.session_state.overlayed_img.shape))
        ax.set_axis_off()
        color_bar = plt.colorbar(im, ax=ax)
        color_bar.set_label('Elevation')
        ax.set_title("Post erosion figure")
        st.pyplot(fig)

