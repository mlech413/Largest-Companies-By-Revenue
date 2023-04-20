import pandas as pd
from sqlalchemy import create_engine
from flask import Flask, render_template, jsonify
from config import user, password, host, port, db

app = Flask(__name__)

engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}")

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/v1.0/companies")
def companies():
    conn = engine.connect()
    query = "SELECT * FROM companies"
    df1 = pd.read_sql(query, conn)
    return df1.to_json(orient="records")

@app.route("/api/v1.0/names")
def names():
    conn = engine.connect()
    query = "SELECT name, symbol, industry FROM companies WHERE symbol IS NOT NULL ORDER BY name"
    nameList = pd.read_sql(query, conn)
    return nameList.to_json(orient="records")

@app.route("/api/v1.0/industries")
def industries():
    conn = engine.connect()
    query = "SELECT industry, rev_usd_mil FROM companies ORDER BY 1"
    indList = pd.read_sql(query, conn)
    return indList.to_json(orient="records")

# @app.route("/api/v1.0/industries")
# def industries():
#     conn = engine.connect()
#     query = "SELECT industry, MAX(rev_usd_mil) as rev_usd_mil, min(rank) as rank FROM companies GROUP BY industry ORDER BY rev_usd_mil DESC"
#     indList = pd.read_sql(query, conn)
#     return indList.to_json(orient="records")

@app.route("/api/v1.0/<stock>")
def stocks(stock):
    conn = engine.connect()
    query = (f"SELECT adj_close, date FROM stocks WHERE symbol = '{stock}'")
    userSelection = pd.read_sql(query, conn)
    return userSelection.to_json(orient="records")

if __name__ == "__main__":
    app.run(debug=True)