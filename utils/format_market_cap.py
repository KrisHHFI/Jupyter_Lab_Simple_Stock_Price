from utils.truncate_two_decimals import truncate_two_decimals


def format_market_cap(value):
    """Convert large numbers into human-readable format (M/B/T)."""
    try:
        value = float(value)
        if value >= 1_000_000_000_000:
            return f"{truncate_two_decimals(value / 1_000_000_000_000)}T"
        elif value >= 1_000_000_000:
            return f"{truncate_two_decimals(value / 1_000_000_000)}B"
        elif value >= 1_000_000:
            return f"{truncate_two_decimals(value / 1_000_000)}M"
        else:
            return str(value)
    except (TypeError, ValueError):
        return value
