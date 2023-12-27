import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.pipeline import Pipeline
from PIL import Image

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to use this extra ML tool 👋")

st.sidebar.success("Select the step")

st.markdown(
    """
    Features for our platform
    **👈 Try to choose step from the sidebar**
    




    ### Pre-processing ✅
    - Data Standardization
    - Data Transformation
    - Categorical Variable
    - Dimensionality Reduction

    
    ### Do you want to learn more?❔
    - Check [streamlit.io](https://streamlit.io)
    - check  [Doc](https://docs.streamlit.io)
"""
)


st.markdown("""
    ### Flexible interface with SAP IBP CI-DS
            """)

# Load your images
image1 = Image.open("pic3.png")

# Display image in Markdown
st.markdown(f"![Image]({image1})", unsafe_allow_html=True)

# Local image path
local_image_path = "pic3.png"

# Display local image in Markdown
st.markdown(f"![Image]({local_image_path})", unsafe_allow_html=True)