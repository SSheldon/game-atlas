CREATE TABLE friend (
    user_id INTEGER NOT NULL REFERENCES auth_user(id),
    friend_id INTEGER NOT NULL REFERENCES auth_user(id),
    type_id INTEGER, 
    PRIMARY KEY (user_id, friend_id)
);
