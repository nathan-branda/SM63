import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Step 1: Identify the URL
url = 'https://www.speedrun.com/sm63?h=Any-Normal&x=7kj99423-68kojzn2.5leo4mqo'

# Step 2: Send HTTP request and parse HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract data
# (Assuming player names and run times are in specific HTML elements)
player_names = []
run_times = []

table = soup.find('table', {'class': 'leaderboard-table'})
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
