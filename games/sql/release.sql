CREATE TABLE release (
    game_id INTEGER REFERENCES game(id) ON DELETE CASCADE,
    platform_id INTEGER REFERENCES platform(id),
    release_date DATE,
    PRIMARY KEY(game_id, platform_id)
);

INSERT INTO release (game_id, platform_id, release_date) VALUES
(1, 1, '2001-11-15'),
(1, 3, '2003-09-30'),
(2, 2, '2009-10-20'),
(2, 3, '2009-10-26'),
(3, 2, '2008-10-14'),
(3, 3, '2008-10-20'),
(4, 2, '2007-11-20'),
(4, 3, '2008-05-28');
