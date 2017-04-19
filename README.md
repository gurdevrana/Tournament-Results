# Tournament-Results
The project consists of three files:
<br>
1.tournament.py contains all the required function to implement the tournament<br>
2.tournament.sql creates the database tables<br>
3.tournament_test.py runs unit tests on tournament.py<br>
<br>
# how to run this project?

Python and PostgreSQL are required. Before a tournament, create a clean database and tables by importing tournament.sql at a PostgreSQL prompt:
<br>
	> psql <br>
	=> \i tournament.sql<br>
Then test the tournament by running <br>
	> python tournament_test.py


