<html>

<head>
    <link type="text/css" href="style.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Baloo+Thambi|Indie+Flower" rel="stylesheet">
    <title>Horoscope Generator</title>
</head>

<body>
<h1>Horoscope Generator</h1>
<h2>What's in your future?</h2>

<br><br>
<form action="index.php" method="POST">
    <fieldset>
        <legend>When were you born?</legend>
        Month:
            <select name="month">
                <option value="January">January</option>
                <option value="February">February</option>
                <option value="March">March</option>
                <option value="April">April</option>
                <option value="May">May</option>
                <option value="June">June</option>
                <option value="July">July</option>
                <option value="August">August</option>
                <option value="September">September</option>
                <option value="October">October</option>
                <option value="November">November</option>
                <option value="December">December</option>
            </select>
            <br>
        Day:
            <input type="number" min="1" max="31" value="1" name="day" id="day">
            <br>
        Year:
            <input type="number" min="1900" max="2017" value="1999" name="year" id="year">
            <br>
        <input type="submit" value="Swami!">
    </fieldset>
</form>
<?php
$servername = "localhost";
$username = "horoscope";
$password = "YQ17Fip9Er1egqE2UfuD";
$dbname = "horoscopes";

if (isset($_POST['month']) && isset($_POST['day']) && isset($_POST['year'])) {

$month = $_POST['month'];
$day = $_POST['day'];
$year = $_POST['year'];

if (((strpos($month, 'January') !== false) ||
	(strpos($month, 'February') !== false) ||
	(strpos($month, 'March') !== false) ||
	(strpos($month, 'April') !== false) ||
	(strpos($month, 'May') !== false) ||
	(strpos($month, 'June') !== false) ||
	(strpos($month, 'July') !== false) ||
	(strpos($month, 'August') !== false) ||
	(strpos($month, 'September') !== false) ||
	(strpos($month, 'October') !== false) ||
	(strpos($month, 'November') !== false) ||
	(strpos($month, 'December') !== false))
	&& is_numeric($day) && is_numeric($year)){
$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
	return;
}

$sql = 'SELECT fortune FROM horoscopes WHERE month = "' . $month . '";';
$result = $conn->query($sql);

if ($result->num_rows > 0) {
	$row = $result->fetch_assoc();
	echo "<center>" . $row["fortune"] . "</center>";
}

$conn->close();
}
else {
	echo "<center><b>Hey!! No funny business!!</b></center>";
}
}
?>
</body>
</html>