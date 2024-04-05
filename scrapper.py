import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import re

#User input of speedrun.com url
def input_url() -> str:
    while(True):
        url = input("speedrun.com url(click on the category that you want):")
        if(re.search("^speedrun.com")):
            return url
        else:
            print("Not a speedrun.com URL")

#Parse the html
def html_parse(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

#Allows user input for desired values
def desired_values():
    player_names = []
    run_times = []

def main():
    url=input_url()
    soup=html_parse(url)
    table = soup.find_all('table')[0]
    world_titles = table.find_all('th')
    world_table_titles=[title.text.strip() for title in world_titles]
    print(world_table_titles)
    data_table = [world_table_titles]
    column_data = table.find_all('tr')
    for row in column_data[2:]:
        row_data=row.find_all('td')
        individual_row_data = [data.text.strip() for data in row_data]
        print(individual_row_data)
        data_table.append(individual_row_data)
    print(data_table)

if __name__=="__main__":
    main()
    
