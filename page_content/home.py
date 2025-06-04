import streamlit as st
from PIL import Image
import os #operating system

def home_page(): # add a function to display the home page in streamlit app
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>Jing Ma</h4>
        <p>Recent Master's Graduate in Marketing<br>
        Chinese University of Hong Kong<br>
        12 Chak Cheung St., Ma Liu Shui, HKSAR<br>
        <a href="mailto:1155216003@link.cuhk.edu.hk">1155216003@link.cuhk.edu.hk</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "image.png")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        I am a recent master's graduate in Marketing from Chinese University of Hong Kong, eager to apply my knowledge and skills in a professional setting. During my academic journey, I developed a strong foundation in digital marketing and statistical analysis.

        As part of my master's program, I completed some projects that involved working with real-world datasets and applying various marketing theories and analytical skills. These projects allowed me to gain hands-on experience in data preprocessing, model building, and analysis.
        I am a quick learner, a collaborative team player, and possess strong problem-solving skills. I am excited to contribute my skills and grow as a digital marketing specialist in a dynamic and challenging environment.
        """
    )

    st.markdown(
        """
        ### Skills
        - Programming Languages: Python, R
        - Video Editing: Adobe Premiere, Vegas
        - Photo Editing: Photoshop
        - Statistical Analysis: Hypothesis Testing, Regression Analysis
        - Communication: Presentation Skills, Technical Writing
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 
