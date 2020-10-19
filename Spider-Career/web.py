import requests
from jinja2 import Environment, FileSystemLoader
import pdfkit
import os
from scrapy.selector import Selector
import PyPDF2


def generate_html(key,body):
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('template.html')
    with open("html/"+key.split(":")[0]+".html",'w+') as fout:
        html_content = template.render(key=key,body=body)
        fout.write(html_content)

root="https://au.indeed.com"
url="https://au.indeed.com/Software-jobs"

strhtml=requests.get(url)
selector = Selector(text=strhtml.text)

links={}
for i in range(15):
    datah = selector.xpath('//*[@id="sja{}"]//@href'.format(i))
    datat = selector.xpath('//*[@id="sja{}"]//@title'.format(i))
    links[datat.get("data").replace(" ","_")]=root+datah.get("data")
print(links)
try:
    for key in links.keys():
        url=links[key]
        strhtml=requests.get(url)
        selector = Selector(text=strhtml.text)
        datah = selector.xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div[1]')
        generate_html(key,datah.get("data"))
except Exception as e:
    print(e)
finally:
    for file in os.listdir("html"):
        if(file!=".DS_Store"):
            pdfkit.from_file("html/"+file,"html-pdf/"+file.split(".")[0]+".pdf")
    original="html-pdf/"
    new="done-pdf/"
    for file in os.listdir("html-pdf"):
        if(file!=".DS_Store"):
            original_pdf = PyPDF2.PdfFileReader(original+file) 
            page = original_pdf.getPage(0) 
            pdfWriter = PyPDF2.PdfFileWriter()
            pdfWriter.addPage(page)

            with open(new+file, 'wb') as f:
                pdfWriter.write(f)















