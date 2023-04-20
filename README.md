# 100 Largest Companies by Revenue in the United States for 2022
Python Flask-powered API, HTML/CSS, JavaScript, Leaflet, Plotly
### This Jupyter notebook "exploration.ipynb" file reads, cleans, and uploads 2 files:
### 100 rows of company data from "largest_us_companies_2022.csv"</br> Source: Wikipedia - https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue
### 21586 rows of historical stock data from "stock_prices_2022.csv"</br> Source: Yahoo! Finance - https://finance.yahoo.com/lookup
### Two csv files are read into Python DataFrames. Data is cleaned by updating column names, splitting geo coordinates into seperate latitude and longitude columns, and removing commas from integer fields. After creating the new tables in PostgreSQL, SQLAlchemy is used to upload the cleaned data into the two new tables.