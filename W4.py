import streamlit as st
import pandas as pd
import numpy as np
import time 

st.title("My Cool Dashboard!")
st.subheader("An analysis of the stuff that I analyzed")
st.write("This app displays many interactive elements that give insight into the data I analyzed.")

st.header("1. Text and Formatting")

st.markdown("""
- **Bold text**
- *Italic text*
- Links: [Streamlit website](https://streamlit.io)
""")

st.header("2. Widgets (User Inputs)")

# Text input box (default value = "Guest")
name = st.text_input("Enter your name:", "Guest")

# Slider (range: 0 to 100, default = 25)
age = st.slider("What is your age?", 0, 100, 25)

# Dropdown menu
zodiac = st.selectbox("Your star sign:", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",  "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])

# Display user inputs dynamically
st.write(f"Hello **{name}**! You are {age} years old and your star sign is {zodiac}!")

st.header("3. Charts and Plots")

# Random dataset (20 rows, 3 columns). When creating an actual dashboard, you will use real data.
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

# Line chart
st.line_chart(chart_data)

# Bar chart
st.bar_chart(chart_data)

# Area chart
st.area_chart(chart_data)


# Note that we can simply use a dataframe as the argument and it seamlessly creates the chart!

st.header("4. Layout and Columns")

# Create two columns side by side
col1, col2 = st.columns(2)

with col1:
    st.write("Left column chart")
    st.area_chart(chart_data)

with col2:
    st.write("Right column chart")
    st.scatter_chart(chart_data)

st.header("5. Session State (Keeping Data for a Session)")

# Initialize counter if it doesn't exist yet
if "counter" not in st.session_state:
    st.session_state.counter = 0

# Button to increment counter
if st.button("Increment counter"):
    st.session_state.counter += 1

# Display current counter value
st.write("Counter value:", st.session_state.counter)

st.header("6. Progress & Status")

# st.progress() makes a progress bar (0 to 100)
progress = st.progress(0)

# Use loop to update the progress bar
for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)

st.success("Done!")  # success message with green box


# For practical applications, you can make the progress bar align with something meaningful on the page.

st.header("7. Images and Media")

# Display an image from the web
st.image("https://placekitten.com/400/250", caption="Cute kitten 😺")

# Embed a video
st.video("https://www.w3schools.com/html/mov_bbb.mp4")