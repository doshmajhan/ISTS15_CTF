<?php

if (($_SERVER['HTTP_REFERER'] !== 'http://(site 3)/wp-content/plugins/duMass/payment.html') or (strpos($_SERVER['HTTP_USER_AGENT'], 'Mozilla/5.0') === false)) {
    die("Tampering detected!!");
}

echo("<!-- flag{wh47_g035_4r0und_c0m35_4r0und} -->
Thanks for your business!");

?>