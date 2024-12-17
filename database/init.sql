-- Создание таблицы для полисов
CREATE TABLE IF NOT EXISTS policies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    policy_type VARCHAR(255) NOT NULL
);
