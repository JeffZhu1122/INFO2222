import requests
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader
import lxml
import pdfkit
import os


def generate_html(key,overview,handbook):
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('template.html')
    with open("html/"+key.split(":")[0]+".html",'w+') as fout:
        html_content = template.render(key=key,overview=overview,handbook=handbook)
        fout.write(html_content)

root="https://cusp.sydney.edu.au"
url="https://cusp.sydney.edu.au/students/view-degree-page/degree_id/753"

strhtml=requests.get(url)
soup=BeautifulSoup(strhtml.text,'lxml')
data = soup.select('#semesters > table > tr > td:nth-child(3) > a')

links={}
for i in data:
    if "Electives" not in str(i):
        links[str(i)[50:-4]]=root+str(i)[9:48]

overview={}
handbook={}
for key in links.keys():
    #overview

    url=links[key]
    strhtml=requests.get(url)
    soup=BeautifulSoup(strhtml.text,'lxml')
    data = soup.select('#overview > table > tr> td')
    singleview={}
    for i in range (len(data)-2):
        if "lh" in str(data[i]):
            singleview[str(data[i])[15:-6].strip()]=str(data[i+1])[4:-5].strip()
    overview[key]=singleview

    #overview
    data = soup.select('#handbook > table > tr > td')
    singlebook = {}
    for i in range (len(data)):
        if "lh" in str(data[i]):
            if "Prohibitions" in str(data[i]):
                singlebook[str(data[i])[15:-6].strip()]=str(data[i+1])[4:-5].strip().replace("students/view-unit-page/alpha", "units")  
            else:
                singlebook[str(data[i])[15:-6].strip()]=str(data[i+1])[4:-5].strip()
    handbook[key]=singlebook


for key in overview:
    print(overview[key])
    print(handbook[key])
    generate_html(key,overview[key],handbook[key])

for file in os.listdir("html"):
    pdfkit.from_file("html/"+file,"html-pdf/"+file.split(".")[0]+".pdf")

