import requests
from bs4 import BeautifulSoup
from typing import Dict, List, Optional

def scrape_catalogue_page(url: str, proxy: Optional[str] = None, max_products: Optional[int] = None) -> List[Dict[str, str]]:
    proxies = {'http': proxy, 'https': proxy} if proxy else None
    response = requests.get(url, proxies=proxies)
    
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    products = []
    product_count = 0
    for product in soup.select('.product-inner'):
        if max_products is not None and product_count >= max_products:
            break

        name = product.select_one('.woo-loop-product__title').get_text(strip=True)
        price = product.select_one('.woocommerce-Price-amount').get_text(strip=True)
        
        image_tag = product.select_one('.mf-product-thumbnail img')
        if image_tag:
            image_url = image_tag.get('data-lazy-src', image_tag.get('src'))
        else:
            image_url = None
        
        products.append({'name': name, 'price': price, 'image_url': image_url})

        product_count += 1
    
    return products

def scrape_catalogue(limit_pages: Optional[int] = None, proxy: Optional[str] = None) -> List[dict]:
    base_url = "https://dentalstall.com/shop/"
    
    page_url = base_url.format()

    return scrape_catalogue_page(page_url, proxy, limit_pages)
