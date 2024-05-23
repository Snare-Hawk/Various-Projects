from bs4 import BeautifulSoup as bs
import requests
import json

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = bs(page.content, "html.parser")

jobTitle = soup.find_all("h2", class_="is-5")
company = soup.find_all("h3", class_="company")
location = soup.find_all("p", class_="location")
date = soup.find_all("time")

masterList = []

for x, y, a, b in zip(jobTitle, company, location, date):
    info = {
        "name": str(x.text.strip()),
        "employer": str(y.text.strip()),
        "location": str(a.text.strip()),
        "datePosted": str(b.text.strip())
    }
    masterList.append(info)

# Serializing json
json_object = json.dumps(masterList, indent=4)

with open("jobs.json", "w+") as outfile:
	outfile.write(json_object)
