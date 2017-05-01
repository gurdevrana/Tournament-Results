#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
from contextlib import contextmanager

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

@contextmanager
def get_cursor():
    """Generate a cursor on the database and making the database connection
    """
    conn=psycopg2.connect(database="tournament", user="postgres", password="babaji9lm", host="localhost", port="5432")
    c = conn.cursor()

    try:
        yield c
    except:
        raise
    else:
        conn.commit()
    finally:
        c.close()
        conn.close()


def deleteMatches():
    """Remove all the match records from the database."""
    with get_cursor() as c:
        c.execute("DELETE FROM matches;")
        #c.execute("UPDATE players SET wins=0,matches=0")


def deletePlayers():
    """Remove all the player records from the database."""
    with get_cursor() as c:
        c.execute("DELETE FROM players;")


def countPlayers():
    """Returns the number of players currently registered."""
    with get_cursor() as c:
        c.execute("SELECT COUNT(*) FROM players;")
        count = c.fetchall()
    return count[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    with get_cursor() as c:
        c.execute("INSERT INTO players (name) VALUES (%s);", (name,))


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
    res = []
    with get_cursor() as c:


        c.execute("SELECT matches_by_player.id,players.name ,wins_by_player.wins,matches_by_player.totalmatches "
                  "FROM matches_by_player "
                  "INNER JOIN wins_by_player ON matches_by_player.id=wins_by_player.id  "
                  "INNER JOIN players ON players.id = matches_by_player.id "
                  "ORDER BY wins_by_player.wins ASC")
        #c.execute("SELECT players.id,players.name ,wins_by_player.wins,matches_by_player.totalmatches "
        #         "FROM players "
         #         "INNER JOIN wins_by_player ON players.id=wins_by_player.id  "
        #          "INNER JOIN matches_by_player ON wins_by_player.id= matches_by_player.id "
        #         "ORDER BY wins_by_player.wins ASC")

        results = c.fetchall()

        return [(row[0], row[1], row[2], row[3]) for row in results]

        #c.execute("SELECT * FROM players ORDER BY wins ASC ")
        #ranks = c.fetchall()
    #return [(row[0], row[1], row[2], row[3]) for row in ranks]tournament.public.matches_by_player.


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    with get_cursor() as c:
        c.execute("INSERT INTO matches (winner, loser) VALUES (%s, %s);", (winner, loser))
        #c.execute("UPDATE players SET matches = matches + 1 WHERE id = %s;", (loser,))
        #c.execute("UPDATE players SET matches = matches + 1 ,wins = wins + 1 WHERE id = %s;", (winner,))
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player  withn equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pairings = []

    standings = playerStandings()
    for i in range(0, len(standings) - 1, 2):
        pairings.append((standings[i][0], standings[i][1], standings[i + 1][0], standings[i + 1][1]))

    return pairings

