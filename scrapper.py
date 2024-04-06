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

#Takes first row of the table and removes all the blank fields and the rank field
def all_valid_fields(available_fields) -> list[str]:
    valid_fields = []
    for field in available_fields:
        if(field != '' and field != '#'):
            valid_fields.append(field)
    return valid_fields

#Allows user input for desired values, returns a string set of choices
def wanted_fields(possible_fields) -> list[str]:
    desired_values = []
    for field in possible_fields:
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

#Takes a list valid fields and a list of wanted fields and converts it into the indeces of the fields in the table's rows
def wanted_indeces(valid_fields, fields) -> list[int]:
    indeces=list()
    if(valid_fields[0] in fields): #hardcoded because of blank columns messing up indeces
        indeces.append(1)

    index=3
    for field in valid_fields:
        if(field in fields):
            indeces.append(index)
        index+=1
    return indeces

#Takes an input of a table from BeautifulSoup and returns the raw data from that table
def get_raw_data(table):
    raw_data = []
    column_data = table.find_all('tr')
    for row in column_data[2:]:
        row_data = row.find_all('td')
        individual_row_data = [data.text.strip() for data in row_data]
        raw_data.append(individual_row_data)
    print(raw_data)
    return raw_data

def main():
    url = input_url()
    soup = html_parse(url)
    table = soup.find_all('table')[0] #first table is always the leaderboard table

    raw_data = get_raw_data(table)
    valid_fields = all_valid_fields(raw_data[0])
    users_fields = wanted_fields(valid_fields)
    field_indeces = wanted_indeces(valid_fields, users_fields)

    data_table = []
    data_table.append(users_fields)

    for row in raw_data:
        data_row = []
        for index in field_indeces:
            data_row.append(row[index])
        data_table.append(data_row)
    print(data_table)

if __name__=="__main__":
    main()
    
