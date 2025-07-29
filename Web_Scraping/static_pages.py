import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://www.geeksforgeeks.org/python/python-programming-language-tutorial/"
)

soup = BeautifulSoup(response.content, "html.parser")

div_content = soup.find("div", class_="article--viewer_content")
if div_content:
    for para in div_content.find_all('p'):
        print(para.text.strip())
else:
    print("No content")