CREATE TABLE carros (
    id SERIAL PRIMARY KEY,
    car_name VARCHAR(100),
    year INT,
    distance INT,
    owner INT,
    fuel VARCHAR(20),
    location VARCHAR(10),
    drive VARCHAR(20),
    type VARCHAR(20),
    price DECIMAL
);
