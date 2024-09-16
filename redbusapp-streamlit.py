import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error
import plotly.express as px

# Function to fetch data from MySQL
def load_data():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="jaini2002",  # Update password if needed
            database="guvi"
        )
        query = "SELECT * FROM bus_details"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df

    except Error as e:
        st.error(f"Error connecting to MySQL: {e}")
        return None

# Load data
df = load_data()

# Check if data is loaded properly
if df is None or df.empty:
    st.error("No data found or failed to load data from the database.")
else:
    # Display the first few rows of data for debugging purposes
    st.write("Data loaded successfully:", df.head())

    # Streamlit App Title
    st.title("Redbus Data Viewer and Filter")

    # Sidebar with search and filters
    st.sidebar.header("Filter Options")

    # Search functionality
    search_term = st.sidebar.text_input("Starting point to ending point", placeholder="Type a route name...")

    # Filter by Bus Type using dropdown
    bus_type = st.sidebar.selectbox(
        "Select Bus Type",
        options=["All"] + list(df["Bus_type"].unique())  # Include 'All' option
    )
    
    # Filter by Route using dropdown
    route_name = st.sidebar.selectbox(
        "Select Route",
        options=["All"] + list(df["Route_name"].unique())  # Include 'All' option
    )

    # Filter by Price Range using slider
    min_price, max_price = st.sidebar.slider(
        "Select Price Range",
        min_value=int(df["Price"].min()),
        max_value=int(df["Price"].max()),
        value=(int(df["Price"].min()), int(df["Price"].max()))
    )

    # Filter by Ratings using slider
    min_rating, max_rating = st.sidebar.slider(
        "Select Ratings Range",
        min_value=0.0, 
        max_value=5.0,  
        value=(1.0, 4.5)
    )

    # Filter by Availability using dropdown
    
    availability = st.sidebar.selectbox(
        "Seats Availability",
        options=["All", "Available", "Not Available"]
    )
    

    # Apply filters dynamically
    filtered_data = df.copy()

    if bus_type != "All":
        filtered_data = filtered_data[filtered_data["Bus_type"] == bus_type]

    if route_name != "All":
        filtered_data = filtered_data[filtered_data["Route_name"] == route_name]

    filtered_data = filtered_data[
        (filtered_data["Price"] >= min_price) &
        (filtered_data["Price"] <= max_price) &
        (filtered_data["Ratings"] >= min_rating) &
        (filtered_data["Ratings"] <= max_rating)
    ]

    if availability == "Available":
        filtered_data = filtered_data[filtered_data["Seats_Available"] != "0"]
    elif availability == "Not Available":
        filtered_data = filtered_data[filtered_data["Seats_Available"] == "0"]

    # Display filtered data
    st.write(f"Showing {len(filtered_data)} results:")
    st.dataframe(filtered_data)


    # Option to download the filtered data as a CSV
    st.download_button(
        label="Download Data as CSV",
        data=filtered_data.to_csv(index=False),
        file_name="filtered_bus_data.csv",
        mime="text/csv"
    )

    # Reset Filters button
    if st.sidebar.button("Reset Filters"):
        st.experimental_rerun()