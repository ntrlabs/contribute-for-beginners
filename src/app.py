import streamlit as st
import pandas as pd
import json
import os

# Path to the contributions file
CONTRIBUTIONS_FILE = "contributors.json"

# Load the contributions from the JSON file
def load_contributions():
    if os.path.exists(CONTRIBUTIONS_FILE):
        with open(CONTRIBUTIONS_FILE, "r") as f:
            return json.load(f)
    return []

# Display Streamlit page
st.markdown("# List of contributors to `Contributors For Beginners`")
st.write("This page shows all the contributors to this project and the time of their contributions.")

# Load and display contributions
contributions = load_contributions()
print(contributions)
if contributions:
    df = pd.DataFrame(contributions)
    try:
        df['contributed_at'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values(by='timestamp', ascending=False)
    except KeyError:
        df['contributed_at'] = None
    st.dataframe(df)
else:
    st.write("Nothing to show here..")
