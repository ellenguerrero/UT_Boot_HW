{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Three observable trends based on data**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**1.** The cities with lattitude closer to the the equator (0 degrees) have higher temperatures that decrease the further away from the equator they get."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**2.** Humidity does not appear to be impacted by the distance from the equator."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**3.** Southern cities appear to have higher wind speeds. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# Dependencies and Setup\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import requests\n",
    "import time\n",
    "\n",
    "# Import API key\n",
    "import api_keys\n",
    "\n",
    "# Incorporated citipy to determine city based on latitude and longitude\n",
    "from citipy import citipy\n",
    "\n",
    "# Output File (CSV)\n",
    "output_data_file = \"output_data/cities.csv\"\n",
    "\n",
    "# Range of latitudes and longitudes\n",
    "lat_range = (-90, 90)\n",
    "lng_range = (-180, 180)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Generate Cities List"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# List for holding lat_lngs and cities\n",
    "lat_lngs = []\n",
    "cities = []\n",
    "\n",
    "# Create a set of random lat and lng combinations\n",
    "lats = np.random.uniform(low=-90.000, high=90.000, size=1500)\n",
    "lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)\n",
    "lat_lngs = zip(lats, lngs)\n",
    "\n",
    "# Identify nearest city for each lat, lng combination\n",
    "for lat_lng in lat_lngs:\n",
    "    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name\n",
    "    \n",
    "    # If the city is unique, then add it to a our cities list\n",
    "    if city not in cities:\n",
    "        cities.append(city)\n",
    "\n",
    "# Print the city count to confirm sufficient count\n",
    "len(cities)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Perform API Calls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# OpenWeatherMap API Key\n",
    "api_key = api_keys.api_key\n",
    "\n",
    "# Starting URL for Weather Map API Call\n",
    "units=\"imperial\"\n",
    "\n",
    "url = \"http://api.openweathermap.org/data/2.5/weather?\"\n",
    "query_url=f\"{url}appid={api_key}&units={units}&q=\"\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Show JSON dict/define variable**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#json is a dict\n",
    "response_json = requests.get(query_url+city).json()\n",
    "response_json"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Loop through cities list and add to dict. Skip error cities**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "citiesWeather=[]\n",
    "\n",
    "count=0\n",
    "for city in cities:\n",
    "    count = count + 1\n",
    "    #print(query_url+city)\n",
    "    city_url=query_url+city\n",
    "    city_weather = requests.get(city_url).json()\n",
    "    \n",
    "    try:\n",
    "        print('----')\n",
    "        print(count)\n",
    "        print(city)\n",
    "\n",
    "        city_lat = city_weather[\"coord\"][\"lat\"]\n",
    "        city_lng = city_weather[\"coord\"][\"lon\"]\n",
    "        city_temp = city_weather[\"main\"][\"temp\"]\n",
    "        city_humidity = city_weather[\"main\"][\"humidity\"]\n",
    "        city_clouds = city_weather[\"clouds\"][\"all\"]\n",
    "        city_wind = city_weather[\"wind\"][\"speed\"]\n",
    "        \n",
    "        city_weather = {\"Lat\"       : city_lat,\n",
    "                        \"Lng\"       : city_lng,\n",
    "                        \"Temp\"  : city_temp,\n",
    "                        \"Humidity\"  : city_humidity,\n",
    "                        \"Cloudiness\": city_clouds,\n",
    "                        \"Wind Speed\": city_wind}\n",
    "        \n",
    "        citiesWeather.append(city_weather)\n",
    "        \n",
    "    # If an error is experienced, skip the city\n",
    "    except:\n",
    "        print('-----')\n",
    "        print(\"Skipping... City Not found...\")\n",
    "        pass\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Check dict values**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "citiesWeather[1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Create Dataframe**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "weather_df=pd.DataFrame(citiesWeather)\n",
    "weather_df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Save output to csv**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "weather_df.to_csv(\"WeatherPy Data Retrival\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Show max/min values for each column for graph parameters**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "max_vals=weather_df.max(axis=0)\n",
    "min_vals=weather_df.min(axis=0)\n",
    "\n",
    "print(\"Minimum Values\")\n",
    "print(min_vals)\n",
    "print(\"-----\")\n",
    "print(\"Maximum Values\")\n",
    "print(max_vals)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Temperature (F) vs. Latitude**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Build a scatter plot for each data type\n",
    "plt.scatter(weather_df[\"Lat\"], weather_df[\"Temp\"], c=\"red\", marker=\"o\")\n",
    "\n",
    "# Incorporate the other graph properties\n",
    "plt.title(\"Temperature in World Cities\")\n",
    "plt.ylabel(\"Temperature (F)\")\n",
    "plt.xlabel(\"Latitude\")\n",
    "plt.grid(True)\n",
    "\n",
    "plt.ylim(25,100)\n",
    "plt.xlim(-60, 85)\n",
    "\n",
    "# Save the figure\n",
    "plt.savefig(\"TemperatureInWorldCities.png\")\n",
    "\n",
    "# Show plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Humidity (%) vs. Latitude**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Build a scatter plot for each data type\n",
    "plt.scatter(weather_df[\"Lat\"], weather_df[\"Humidity\"], c=\"orange\", marker=\"o\")\n",
    "\n",
    "# Incorporate the other graph properties\n",
    "plt.title(\"Humidity in World Cities\")\n",
    "plt.ylabel(\"Humidity (%)\")\n",
    "plt.xlabel(\"Latitude\")\n",
    "plt.grid(True)\n",
    "\n",
    "plt.ylim(0,120)\n",
    "plt.xlim(-60, 85)\n",
    "\n",
    "# Save the figure\n",
    "plt.savefig(\"HumidityInWorldCities.png\")\n",
    "\n",
    "# Show plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Cloudiness (%) vs. Latitude**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Build a scatter plot for each data type\n",
    "plt.scatter(weather_df[\"Lat\"], weather_df[\"Cloudiness\"], c=\"blue\", marker=\"o\")\n",
    "\n",
    "# Incorporate the other graph properties\n",
    "plt.title(\"Cloudiness in World Cities\")\n",
    "plt.ylabel(\"Cloudiness (%)\")\n",
    "plt.xlabel(\"Latitude\")\n",
    "plt.grid(True)\n",
    "\n",
    "plt.ylim(-10,110)\n",
    "plt.xlim(-60, 85)\n",
    "\n",
    "# Save the figure\n",
    "plt.savefig(\"CloudinessInWorldCities.png\")\n",
    "\n",
    "# Show plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Wind Speed (mph) vs. Latitude**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Build a scatter plot for each data type\n",
    "plt.scatter(weather_df[\"Lat\"], weather_df[\"Wind Speed\"], c=\"green\", marker=\"o\")\n",
    "\n",
    "# Incorporate the other graph properties\n",
    "plt.title(\"Wind Speed in World Cities\")\n",
    "plt.ylabel(\"Wind Speed (mph)\")\n",
    "plt.xlabel(\"Latitude\")\n",
    "plt.grid(True)\n",
    "\n",
    "plt.ylim(-1,35)\n",
    "plt.xlim(-60, 85)\n",
    "\n",
    "# Save the figure\n",
    "plt.savefig(\"WindSpeedInWorldCities.png\")\n",
    "\n",
    "# Show plot\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
