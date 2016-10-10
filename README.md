# Tournament-Result
  This application is designed to operate swiss-paring tournament.
  There are four files including this README.md file.
  In tournament.py file, all the function to operate functions to create, 
    update, and delete database.
  There are tables and view is refered to the swiss-paring tournament in 
    tournament.sql file.
  When tournament_test.py is executed, every operation described below
    will be oprated. 

## execute the application##
  1. open the git bash.
  2. go to the vagrant folder and "vagrant up".
  3. next, "vagrant ssh". type "vagrant provision" if need before type
     "vagrant ssh".
  4. when the vagrant machine turn on, and all set,
      execute "python tournament_test.py"



##I. TestCount
  1. countPlayers() returns 0 after initial deletePlayers() execution.
  2. countPlayers() returns 1 after one player is registered.
  3. countPlayers() returns 2 after two players are registered.
  4. countPlayers() returns zero after registered players are deleted.
  5. Player records successfully deleted.
  
##II. testStandingsBeforeMatches
  6. Newly registered players appear in the standings with no matches.

##III. testReportMatches
  7. After a match, players have updated standings.
  8. After match deletion, player standings are properly reset.
  9. Matches are properly deleted.

##IV. testPairings
  10. After one match, players with one win are properly paired.
