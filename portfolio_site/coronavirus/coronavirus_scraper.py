# Scraper imports
import requests
from datetime import date
from bs4 import BeautifulSoup
from time import sleep

# Reader imports
from csv import reader
import numpy as np
import re


class COVID19_Scraper:
    def __init__(self):
        self.date = date.today()

    def get_dayton_stats(self):
        # Dayton information is taken from two separate pages on the New York Times site, so this function finds
        # the case number for each county and strips unnecessary information from each
        def nytimes_scraper(url):
            ohio_response = requests.get(url)
            ohio_soup = BeautifulSoup(ohio_response.text, "html.parser")
            return int(ohio_soup.find(id="cases").find_all("strong")[1].get_text().replace(" cases per day", ""))

        new_greene_cases = nytimes_scraper("https://www.nytimes.com/interactive/2021/us/greene-ohio-covid-cases.html")
        sleep(1)
        new_montgomery_cases = nytimes_scraper("https://www.nytimes.com/interactive/2021/us/montgomery-ohio-covid-cases.html")

        dayton_total = new_greene_cases + new_montgomery_cases

        # If the totals have not yet been updated, this will return the string "NULL"
        if dayton_total == 0:
            return "NULL"
        return dayton_total

    def get_tokyo_stats(self):
        url = "https://stopcovid19.metro.tokyo.lg.jp/en"
        tokyo_response = requests.get(url)
        tokyo_soup = BeautifulSoup(tokyo_response.text, "html.parser")

        tokyo_total = int(tokyo_soup.find(class_="InfectionMedicalcareprovisionStatus-description").span.get_text().replace("人", ""))

        if tokyo_total == 0:
            return "NULL"
        return tokyo_total

    def package_data(self, dayton_total, tokyo_total):
        return {"Date": self.date, "Dayton": dayton_total, "Tokyo": tokyo_total}


class COVID19_Reader:
    def __init__(self):
        pass

    def data_reader(self):
        with open("coronavirus_data.csv") as file:
            csv_reader = reader(file)
            return list(csv_reader)

    def print_cases(self, data):
        todays_data = data[len(data) - 1]  # data[len(data)-2]
        # The above commented out code allows you to see yesterday's data instead.

        # Below is a regex which will match the day, month, and year that the data was collected.
        date_analysis = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d\d?)")
        match = date_analysis.search(todays_data[0])
        MONTHS = {
            "01": "January",
            "02": "February",
            "03": "March",
            "04": "April",
            "05": "May",
            "06": "June",
            "07": "July",
            "08": "August",
            "09": "September",
            "10": "October",
            "11": "November",
            "12": "December"
        }

        # Below converts the regex groups into variables so that they can be included in the final f-string.
        month = MONTHS[match.group("month")]
        day = match.group("day")
        year = match.group("year")

        tokyo_new_cases = todays_data[2]
        dayton_new_cases = todays_data[1]
        print(f"The number of new cases in Tokyo on {month} {day}, {year} was {tokyo_new_cases}.")
        print(f"The number of new cases in Dayton was {dayton_new_cases}.")


if __name__ == "__main__":
    scraper = COVID19_Scraper()
    cvd_reader = COVID19_Reader()

    todays_values = scraper.package_data(scraper.get_dayton_stats(), scraper.get_tokyo_stats())
    print(todays_values)
    print(todays_values["Dayton"])
    print(todays_values["Tokyo"])

    data = cvd_reader.data_reader()
    cvd_reader.print_cases(data)
