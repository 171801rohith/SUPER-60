import urllib.request

url = "https://www.geeksforgeeks.org/python/python-programming-language-tutorial/"

try:
    response = urllib.request.urlopen(url)
    data = response.read()

    html_content = data.decode("utf-8")

    print(html_content)
except Exception as e:
    print(e)
