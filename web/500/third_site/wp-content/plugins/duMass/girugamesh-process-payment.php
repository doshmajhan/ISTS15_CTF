<?php

if (($_SERVER['HTTP_REFERER'] !== 'http://(site 3)/wp-content/plugins/duMass/payment.html') or (strpos($_SERVER['HTTP_USER_AGENT'], 'Mozilla/5.0') === false)) {
    die("Tampering detected!!");
}

echo("Thanks for your business, asshole!");

?>