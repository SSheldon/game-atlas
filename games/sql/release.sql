CREATE TABLE release (
    game_id INTEGER REFERENCES game(id),
    platform_id INTEGER REFERENCES platform(id),
    release_date DATE,
    PRIMARY KEY(game_id, platform_id)
);
