import requests
from bs4 import BeautifulSoup

def search_web(query):

    url = f"https://www.bing.com/search?q={query}"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for item in soup.select("li.b_algo h2"):
        results.append(item.text)

    return results[:10]