from flask import Flask, request, jsonify, render_template, send_file
import psycopg2
import pandas as pd

app = Flask(__name__)

# Conexão com o banco de dados
conn = psycopg2.connect("dbname=producao user=postgres password= host=localhost port=5432")

@app.route("/")
def home():
    return render_template("index.html", title="Home")

@app.route('/cars', methods=['GET', 'POST', 'PUT', 'DELETE'])
def manage_cars():
    if request.method == 'GET':
        with conn.cursor() as cur:
            cur.execute("SELECT car_name, year, distance, owner, fuel, location, drive, type, price FROM carros")
            rows = cur.fetchall()
            cars = [
                {
                    "car_name": row[0], "year": row[1], "distance": row[2],
                    "owner": row[3], "fuel": row[4], "location": row[5],
                    "drive": row[6], "type": row[7], "price": row[8]
                } for row in rows
            ]
        return render_template("cars.html", cars=cars, title="Cars")
    
    elif request.method == 'POST':
        data = request.json
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO carros (car_name, year, distance, owner, fuel, location, drive, type, price)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (data['car_name'], data['year'], data['distance'], data['owner'], data['fuel'], data['location'], data['drive'], data['type'], data['price']))
            conn.commit()
        return jsonify({"message": "Car added"}), 201

@app.route('/report', methods=['GET'])
def generate_report():
    query = request.args.get('query')
    df = pd.read_sql_query(query, conn)
    file_path = "report.xlsx"
    df.to_excel(file_path, index=False)
    return send_file(file_path, as_attachment=True)

@app.route("/insights")
def insights():
    return render_template("insights.html", title="Insights")

if __name__ == "__main__":
    app.run(debug=True)
