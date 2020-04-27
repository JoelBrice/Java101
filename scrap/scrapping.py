import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time


URL = "https://www.indeed.com/jobs?q=data+scientist+%2420%2C000&l=New+York&start=10" #conducting a request of the stated URL above:
page = requests.get(URL)#specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
soup = BeautifulSoup(page.text, "html.parser")#printing soup in a more structured tree format that makes for easier reading
print(soup.prettify())

def extract_job_title_from_result(soup): 
    jobs = []
    for div in soup.find_all(name="div", attrs={"class":"row"}):
        for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
            jobs.append(a["title"])

return (jobs)extract_job_title_from_result(soup)


def extract_location_from_result(soup):
    locations = []
    spans = soup.findAll('span', attrs={'class': 'location'})
    for span in spans:
        locations.append(span.text)
  
return(locations)extract_location_from_result(soup)


def extract_company_from_result(soup): 
  companies = []
  for div in soup.find_all(name="div", attrs={"class":"row"}):
    company = div.find_all(name="span", attrs={"class":"company"})
    if len(company) > 0:
      for b in company:
        companies.append(b.text.strip())
    else:
      sec_try = div.find_all(name="span", attrs={"class":"result-link-source"})
        for span in sec_try:
          companies.append(span.text.strip())
 return(companies)
 
extract_company_from_result(soup)


def extract_salary_from_result(soup): 
  salaries = []
  for div in soup.find_all(name="div", attrs={"class":"row"}):
    try:
      salaries.append(div.find(‘nobr’).text)
    except:
      try:
        div_two = div.find(name="div", attrs={"class":"sjcl"})
        div_three = div_two.find("div")
        salaries.append(div_three.text.strip())
      except:
        salaries.append("Nothing_found")
  return(salaries)extract_salary_from_result(soup)

max_results_per_city = 100city_set = ['New+York','Chicago','San+Francisco', 'Austin', 'Seattle', 'Los+Angeles', 'Philadelphia', 'Atlanta', 'Dallas', 'Pittsburgh', 'Portland', 'Phoenix', 'Denver', 'Houston', 'Miami', 'Washington+DC', 'Boulder']
columns = ["city", "job_title", "company_name", "location", "summary", "salary"]sample_df = pd.DataFrame(columns = columns)