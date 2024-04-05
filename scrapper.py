import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


url = 'https://www.speedrun.com/sm63?h=Any-Normal&x=7kj99423-68kojzn2.5leo4mqo'

#Parse the html
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#Extract desired data
player_names = []
run_times = []

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
    
