import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
import time

def scrape_yahoo_data(category="most-active"):
    """
    Scrapes a specific category table from Yahoo Finance.
    Categories can be: 'most-active', 'gainers', 'losers', 'crypto'
    
    Returns a dictionary:
    {
        "success": bool,
        "data": pd.DataFrame or None,
        "error": str or None
    }
    """
    url = f"https://finance.yahoo.com/{category}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5"
    }
    
    try:
        # Adding a tiny delay can sometimes help prevent aggressive rate limiting
        time.sleep(0.5)
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 404:
            return {"success": False, "data": None, "error": "Page not found (404). The category might be invalid."}
        elif response.status_code != 200:
            return {"success": False, "data": None, "error": f"Failed to fetch data. The server returned status code: {response.status_code}"}
            
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Yahoo finance uses standard <table> tags for these lists
        table = soup.find('table')
        
        if not table:
            return {"success": False, "data": None, "error": "Could not find the data table. The website structure may have changed."}
            
        # Read HTML table using pandas
        html_io = StringIO(str(table))
        df = pd.read_html(html_io)[0]
        
        if df.empty:
            return {"success": False, "data": None, "error": "The table was found but contained no data."}
            
        return {"success": True, "data": df, "error": None}
        
    except requests.exceptions.Timeout:
        return {"success": False, "data": None, "error": "The request timed out. Yahoo Finance might be responding slowly."}
    except requests.exceptions.RequestException as e:
        return {"success": False, "data": None, "error": f"Network error occurred: {str(e)}"}
    except Exception as e:
        return {"success": False, "data": None, "error": f"An unexpected error occurred while parsing: {str(e)}"}
