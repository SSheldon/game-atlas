CREATE TABLE genre (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

INSERT INTO genre (name) VALUES
('Shooter'),
('Survival Horror'),
('Role-playing');
