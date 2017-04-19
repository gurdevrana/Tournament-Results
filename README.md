# Tournament-Results
The project consists of three files:
<br>
1.&nbsp;tournament.py contains all the required function to implement the tournament<br>
2.&nbsp;tournament.sql creates the database tables<br>
3.&nbsp;tournament_test.py runs unit tests on tournament.py<br>
<br>
<h3> Requirements:</h3>
1.&nbsp;Python<br>
2.&nbsp PostgreSQL<br>

# how to run this project?
First create a clean database and tables by importing tournament.sql at a PostgreSQL prompt:<br>

	> psql <br>
	=> \i tournament.sql<br>
Then test the tournament by running <br>
	> python tournament_test.py


