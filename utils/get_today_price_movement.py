import yfinance as yf


def get_today_price_movement(symbol):
    """Fetch intraday close prices for the current trading day."""
    ticker = yf.Ticker(symbol)
    intraday = ticker.history(period="1d", interval="5m")
    if intraday.empty:
        raise ValueError(f"No intraday data found for stock symbol '{symbol}'")

    intraday = intraday.dropna(subset=["Close"])
    if intraday.empty:
        raise ValueError(f"No intraday close prices found for stock symbol '{symbol}'")

    exchange_timezone = None
    try:
        exchange_timezone = ticker.fast_info.get("timezone")
    except Exception:
        exchange_timezone = None

    if not exchange_timezone:
        info = ticker.info
        exchange_timezone = info.get("exchangeTimezoneName") or info.get("timeZoneFullName")

    if exchange_timezone:
        index_tz = intraday.index.tz
        if index_tz is None:
            intraday.index = intraday.index.tz_localize("UTC")
        intraday.index = intraday.index.tz_convert(exchange_timezone)

    return intraday["Close"]
