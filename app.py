import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
st.title('hi!!')

st.write('# Gender')

man_woman = st.slider('gender', 0, 30, 15)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

def open_img(sexibility):
    img_path = f'img/img{"%0.2d" %sexibility}.png'
    img = Image.open(img_path)
    return img

st.image(open_img(man_woman))

st.subheader(f'Gender of the one: {"%0.3f" %(man_woman/30 * 100)} % woman')



