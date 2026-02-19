# BasicStockData2 — Agent Notes

## Project Overview
This project is a modular Python + Jupyter workflow for viewing stock information and charting today's intraday price movement.

Main flow:
- Cell 1 in `main.ipynb` runs the app flow.
- Data is fetched from Yahoo Finance via `yfinance`.
- Text output and chart rendering are handled by separate function modules.

## Coding Rules
- Keep the code modular.
- Each function should be in its own file.
- Notebook cells should stay thin and primarily orchestrate imports + function calls.
- Prefer clear, descriptive file names that match the function they contain.

## Current Function File Pattern
Examples in this project:
- `utils/get_stock_info.py`
- `utils/get_today_price_movement.py`
- `utils/print_stock_info.py`
- `utils/plot_today_price_movement.py`
- `utils/format_market_cap.py`
- `utils/truncate_two_decimals.py`

## Folder Structure
```text
BasicStockData2/
├── main.ipynb
├── AGENTS.md
└── utils/
	├── __init__.py
	├── get_stock_info.py
	├── get_today_price_movement.py
	├── print_stock_info.py
	├── plot_today_price_movement.py
	├── format_market_cap.py
	└── truncate_two_decimals.py
```

## File Responsibilities
- `main.ipynb`: Thin orchestration only (imports + top-level calls).
- `utils/get_stock_info.py`: Fetches current stock fundamentals and price snapshot.
- `utils/get_today_price_movement.py`: Fetches intraday close series and applies exchange-local timezone conversion.
- `utils/print_stock_info.py`: Console/text presentation of stock summary fields.
- `utils/plot_today_price_movement.py`: Chart rendering and axis formatting rules.
- `utils/format_market_cap.py`: Market cap human-readable formatting helper.
- `utils/truncate_two_decimals.py`: Numeric truncation helper used across modules.
