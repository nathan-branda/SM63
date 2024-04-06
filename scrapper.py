import requests
from bs4 import BeautifulSoup
import re

#User input of speedrun.com url
def input_url() -> str:
    while(True):
        url = input("speedrun.com URL(click on the category that you want): ")
        if(re.search("speedrun.com",url)):
            return url
        else:
            print("Not a speedrun.com URL")

#Parse the html
def html_parse(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

#Allows user input for desired values, returns a string set of choices
def wanted_fields() -> list[str]:
    possible_values=['Player', 'Time', 'Date', 'Timing']#Last field is different by game and there may be more fields 
    desired_values=list()
    for field in possible_values:
        while(True):
            decision=input("Would you like "+field+" tracked(Y/N): ")
            if(decision=="Y"):
                desired_values.append(field)
                print(field+" field added")
                break
            elif(decision=="N"):
                break
            else:
                print('Invalid input')
    return desired_values

#Takes a list of strings and converts it into the indeces of the fields in the table's rows
def wanted_indeces(fields) -> list[int]:
    indeces=list()
    if("Player" in fields):
        indeces.append(1)
    if("Time" in fields):
        indeces.append(3)
    if("Date" in fields):
        indeces.append(4)
    if("Timing" in fields):
        indeces.append(5)
    return indeces

#Takes an input of a table from BeautifulSoup and returns the raw data from that table
def get_raw_data(table):
    raw_data = []
    column_data = table.find_all('tr')
    for row in column_data[2:]:
        row_data = row.find_all('td')
        individual_row_data = [data.text.strip() for data in row_data]
        raw_data.append(individual_row_data)


def main():
    url = input_url()
    soup = html_parse(url)
    table = soup.find_all('table')[0] #first table is always the leaderboard table
    data_table = []
    data_table.append(wanted_fields())
    field_indeces=wanted_indeces(data_table[0])
    raw_data = []
    for row in raw_data:
        data_row = []
        for index in field_indeces:
            data_row.append(row[index])
        data_table.append(data_row)
    print(data_table)

if __name__=="__main__":
    main()
    
