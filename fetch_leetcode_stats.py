import requests
from bs4 import BeautifulSoup

# Your LeetCode username
username = "Deepadharshan"

# LeetCode profile URL
url = f"https://leetcode.com/{username}/"

# Make a request to your profile page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract your stats
problems_solved = soup.find("div", class_="profile-stat solved-problems").find("span", class_="value").text.strip()
rank = soup.find("div", class_="rank").find("span", class_="title").text.strip()
rating = soup.find("div", class_="rating").find("span", class_="value").text.strip()

# Prepare stats content
stats = f"""
## 📊 LeetCode Stats
- **Total Solved Problems**: {problems_solved}
- **Rank**: {rank}
- **Rating**: {rating}
"""

# Read the current README.md
with open("README.md", "r") as file:
    readme_content = file.read()

# Replace the placeholder with the new stats
readme_content = readme_content.replace("<!-- leetcode-stats -->", stats)

# Write the updated content back to the README.md
with open("README.md", "w") as file:
    file.write(readme_content)

print("LeetCode stats updated successfully!")
