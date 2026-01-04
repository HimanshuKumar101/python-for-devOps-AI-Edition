import requests

API_KEY = "QRHE86JT0WVBQLHI"
BASE_URL = "https://www.alphavantage.co/query"


def build_api_url(symbol: str, time_series: bool = True) -> dict:
    """
    Build API parameters for Alpha Vantage request.
    """
    if time_series:
        return {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": API_KEY
        }

    return {
        "symbol": symbol,
        "apikey": API_KEY
    }


def fetch_stock_data(params: dict) -> dict:
    """
    Fetch stock data from Alpha Vantage API.
    Handles network and API errors.
    """
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print("❌ API request failed:", error)
        return {}


def display_time_series(data: dict) -> None:
    """
    Display time series data safely.
    """
    if "Time Series (Daily)" not in data:
        print("⚠️ Invalid response or symbol not found.")
        return

    time_series = data["Time Series (Daily)"]

    for date, values in list(time_series.items())[:5]:
        print(f"\nDate: {date}")
        print(f"Open: {values['1. open']}")
        print(f"High: {values['2. high']}")
        print(f"Low: {values['3. low']}")
        print(f"Close: {values['4. close']}")


def main() -> None:
    """
    Main function to run the script.
    """
    try:
        symbol = input(
            "Enter stock symbol (e.g. AMZN, GOOGL, IBM): "
        ).strip().upper()

        if not symbol:
            raise ValueError("Stock symbol cannot be empty.")

        api_params = build_api_url(symbol)
        stock_data = fetch_stock_data(api_params)

        if stock_data:
            display_time_series(stock_data)

    except ValueError as error:
        print("❌ Input Error:", error)


if __name__ == "__main__":
    main()
