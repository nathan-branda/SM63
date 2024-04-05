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

table = soup.find('table', {'class': 'w-full whitespace nowarp'})
rows = table.find_all('tr')

for row in rows[1:]:  # Skip header row
    cells = row.find_all('td')
    player_names.append(cells[1].text.strip())  # Assuming player names are in the second column
    run_times.append(cells[2].text.strip())    # Assuming run times are in the third column

# Step 4: Process the data (convert run times to numeric format, etc.)

# Step 5: Create the chart
plt.bar(player_names[:10], run_times[:10])  # Example: Creating a bar chart for the top 10 players
plt.xlabel('Player Name')
plt.ylabel('Run Time')
plt.title('Leaderboard')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()

# Step 6: Display or save the chart
plt.show()
