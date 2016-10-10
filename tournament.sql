-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Create players table with primary key id, and name of text type
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

CREATE TABLE players (
		id SERIAL primary key,
		name TEXT
		);

-- Create matches table with primary ky id, and winner, loser column reference to playeres id.
CREATE TABLE matches (
		id SERIAL primary key,
		winner INTEGER REFERENCES players (id),
		loser INTEGER REFERENCES players (id)
		);

-- Create view current_standing which is left outer join from players to matches which is the same id column of players
-- as winner column of matches. and especially display how many matches have ouccured, and sum of the wins and also
-- ordered by wins desc so that it is convinence later to pair player for SwissPairings.

CREATE VIEW current_standing as select players.id, players.name, sum(case when players.id = matches.winner then 1 else 0 end)
	as wins, count(matches) as matches from players left outer join matches on players.id = matches.winner or
	players.id = matches.loser group by players.id order by wins desc, matches;
