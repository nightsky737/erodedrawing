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
        print(np.min(img_data[:,:,0]))
        overlayed_img = overlay_img(img_data)
        raster_grid, flow_accumulator, eroder = make_simulation(overlayed_img)
        st.write("Pre erosion river")
        fig, ax = plt.subplots()
        ax.imshow(overlayed_img)
        st.pyplot(fig)
        
if st.button("Click to erode the river!"):
    run_simulation(flow_accumulator, eroder)
    st.write("Post erosion")
    ax.imshow(overlayed_img)

