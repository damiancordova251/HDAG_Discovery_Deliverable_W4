import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import warnings
warnings.filterwarnings('ignore')


st.title ("W4 Deliverable: Linear Regression and Streamlit")
st.subheader("By: Damian C.")

st.header("Background Selector")

bg_col = st.selectbox(
    "Background color",
    ["Dark", "Blue", "Purple", "Red"]
)

map_col = {
    "Red": "#8B0000",
    "Blue": "#0B3D91",
    "Purple":  "#520067",
    "Dark": "#1e1e1e"
}

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {map_col[bg_col]};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.header("Graph Selection")

linreg = st.checkbox("Linear Regression: Housing Units vs. Population (Log Scaled)")
piechart = st.checkbox("Pie Chart: Distribution of Assisted Unit Types in 2022")


# Load data
df = pd.read_csv('Copy of merged_housing_population_with_growth.csv')


#Linreg Data: 
df_2022 = df[df['Year'] == 2022].copy()
df_2022_nogov = df_2022[df_2022['Government Assisted'] == 0].copy()
df_2022_withgov = df_2022[df_2022['Government Assisted'] > 0].copy()
for d in [df_2022, df_2022_nogov, df_2022_withgov]:
    d['log_Population_2025'] = np.log(d['Population_2025'] + 1)
    d['log_2010_Census_Units'] = np.log(d['2010 Census Units'] + 1)

#Pie Chart Data: 
df_yr_types_assistedun = df.loc[df['Year'] == 2022, ['Government Assisted', 'Tenant Rental Assistance', 'Single Family CHFA/ USDA Mortgages', 'Deed Restricted Units']]
total = df_yr_types_assistedun.sum()
labels = total.index.tolist()
sizes = total.values



if linreg: 
    X = df_2022[['log_2010_Census_Units']]
    y = df_2022['log_Population_2025']

    model = LinearRegression()
    model.fit(X, y)

    # Create plot
    fig, ax = plt.subplots(figsize=(10, 8))

    # Scatter points
    sns.scatterplot(
        x='log_2010_Census_Units',
        y='log_Population_2025',
        data=df_2022_nogov,
        label='No Gov',
        ax=ax
    )

    sns.scatterplot(
        x='log_2010_Census_Units',
        y='log_Population_2025',
        data=df_2022_withgov,
        label='With Gov',
        ax=ax
    )

    # Regression line
    x_range = np.linspace(
        df_2022['log_2010_Census_Units'].min(),
        df_2022['log_2010_Census_Units'].max(),
        100
    ).reshape(-1, 1)

    y_pred = model.predict(x_range)

    ax.plot(x_range, y_pred)

    ax.set_title("Housing Units vs Population (Log Scale)")
    ax.set_xlabel("Log Housing Units")
    ax.set_ylabel("Log Population")
    ax.legend()

    st.pyplot(fig)

if piechart: 
    fig, ax = plt.subplots(figsize=(10, 8))

    ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        textprops={'fontweight': 'bold'}
    )

    ax.set_title('Distribution of Assisted Unit Types in 2022')
    ax.axis('equal')
    plt.tight_layout()
    st.pyplot(fig)

st.header("Slider and Graph displays")

year = st.slider("Year", 2011, 2022, 2011)

df_yrvar_types = df.loc[df['Year'] == year, ['Government Assisted', 'Tenant Rental Assistance', 'Single Family CHFA/ USDA Mortgages', 'Deed Restricted Units']]
total = df_yrvar_types.sum()
labels = total.index.tolist()
sizes = total.values

fig, ax = plt.subplots(figsize=(10, 8))

ax.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    textprops={'fontweight': 'bold'}
   )

ax.set_title('Distribution of Assisted Unit Types in 2022')
ax.axis('equal')
plt.tight_layout()
st.pyplot(fig)

st.header("End :D")


