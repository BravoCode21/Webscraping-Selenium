from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.service import Service



options = webdriver.FirefoxOptions()
options.add_argument("-headless")
PATH = "C:\Program Files\Mozilla Firefox\geckodriver.exe"
driver = webdriver.Firefox(PATH, options=options)


search_string = input("What would you  like to generate an essay for ?\n ")

formated_search_s = search_string.replace(" ", "_")

driver.get('https://www.wikipedia.org/wiki/{formated_search_s}')

#output file

output = open(fr"{formated_search_s}_essay.txt", "w+")

if "Wikipedia does not have an article with this exact name." in driver.page_source:
    print("Sorry we couldn't find wikipedia page for your search: ")
else:
#webscrap from wikipedia  accessing body

    body = driver.find_element_by_id("bodycontent")
    p_tags = body.find_elements_by_tag_name("p")

#output the file
for p_tag in p_tags:
    output.write(f"t\{p_tag}\n")
    print(f"search completed. Essay generated in {formated_search_s}_essay.txt:")

output.close()
