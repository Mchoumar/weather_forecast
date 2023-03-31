import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")

# streamlit input for the city name, forcast slider, and view select
city_name = st.text_input("Place: ")
forecast_days = st.slider("Forecast Days", 1, 5,
                          help="Select the number of forecasted days")
data_view = st.selectbox("Select data to view",("Temperature", "Sky"))

st.subheader(f"{data_view} for the next {forecast_days} days in {city_name}")

# Checks if the user provided a city name before calling the function
if city_name:
    try:
        # Get the temp/sky data
        filtered_data = get_data(city_name, forecast_days, data_view)

        # filtering the data depending on the data view
        if data_view == "Temperature":
            temperature = [dictl['main']['temp'] / 10 for dictl in filtered_data]
            dates = [dictl["dt_txt"] for dictl in filtered_data]

            # presents the data
            figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if data_view == "Sky":
            sky_conditions = [dictl['weather'][0]['main'] for dictl in filtered_data]
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            images_path = [images[condition] for condition in sky_conditions]
            st.image(images_path, width=115)
    except KeyError:
        st.warning("You should enter a city name!")

