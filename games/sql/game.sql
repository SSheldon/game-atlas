CREATE TABLE game (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    genre_id INTEGER NOT NULL REFERENCES genre(id)
);

INSERT INTO game (title, genre_id) VALUES
('Halo: Combat Evolved', 1),
('Borderlands', 1),
('Dead Space', 2),
('Mass Effect', 3);
