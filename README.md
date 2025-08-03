# Info
This project is a simple project that helps to demonstrate erosion patterns over the course of 2000 years by allowing the user to draw a river or design that will then be eroded, with this project also showing the finished result.

It does so by creating a shallow slope that the user can then carve a deeper trench into. The trench is both at a lower elevation than the rest of the slope and has a steeper gradient than the slope. I then use sklearn's gaussian blur to smooth out the walls of the trench, before running the erosion simulation.

# DEMO
[Link](http://37.27.51.34:34961/)
# Screenshots 
<img width="817" height="579" alt="image" src="https://github.com/user-attachments/assets/99459462-6232-4792-9dc2-0e0690916c99" />
<img width="625" height="877" alt="image" src="https://github.com/user-attachments/assets/74464279-dddf-4509-9ba4-6c47a5a988c4" />

# Hosting it yourself
1. Clone the repo
2. Run pip install -r requirements.txt
3. Run streamlit run streamlit_app.py

# Additional Notes
I made this project for personal use with the help of landlab and streamlit, more specifically with the streamlit-drawable-canvas, fastscapeeroder, and flowaccumulator. 
