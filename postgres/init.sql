-- postgres/init.sql

-- Создаем analysis DB и пользователя
CREATE USER analysis_user WITH PASSWORD 'analysis_pass';
CREATE DATABASE analysis;
GRANT ALL PRIVILEGES ON DATABASE analysis TO analysis_user;

-- Подключаемся к БД files (создана через POSTGRES_DB в docker-compose)
\connect files;

-- Создаем таблицу files
CREATE TABLE IF NOT EXISTS files (
    id UUID PRIMARY KEY,
    filename TEXT NOT NULL,
    location TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
