import json
import os
import warnings
from fastapi import FastAPI, Query
from typing import Optional
import scraper

# Ignore the NotOpenSSLWarning warning
from urllib3.exceptions import NotOpenSSLWarning
warnings.filterwarnings("ignore", category=NotOpenSSLWarning)

app = FastAPI()

def save_to_json(data, filename='db.json'):
    current_directory = os.getcwd()

    file_path = os.path.join(current_directory, filename)
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

@app.get("/scrape")
def scrape(
    limit_pages: Optional[int] = Query(None, alias="limit_pages"), 
    proxy: Optional[str] = Query(None, alias="proxy")
):
    products = scraper.scrape_catalogue(limit_pages, proxy)
    
    if products:
        save_to_json(products)
        return {"message": "Scraped data has been saved to db.json", "data": products}
    else:
        return {"message": "No data scraped."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)