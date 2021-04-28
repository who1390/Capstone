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
	<label for="name">Name:</label>
	<input type="text" name="name" id="name" required="required">
	<label for="userName">Username:</label>
	<input type="text" name="userName" id="userName" required="required">
	<label for="email">E-mail:</label>
	<input type="email" name="email" id="email" required="required">
	<input type="submit" value="Add" name="add" id="add">
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
	$sql = 'SELECT name, username, email FROM form';
	
	$retval = mysqli_query($conn, $sql);
	
	if (! $retval) {
		die('Could not get data: ' . mysqli_error($conn));
	}
	
	
	
	echo "Create your Account!";
	
	mysqli_free_result($retval);
	mysqli_close($conn);
	?>
	
	<!if the form has been submitted, execute this if statement, until then, display the form>
	<?php
		if(isset($_POST['add'])) {
			//Connects to the database
			$dbhost = 'localhost';
			$dbuser = 'root';
			$dbpass = '';
			$dbname= 'mydb';
	
			$conn = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname);
			
			//Handles errors with connection to database
			if(! $conn){
				die('Could not connect to database: ' . 	mysqli_error($conn));
			}
			
			//Collects values from form
			$ID = 0;
			$name = $_POST['name'];
			$userName = $_POST['userName'];
			$email = $_POST['email'];
			$gold = 0;
			$level = 1;
			$Wins = '';
			//Auto increment the first value
			
			//SQL statement
			$sql = "INSERT INTO form VALUES ('$ID', '$name', '$userName', '$email');";
			
			$retval=mysqli_query($conn,$sql);
			
			//Handles errors from MySQL
			if(! $retval) {
				die('Addition of Form failed. ' . mysqli_error($conn));
			}
			else {
				echo "Added Form successfully! ";
			}
			
			
			
			
			//SQL statement 2
			$sql2 = "INSERT INTO account VALUES ('$ID', '$name', '$userName', '$email', '$Wins');";
			
			$retval2=mysqli_query($conn,$sql2);
			
			//Handles errors from MySQL
			if(! $retval2) {
				die('Addition of Account failed. ' . mysqli_error($conn));
			}
			else {
				echo "Added Account successfully";
			}
			//Closes connection
			mysqli_close($conn);
			}
		else {
			?>
			
	
	
	<?php } ?>

</main>

</div>




</body>
</html>