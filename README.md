# OpenWeatherMap API Wrapper

Simple function to get weather data in a tidy form for any lattitude and longitude. 
The function takes just four arguments: lat, long, api_key and an optional primary_key if it is used to build a dimensional table. 
It returns a single line pandas df. It can be used within a loop, but a free account only allows for 60 API calls a minute. 
