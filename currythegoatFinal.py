import os
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import warnings
warnings.filterwarnings('ignore')
from PIL import Image

st.set_page_config(page_title="Stephen Curry Shot Plot Data", page_icon=":basketball:", layout="wide")
st.title(":basketball: Stephen Curry Career Shot Plot by Arjun Singh ")
st.markdown(
    """
    <style>
    .main .block-container {
        padding-top: 3rem; /* Adjust this value to create space above the title */
    }
    .make-percentage {
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the dataset directly
df = pd.read_csv("stephen_curry_shots_new.csv")

# Load the court image
court_img = Image.open('NBAHALFCOURTREAL.PNG')

# Rename columns for easier access (assuming they are already in the CSV)
df.columns = ['Season', 'X_Loc', 'Y_Loc', 'Quarter', 'Time', 'Shot Type', 'Made']

# Extract the start and end year of each season
df['Start Year'] = df['Season'].apply(lambda x: int(x[:4]))
df['End Year'] = df['Season'].apply(lambda x: int(x[5:9]))

# Get the unique start years for the slider
start_years = sorted(df['Start Year'].unique())

# Sidebar filters
selected_year_range = st.sidebar.slider(
    "Select a range of seasons (2009 = 2009-10 season and vice versa)",
    min_value=start_years[0],
    max_value=start_years[-1],
    value=(start_years[0], start_years[-1]),
    step=1,
    format="%d"
)

# Filter the DataFrame based on the selected start year range
filtered_df = df[(df['Start Year'] >= selected_year_range[0]) & (df['Start Year'] <= selected_year_range[1])]

# Filter by Quarter
quarters = ['1st quarter', '2nd quarter', '3rd quarter', '4th quarter']
selected_quarters = st.sidebar.multiselect("Select Quarter(s)", quarters, default=quarters)
filtered_df = filtered_df[filtered_df['Quarter'].isin(selected_quarters)]

# Filter by Time (slider for time range, assuming time is in "minutes:seconds" format)
selected_time_range = st.sidebar.slider(
    "Select Time Range (Time left in quarter) (mm:ss)",
    min_value=0.0,
    max_value=12.0,
    value=(0.0, 12.0),
    step=0.1,
    format="%f"
)

# Convert 'Time' to numeric minutes for filtering
filtered_df['Time (mins)'] = filtered_df['Time'].apply(lambda x: float(x.split(':')[0]) + float(x.split(':')[1]) / 60)
filtered_df = filtered_df[(filtered_df['Time (mins)'] >= selected_time_range[0]) & (filtered_df['Time (mins)'] <= selected_time_range[1])]

# Filter by Shot Type
shot_types = filtered_df['Shot Type'].unique().tolist()
selected_shot_types = st.sidebar.multiselect("Select Shot Type(s)", shot_types, default=shot_types)
filtered_df = filtered_df[filtered_df['Shot Type'].isin(selected_shot_types)]

# Filter by Made Shot with the option to select True, False, or both
made_options = ['True', 'False']  # Display options as strings
selected_made_shots = st.sidebar.multiselect("Made Shot?", made_options, default=made_options)

# Convert the selected options back to boolean for filtering
selected_made_shots = [True if x == 'True' else False for x in selected_made_shots]
filtered_df = filtered_df[filtered_df['Made'].isin(selected_made_shots)]

# Calculate the Make Percentage
total_shots = len(filtered_df)
made_shots = filtered_df['Made'].sum()
make_percentage = (made_shots / total_shots) * 100 if total_shots > 0 else 0

# Create two columns
col1, col2 = st.columns([0.8, 3])  # Adjust the ratios to control the space
