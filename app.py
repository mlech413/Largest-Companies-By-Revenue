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
    # print(df1)
    return df1.to_json(orient="records")

@app.route("/api/v1.0/names")
def names():
    conn = engine.connect()
    query = "SELECT name, symbol, industry FROM companies WHERE symbol IS NOT NULL"
    nameList = pd.read_sql(query, conn)
    # print(nameList)
    return nameList.to_json(orient="records")

@app.route("/api/v1.0/<stock>")
def stocks(stock):
    conn = engine.connect()
    query = (f"SELECT * FROM stocks WHERE symbol = '{stock}'")
    df2 = pd.read_sql(query, conn)
    # print(df1)
    return df2.to_json(orient="records")

if __name__ == "__main__":
    app.run(debug=True)