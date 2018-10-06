# season-plot

Plot each year of trading days to find seasonality

Download historical data from Yahoo Finance and delete top line of column names and any lines containing null values

e.g. link https://finance.yahoo.com/quote/AAPL/history?period1=347173200&period2=1538798400&interval=1d&filter=history&frequency=1d

Make sure the start date is the first trading day of a year.

run python season-plot.py AAPL.csv

replacing AAPL.csv with whichever stock you chose
