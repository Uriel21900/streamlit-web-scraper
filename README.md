# Web Scraper Dashboard

A Streamlit application that scrapes live stock market data from Yahoo Finance's "Most Active" stocks page and visualizes it using interactive charts.

## Features
- **Live Web Scraping**: Fetches the latest data directly from the web using `requests` and `BeautifulSoup`.
- **Data Visualization**: Uses `plotly` to render interactive charts for Volume and Price vs % Change.
- **Data Cleaning**: Automatically handles string-to-numeric conversions for financial data.
- **Streamlit Ready**: Fully responsive web interface.

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd streamlit-web-scraper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Technologies
- Python
- Streamlit
- Pandas
- BeautifulSoup4
- Plotly
