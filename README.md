# Bitcoin Price Tracker 🪙

A simple Python script that fetches the current Bitcoin price from the CoinGecko API and saves it to a CSV file with a timestamp.

## What it does

- Fetches the live Bitcoin price in USD
- Saves the price and current date/time to a CSV file
- Adds a new row every time you run it — never overwrites old data
- Handles errors gracefully (e.g. no internet connection)

## Project Structure

```
bitcoin_tracker/
├── fetch_price.py        # main script
└── bitcoin_prices.csv    # created automatically on first run
```

## Requirements

- Python 3.x
- `requests` library

Install the required library:
```bash
pip install requests
```

## How to Run

```bash
python fetch_price.py
```

## Example Output

**In the terminal:**
```
File already exists, adding new row...
Bitcoin price fetched: $68432
Saved successfully!
Time: 2024-03-15 14:30:00
Price: $68432
```

**In `bitcoin_prices.csv`:**
```
Timestamp,Bitcoin Price (USD)
2024-03-15 14:30:00,68432
2024-03-15 14:35:00,68501
2024-03-15 14:40:00,68289
```

## API Used

[CoinGecko API](https://www.coingecko.com/en/api) — free, no API key required.

---

*This is my first Python project — a beginner-friendly Bitcoin price tracker.*
