import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def plot_today_price_movement(symbol, intraday_close_series):
    """Plot intraday close price movement for today."""
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(intraday_close_series.index, intraday_close_series.values, linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Price")
    index_tz = getattr(intraday_close_series.index, "tz", None)
    ax.xaxis.set_major_locator(mdates.HourLocator(tz=index_tz))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M", tz=index_tz))
    max_abs_price = float(intraday_close_series.abs().max())
    use_decimals = max_abs_price < 10
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y:.2f}" if use_decimals else f"{y:.0f}"))
    ax.grid(True, alpha=0.3)
    fig.autofmt_xdate()
    plt.tight_layout()
    plt.show()
