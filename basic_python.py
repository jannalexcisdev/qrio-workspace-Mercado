import requests
import json
from bs4 import BeautifulSoup

def main():
    url = 'https://www.imdb.com/chart/top'
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            " AppleWebKit/537.36 (KHTML, like Gecko)"
            " Chrome/109.0.0.0 Safari/537.36"
        )
    }
    response = requests.get(url, headers=headers)

    # save response to text
    # with open('imdb.html', 'w') as file:
    #     file.write(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')
    
    json_ld_script = soup.find("script", type="application/ld+json")
    data = json.loads(json_ld_script.string)

    items = data.get('itemListElement')

    for i, item in enumerate(items[:25]):
        item_name = item.get('item').get('name')
        print(str(i + 1) + " " + item_name)

if __name__ == "__main__":
    main()