
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


last_page_number = 10

URL = 'https://vesti.kg/'

def get_page(url):
    response = requests.get(url = 'https://vesti.kg/')
    return response.text

def analyze_page_content(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    return soup



def get_product_cards(soup):
    products_list = soup.find('div', id_='gkContentWrap')
    product_cards = products_list.find_all('div', class_='nspLinkScroll1')
    return product_cards



def get_product_info(product_card):
    
    title_element = product_card.find('div', class_='itemBody').find('div', class_='itemIntroText').find('div', class_='moduleItemDateCreated').find('span')
    title = title_element.text
    details_link = title_element.get('href')

   

    info = {
        'title': title, 
      
    }

    return info





def write_to_csv(data):
    import csv
    with open('products.csv', 'w') as file:
        fieldnames = ['title']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def main():
    products = []
    for num in tqdm(range(1, last_page_number + 1), 'Проходим по страницам'):
        page_url = f'{URL}?page={num}'
        page_content = get_page(page_url)
        page_soup = analyze_page_content(page_content)
        product_cards = get_product_cards(page_soup)
        page_products = []
        for card in tqdm(product_cards, f'Проходим по карточкам страницы {num}'):
            prod = get_product_info(card)
            page_products.append(prod)
        products.extend(page_products)
    write_to_csv(products) 


main()