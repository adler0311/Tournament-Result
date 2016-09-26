#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    db_cursor = conn.cursor()
    query1 = "DELETE from matches;"
    db_cursor.execute(query1)
    conn.commit()
    conn.close()

def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    db_cursor = conn.cursor()
    query1 = "DELETE from players;"
    db_cursor.execute(query1)
    conn.commit()
    conn.close()

def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    db_cursor = conn.cursor()
    #query1 = "select id from players order by id desc limit 1;"
    query1 = "SELECT count(*) as count from players;"
    db_cursor.execute(query1)
    count = ({'id': str(row[0])}
                for row in db_cursor.fetchall())
    for p in count:
        return int(p['id'])


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    db_cursor = conn.cursor()
    query = "INSERT INTO players (name) VALUES ('%s');" % name
    db_cursor.execute(query)
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    query = "SELECT * from current_standing"
    c.execute(query)
    DB.commit()
    standings = c.fetchall()
    DB.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    standings = playerStandings() # ex: (98, 'Princess Celestia', '0', '0')
    players = [item[0:2] for item in standings]




    DB = connect()
    c = DB.cursor()
    query = "INSERT INTO matches (winner, loser) VALUES (%s, %s);" % (winner, loser)
    c.execute(query)
    DB.commit()
    DB.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    players = [item[:2] for item in standings]
    index = 0
    SwissPairList = []
    while index < len(players):
        member = players[index] + players[index + 1]
        SwissPairList.append(member)
        index += 2

    return SwissPairList