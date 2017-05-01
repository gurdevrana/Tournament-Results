-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

CREATE TABLE players (
	id serial primary key,
	name text

);

-- Recording matches allows checking for rematches
CREATE TABLE matches (
  match_id serial primary key,
	winner int references players(id),
	loser int references players(id)
);

CREATE VIEW wins_by_player AS
        SELECT players.id,
        COUNT(matches.match_id) AS wins
        FROM players
        LEFT OUTER JOIN  matches
        ON players.id = matches.winner
        GROUP BY players.id;
CREATE VIEW matches_by_player AS
      SELECT players.id,
      COUNT(matches.match_id) AS totalmatches
      from players
      LEFT OUTER JOIN  matches
      on players.id=matches.winner OR players.id=matches.loser
      GROUP BY players.id;
