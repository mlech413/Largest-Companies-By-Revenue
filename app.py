import pandas as pd
from sqlalchemy import create_engine
from flask import Flask, render_template, jsonify
from config import user, password, host, port, db

app = Flask(__name__)

# Credentials from the hidden config file
engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}")

# Route for rendering the initial landing page
@app.route("/")
def home():
    return render_template("index.html")

# Route for rendering the linked dashboard page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# API to retrieve a full list of company info from the companies table
@app.route("/api/v1.0/companies")
def companies():
    conn = engine.connect()
    query = "SELECT * FROM companies"
    df1 = pd.read_sql(query, conn)
    return df1.to_json(orient="records")

# API to retrieve stock names and associated symbols for populating dropdown list
@app.route("/api/v1.0/names")
def names():
    conn = engine.connect()
    query = "SELECT name, symbol FROM companies WHERE symbol IS NOT NULL ORDER BY name"
    nameList = pd.read_sql(query, conn)
    return nameList.to_json(orient="records")

# API to retrieve grouped industry and revenue data
@app.route("/api/v1.0/industries")
def industries():
    conn = engine.connect()
    query = "SELECT industry, AVG(rev_usd_mil) AS rev_usd_mil FROM companies GROUP BY industry ORDER BY 2 DESC"
    indList = pd.read_sql(query, conn)
    return indList.to_json(orient="records")
@app.route("/api/v1.0/industries")

# API to retrieve data for the stock that the user selected in the dropdown
@app.route("/api/v1.0/<stock>")
def stocks(stock):
    conn = engine.connect()
    query = (f"SELECT adj_close, date FROM stocks WHERE symbol = '{stock}'")
    userSelection = pd.read_sql(query, conn)
    return userSelection.to_json(orient="records")

if __name__ == "__main__":
    app.run(debug=True)