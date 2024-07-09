import requests
from bs4 import BeautifulSoup

def get_rent_prices(city):
    url = f'https://{city}.craigslist.org/search/apa'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad response status
        soup = BeautifulSoup(response.content, 'html.parser')
        listings = soup.find_all('li', class_='result-row')

        rent_prices = []
        for listing in listings:
            price = listing.find('span', class_='result-price')
            if price:
                rent_prices.append(price.text.strip())

        return rent_prices

    except requests.exceptions.RequestException as e:
        print(f"Error fetching Craigslist data for {city}: {e}")
        return []

if __name__ == "__main__":
    city = 'newyork'
    prices = get_rent_prices(city)
    print(f"Rent prices in {city}:")
    print(prices)
