import json
import requests
from bs4 import BeautifulSoup as bs

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = bs(page.content, "html.parser")

# gets all the info from the base page
jobTitle = soup.find_all("h2", class_="is-5")
company = soup.find_all("h3", class_="company")
location = soup.find_all("p", class_="location")
date = soup.find_all("time")

# gets all links on page
listOfLinks = soup.find_all("a", class_="card-footer-item", attrs={"href"})

# initialize array to be used for storing application links
applyLinksList = []

# since we only want to go to the link the "Apply" link takes us, we filter out and only take those and store them
for i in listOfLinks:
    if i.text == "Apply":
        applyLinksList.append(i)

# initialize array to be used for storing descriptions from application links
descList = []

# grab description from each link
for i in applyLinksList:
    newURL = i['href']
    newPage = requests.get(newURL)

    soup = bs(newPage.content, "html.parser")

    divBlock = soup.find("div", class_="content")
    actualDesc = divBlock.find("p", attrs={"class": None})

    descList.append(actualDesc)

# put everything into an array of dictionaries
masterList = []
for title, desc, employer, location, date  in zip(jobTitle, descList, company, location, date):
    info = {
        "name": str(title.text.strip()),
        "description": str(desc.text.strip()),
        "employer": str(employer.text.strip()),
        "location": str(location.text.strip()),
        "datePosted": str(date.text.strip())
    }
    masterList.append(info)

# write it to a json file
json_object = json.dumps(masterList, indent=4)

with open("jobs.json", "w+") as outfile:
	outfile.write(json_object)
