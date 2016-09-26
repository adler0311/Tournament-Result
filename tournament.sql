-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE players (
		id SERIAL primary key,
		name TEXT
		);

CREATE TABLE matches (
		id SERIAL primary key,
		winner INTEGER REFERENCES players (id),
		looser INTEGER REFERENCES players (id)
		);

CREATE VIEW current_standing as select players.id, players.name, sum(case when players.id = matches.winner then 1 else 0 end)
	as wins, count(matches) as matches from players left outer join matches on players.id = matches.winner or
	players.id = matches.loser group by players.id order by wins desc, matches;
