-- Création des extensions nécessaires
CREATE EXTENSION IF NOT EXISTS timescaledb;

-- Création de la table pour les données financières
CREATE TABLE IF NOT EXISTS stock_data (
    time TIMESTAMPTZ NOT NULL,
    symbol VARCHAR(10) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    volume BIGINT NOT NULL
);

-- Conversion en table hypertable
SELECT create_hypertable('stock_data', 'time');

-- Index pour améliorer les performances
CREATE INDEX IF NOT EXISTS idx_stock_symbol ON stock_data (symbol); 