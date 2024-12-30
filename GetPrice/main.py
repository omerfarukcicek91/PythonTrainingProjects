
import requests
from bs4 import BeautifulSoup


def get_price(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        price_tag = soup.find('span', {'itemprop': 'price'})

        # Check if the price element was found
        if price_tag and 'content' in price_tag.attrs:
            return price_tag['content']
        else:
            print("Price not found on the page.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error while making request: {e}")
        return None


print(get_price('https://www.scan.co.uk/products/ttartisan-100mm-f28-macro-x2-canon-ef-mount-24-viewing-angle-telephoto-prime-lens'))