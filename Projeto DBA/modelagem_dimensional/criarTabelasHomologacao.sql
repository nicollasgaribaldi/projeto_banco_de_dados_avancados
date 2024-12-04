CREATE TABLE dim_carro (
    id SERIAL PRIMARY KEY,
    car_name VARCHAR(100),
    type VARCHAR(20),
    drive VARCHAR(20)
);

CREATE TABLE dim_localizacao (
    id SERIAL PRIMARY KEY,
    location VARCHAR(10)
);

CREATE TABLE dim_combustivel (
    id SERIAL PRIMARY KEY,
    fuel VARCHAR(20)
);

CREATE TABLE fato_precos (
    id SERIAL PRIMARY KEY,
    carro_id INT REFERENCES homologacao.dim_carro(id),
    localizacao_id INT REFERENCES homologacao.dim_localizacao(id),
    combustivel_id INT REFERENCES homologacao.dim_combustivel(id),
    year INT,
    distance INT,
    owner INT,
    price DECIMAL
);
