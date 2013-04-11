CREATE TABLE friends (
    user_id INTEGER NOT NULL REFERENCES auth_user(id),
    friend_id INTEGER NOT NULL REFERENCES auth_user(id),
    PRIMARY KEY (user_id1, user_id2),
);
