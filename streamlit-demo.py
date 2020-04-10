import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random
st.title(f"Hello, World! {random.random()}")
x = st.slider('x', -10., 10.)
phi = np.linspace(-10, 10, 300)
plt.plot(np.sin(phi * x))
st.pyplot()

