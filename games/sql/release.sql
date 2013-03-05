CREATE TABLE release (
    game_id INTEGER REFERENCES game(id),
    platform_id INTEGER REFERENCES platform(id),
    PRIMARY KEY(game_id, platform_id)
);
