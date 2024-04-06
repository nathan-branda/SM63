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

#Takes first row of the table and removes all the blank fields and the rank field(not used)
def all_valid_fields(available_fields: list[str]) -> list[str]:
    valid_fields = []
    for field in available_fields:
        if(field != '' and field != '#'):
            valid_fields.append(field)
    return valid_fields

#Allows user input for desired values, returns a string list of choices and a list of indeces
def wanted_fields(possible_fields: list[str]) -> tuple[list[str], list[int]]:
    desired_indeces = []
    desired_fields = []
    index=0

    #possible_fields used to maintain the index properly for the table columns
    for field in possible_fields:
        while(True):
            if(field == '' or field == "#"):
                index+=1
                break
            decision=input("Would you like "+field+" tracked(Y/N): ")
            if(decision=="Y"):
                desired_indeces.append(index)
                desired_fields.append(field)
                print(field+" field added")
                index+=1
                break
            elif(decision=="N"):
                index+=1
                break
            else:
                print('Invalid input')
    return desired_fields, desired_indeces

#Takes an input of a table from BeautifulSoup and returns the raw data from that table and all fields of columns
def get_raw_data(table: list[str]) -> tuple[list[list[str]], list[str]]:
    raw_data = []
    column_data = table.find_all('tr')
    fields=[data.text.strip() for data in column_data[0]]

    for row in column_data[2:]:
        row_data = row.find_all('td')
        individual_row_data = [data.text.strip() for data in row_data]
        raw_data.append(individual_row_data)
    return raw_data, fields

def get_table(url = input_url()):
    soup = html_parse(url)
    table = soup.find_all('table')[0] #first table is always the leaderboard table
    return table

def main():
    table=get_table()
    raw_data, possible_fields = get_raw_data(table)
    users_fields, field_indeces = wanted_fields(possible_fields)

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
    
