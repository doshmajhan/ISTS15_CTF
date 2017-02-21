<html>
<head>
<link href="css/style.css" rel="stylesheet" type="text/css" />

<script>
function hash_password(pwField) {
	hash = pwField.value.toLowerCase().split('');

	caesarian_shift(hash, 13);
	rotate_right(hash, 37);
	swap_chars(hash, 'g', 'i');
	swap_chars(hash, 'r', 'u');
	swap_chars(hash, 'g', 'a');
	swap_chars(hash, 'm', 'e');
	swap_chars(hash, 's', 'h');
	hash = morse_code(hash);

	pwField.value = hash.join(' ').replace(/ +/g, ' ');
}

function rotate_right(pass, amount) {
	for (var i=0; i<amount; i++) {
		for (var j=pass.length-1; j>0; j--) {
			var temp = pass[j];
			pass[j] = pass[j-1];
			pass[j-1] = temp;
		}
	}
}

function swap_chars(pass, c1, c2) {
	for (var i=0; i<pass.length; i++) {
		if (pass[i] == c1) {
			pass[i] = c2;
		}
		else if (pass[i] == c2) {
			pass[i] = c1;
		}
	}
}

function caesarian_shift(pass, amount) {
	for (var i=0; i<pass.length; i++) {
		if (pass[i].match(/[a-z]/i)) {
			pass[i] = String.fromCharCode(((pass[i].charCodeAt()-97+amount)%26)+97);
		}
	}
}

function morse_code(pass) {
	var alphabet = {
		'a': '.-',    'b': '-...',  'c': '-.-.', 'd': '-..',
		'e': '.',     'f': '..-.',  'g': '--.',  'h': '....',
		'i': '..',    'j': '.---',  'k': '-.-',  'l': '.-..',
		'm': '--',    'n': '-.',    'o': '---',  'p': '.--.',
		'q': '--.-',  'r': '.-.',   's': '...',  't': '-',
		'u': '..-',   'v': '...-',  'w': '.--',  'x': '-..-',
		'y': '-.--',  'z': '--..',  ' ': '/',
		'1': '.----', '2': '..---', '3': '...--', '4': '....-', 
		'5': '.....', '6': '-....', '7': '--...', '8': '---..', 
		'9': '----.', '0': '-----'
	};
	return pass.map(function(e){return alphabet[e] || '';});
}
</script>
</head>

<body>
<div class="login">
	<form method="POST" onsubmit="hash_password(document.getElementById('password'))">
<?php
$correctPw = '... ..-. ..- --.. ..- - ...- -- ... - -. --.. ..- ..-. .-. .--- ..- -.-- -.-- ..- -.- .--.';
if (isset($_POST['username']) && isset($_POST['password'])){
	if (($_POST['username'] == "girugamesh") and ($_POST['password'] == $correctPw)) {
		setcookie("flag", $correctPw, time()+86400, "/");
		header('Location: index.php');
		die();
	}
	else {
		echo 'Invalid username/password!<br>';
	}
}
?>
	<input type="text" name="username" placeholder="Username" required><br>
	<input type="password" name="password" id="password" placeholder="Password" required><br>
	<button type="submit">Login</button>
	</form>
</div>
</body>
</html>
