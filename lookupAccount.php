<!DOCTYPE html>

<link rel="stylesheet" href="siteCSS.css">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="siteCSS.css">
</head>
<body>
<div id="wrapper">
<nav>
<ul>
 <li><a href="index.php">Home</a></li>
 <li><a href="howToPlay.php">How to Play</a></li>
 <li><a href="account.php">Account</a></li>
 <li><a href="lookupAccount.php">Leaderboards</a></li>
 
 
</ul>
</nav>
<header><h1>Bubble Poppers</h1></header>
<main>

<form method="post" action="<?php $_PHP_SELF ?>">
	<input type="submit" value="Lookup" name="Lookup" id="Lookup">
	</form>



	<?php
	
	//Connects to the database
	$dbhost = 'localhost';
	$dbuser = 'root';
	$dbpass = '';
	$dbname= 'mydb';
	
	$conn = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname);
	
	if(! $conn){
		die('Could not connect to database: ' . mysqli_error($conn));
	}
	
	//Queries the database for future output
	$sql = 'SELECT UserID, Name, UserName, Wins FROM Account';
	
	//mysqli_select_db('mydb');
	
	$retval = mysqli_query($conn, $sql);
	
	if (! $retval) {
		die('Could not get data: ' . mysqli_error($conn));
	}
	
	
	
	//Creates a new table
	echo "<table>";
	
	//Creates headers for the new table
	echo "<tr>
			<th>ID</th>
			<th>Name</th>
			<th>Username</th>
			<th>Wins</th>
			</tr>";
	
	//Outputs results of the query as an HTML table		
	while($row = mysqli_fetch_array($retval, MYSQLI_NUM)) {
		echo "<tr><td>" . $row['0'] . 
				"</td><td>" . $row['1'] .
				"</td><td>" . $row['2'] .
				"</td><td>" . $row['3'] .
				"</td></tr>";
		}
		
	//Ends the table			
	echo "</table>";
	
	echo "Data retrieval complete";
	
	mysqli_free_result($retval);
	mysqli_close($conn);
	?>
	</body>
</html>
