import requests
from bs4 import BeautifulSoup
import csv

# Replace this URL with the URL of the weather page you want to scrape
url = "https://weather.com/weather/today/l/USNY0996:1:US"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract weather data
    location = soup.find("h1", class_="CurrentConditions--location--1Ayv3").text
    temperature = soup.find("span", class_="CurrentConditions--tempValue--3KcTQ").text
    humidity = soup.find("span", text="Humidity").find_next("span", class_="value").text
    
    # Print the extracted data
    print("Location:", location)
    print("Temperature:", temperature)
    print("Humidity:", humidity)
    
    # Save the data in a CSV file
    with open("weather_data.csv", mode='w', newline='') as csv_file:
        fieldnames = ["Location", "Temperature", "Humidity"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        # Write the header row
        writer.writeheader()
        
        # Write the data rows
        writer.writerow({"Location": location, "Temperature": temperature, "Humidity": humidity})
        
    print("Data has been saved in 'weather_data.csv'")
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)