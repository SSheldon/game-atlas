CREATE TABLE game (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    genre_id INTEGER NOT NULL REFERENCES genre(id)
);
