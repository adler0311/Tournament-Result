#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

"""Connect to the PostgreSQL database.  Returns a database connection."""
def connect(database_name="tournament"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor=db.cursor()
        return db, cursor
    except:
        print("<error message>")


def deleteMatches():
    """Remove all the match records from the database."""

    """First using connect function to connect to the tournament database, 
        and make cursor, and query the command and commint, 
        and finally close what I connected before. The command stands for 
        delete all data from the matches table """

    DB, c = connect()
    query1 = "DELETE from matches;"
    c.execute(query1)
    DB.commit()
    DB.close()

def deletePlayers():
    """Remove all the player records from the database."""

    """First using connect function to connect to the tournament database, 
        and make cursor, and query the command and commint, and finally
        close what I connected before. The command stands for delete all
        data from the players table """


    DB, c = connect()
    query1 = "DELETE from players;"
    c.execute(query1)
    DB.commit()
    DB.close()

def countPlayers():
    """Returns the number of players currently registered."""

    """ query that display table which is the number of players currently registered.
        and extract the value of number of players in the table and return the value """

    DB, c = connect()
    #query1 = "select id from players order by id desc limit 1;"
    query1 = "SELECT count(*) as count from players;"
    c.execute(query1)
    return int(c.fetchone()[0])


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """

    DB, c = connect()
    query = "INSERT INTO players (name) VALUES (%s);"
    parameter=(name, )
    c.execute(query, parameter)
    DB.commit()
    DB.close()


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

    """ first, make the querry of current_standing view, 
    which I made this view and explained in the tournament.sql.
        and than fetchall data and return the list of tuples. """

    DB, c = connect()
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

    DB, c = connect()
    query = "INSERT INTO matches (winner, loser) VALUES (%s, %s);"
    data = (winner, loser)
    c.execute(query, data)
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

    """ using playerStandings function which is written before, 
        fetch all the list of tuples from the current_standings table. 
        and just pick first two date of the tuple and package every 
        two revised tuple, and finally return the value which means 
        the list of swisspairlist. """

    standings = playerStandings()
    players = [item[:2] for item in standings]
    index = 0
    SwissPairList = []
    while index < len(players):
        member = players[index] + players[index + 1]
        SwissPairList.append(member)
        index += 2

    return SwissPairList