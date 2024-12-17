from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
from psycopg2 import sql

app = Flask(__name__)
CORS(app)

# Получаем переменные окружения
import os
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'policy_db')
POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres_user')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres_password')

# Подключение к базе данных PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD
    )
    return conn

@app.route('/policy/', methods=['POST'])
def create_policy():
    data = request.get_json()
    name = data.get('name')
    city = data.get('city')
    policy_type = data.get('policy_type')

    if not all([name, city, policy_type]):
        return jsonify({'error': 'All fields are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    # Добавляем новый полис в таблицу policies
    insert_query = sql.SQL("""
        INSERT INTO policies (name, city, policy_type)
        VALUES (%s, %s, %s)
        RETURNING id;
    """)
    cursor.execute(insert_query, (name, city, policy_type))
    policy_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'policy_id': policy_id, 'status': 'success'}), 201

@app.route('/policies/', methods=['GET'])
def get_all_policies():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM policies;")
    policies = cursor.fetchall()
    cursor.close()
    conn.close()

    policies_list = [
        {"id": policy[0], "name": policy[1], "city": policy[2], "policy_type": policy[3]}
        for policy in policies
    ]

    return jsonify(policies_list)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
