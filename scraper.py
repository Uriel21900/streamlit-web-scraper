import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

def scrape_yahoo_active():
    """
    Scrapes the 'Most Active' stocks page from Yahoo Finance
    and returns a pandas DataFrame.
    """
    url = "https://finance.yahoo.com/most-active"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from Yahoo Finance. Status code: {response.status_code}")
        
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    
    if not table:
        raise Exception("Could not find the data table on the page.")
        
    # Read HTML table using pandas
    # We use StringIO to avoid FutureWarnings with passing literal HTML
    html_io = StringIO(str(table))
    df = pd.read_html(html_io)[0]
    
    # Basic data cleaning
    # Rename columns to ensure consistency in case Yahoo Finance changes them slightly
    # Typically: Symbol, Name, Price (Intraday), Change, % Change, Volume, Avg Vol (3 month), Market Cap, PE Ratio (TTM)
    
    # We will just return the raw DataFrame and let the app handle the specific columns
    # it wants to display, but let's ensure we return it cleanly.
    return df
