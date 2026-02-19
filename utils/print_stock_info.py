from datetime import datetime


def print_stock_info(stock_data):
    """Print stock information in a clean, readable format."""
    title = f"{stock_data['company_name']} ({stock_data['symbol']})"
    print("=" * len(title))
    print(title.upper())
    print("=" * len(title))

    print(f"Current Price: {stock_data['current_price']}")
    print(f"Open: {stock_data['open']} | High: {stock_data['high']} | Low: {stock_data['low']}")
    print(f"Market Cap: {stock_data['market_cap']}")
    print(f"P/E Ratio: {stock_data['pe_ratio']}")
    print(f"52 Week High: {stock_data['52_week_high']} | 52 Week Low: {stock_data['52_week_low']}")
    print(f"Dividend: {stock_data['dividend']}")
    print(f"Dividend Yield %: {stock_data['dividend_yield_pct']}")
    print(f"Qtrly Div Amt: {stock_data['qtrly_div_amt']}")

    now = datetime.now()
    print("\n\nData collected on:", now.strftime("%Y-%m-%d %H:%M:%S"))
