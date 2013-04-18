CREATE TABLE user_game (
    user_id INTEGER REFERENCES auth_user(id),
    game_id INTEGER REFERENCES game(id),
    PRIMARY KEY(user_id, game_id)
);
