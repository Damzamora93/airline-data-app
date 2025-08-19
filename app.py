import streamlit as st
import pandas as pd
import plotly.express as px

# Set page title and icon
st.set_page_config(page_title="Airline Passenger Satisfaction Dataset Explorer", page_icon="")

# Sidebar navigation
page = st.sidebar.selectbox("Select a Page", ["Home", "Data Overview", "Exploratory Data Analysis", "Extras"])

# Load dataset
df = pd.read_csv('data/cleaned_airline_passenger_satisfaction.csv')

# Home Page
if page == "Home":
    st.title("✈ Airline Passenger Satisfaction Dataset 📊")
    st.subheader("Welcome to our Airline Satisfaction dataset explorer app!")
    st.write("""
        This app provides an interactive platform to explore the Airline Satisfaction Dataset. 
        You can visualize the distribution of data, explore relationships between features, and even make predictions on new data!
        Use the sidebar to navigate through the sections.
    """)
    st.image('airport.jpg', caption="Airport View")
    st.write("Use the sidebar to navigate between different sections.")


# Data Overview
elif page == "Data Overview":
    st.title("🔢 Data Overview")

    st.subheader("About the Data")
    st.write("""
       This dataset contains an airline passenger satisfaction survey. We are able to examine factors that are highly correlated to a satisfied (or dissatisfied) passenger.  
    """)
    st.image('inside.jpg', caption="Airport")

    # Dataset Display
    st.subheader("Quick Glance at the Data")
    if st.checkbox("Show DataFrame"):
        st.dataframe(df)
    

    # Shape of Dataset
    if st.checkbox("Show Shape of Data"):
        st.write(f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")


# Exploratory Data Analysis (EDA)
elif page == "Exploratory Data Analysis":
    st.title("📊 Exploratory Data Analysis (EDA)")

    st.subheader("Random Forest Model")
    st.write("""
       Random Forest model tested fairly well as we can see here with a 14230 true negative score which shows consistency and reliabilty in predicting the dissastisfied ratings.  Based on our EDA we were able to noticed higher delays in departure times often correlates to higher probability of a dissatisfied airline customer.  
    """)
    st.image('matrix.jpg', caption="Random Forest Confusion Matrix")

    st.write("""
       Our dissatisfied rating baseline target to reach using this model was set at 56.6%.  We were able to beat this score with a 94.9%   
    """)



    st.subheader("Select the type of visualization you'd like to explore:")
    eda_type = st.multiselect("Visualization Options", ['Histograms', 'Box Plots', 'Scatterplots', 'Count Plots'])

    obj_cols = df.select_dtypes(include='object').columns.tolist()
    num_cols = df.select_dtypes(include='number').columns.tolist()

    if 'Histograms' in eda_type:
        st.subheader("Histograms - Visualizing Numerical Distributions")
        h_selected_col = st.selectbox("Select a numerical column for the histogram:", num_cols)
        if h_selected_col:
            chart_title = f"Distribution of {h_selected_col.title().replace('_', ' ')}"
            if st.checkbox("Show by satisfaction"):
                st.plotly_chart(px.histogram(df, x=h_selected_col, color='satisfaction', title=chart_title, barmode='overlay'))
            else:
                st.plotly_chart(px.histogram(df, x=h_selected_col, title=chart_title))

    if 'Box Plots' in eda_type:
        st.subheader("Box Plots - Visualizing Numerical Distributions")
        b_selected_col = st.selectbox("Select a numerical column for the box plot:", num_cols)
        if b_selected_col:
            chart_title = f"Distribution of {b_selected_col.title().replace('_', ' ')}"
            st.plotly_chart(px.box(df, x='satisfaction', y=b_selected_col, title=chart_title, color='satisfaction'))

    if 'Scatterplots' in eda_type:
        st.subheader("Scatterplots - Visualizing Relationships")
        selected_col_x = st.selectbox("Select x-axis variable:", num_cols)
        selected_col_y = st.selectbox("Select y-axis variable:", num_cols)
        if selected_col_x and selected_col_y:
            chart_title = f"{selected_col_x.title().replace('_', ' ')} vs. {selected_col_y.title().replace('_', ' ')}"
            st.plotly_chart(px.scatter(df, x=selected_col_x, y=selected_col_y, color='satisfaction', title=chart_title))

    if 'Count Plots' in eda_type:
        st.subheader("Count Plots - Visualizing Categorical Distributions")
        selected_col = st.selectbox("Select a categorical variable:", obj_cols)
        if selected_col:
            chart_title = f'Distribution of {selected_col.title()}'
            st.plotly_chart(px.histogram(df, x=selected_col, color='satisfaction', title=chart_title))

if page == "Extras":


    
    st.divider()

    st.title("Dataset Source & Notes")

    container = st.container(border=True)
    container.write("Original Dataset used in this Application is found here: ")
    st.write("- Note: This dataset was modified from this dataset by John D here 2 years prior. It has been cleaned up for the purposes of classification." \
    "")

    st.write("- Streamlit Application created by Damian Zamora" \
    "")

    # Now insert some more in the container
    container.write("https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction/data")

    st.image('data.jpg', caption="Data source")