# What Goes Around...
The user is given the IP to the first site, which appears to be a gym website with a focus on 'curling'. Requesting the page with the cURL user-agent directs the user to the second site.

The second site has a bunch of images that are loaded from `viewimage.php` using a file path parameter and an access token parameter. The access token is the same for many of the images, and is seemingly composed of hex values. Upon further inspection, this access token is actually the first 4 bytes of the file being requested.

To get to the next phase of the challenge, the user needs to exploit a file inclusion vulnerability within the file path parameter to load the actual `viewimage.php` file and reveal its source code. However, the application only allows file paths starting with `images`, so the file path must be modified to `images/../viewimage.php`. As this is a php file, the user can easily guess the first 4 bytes of the file (`3C 3F 70 68` or `<?ph`). A comment within the php file reveals the IP of the third and final website.

The final website is a WordPress blog that discusses a new payment processing system implemented on the site that is not yet publicly accessible. Links on the bottom of the page indicate the blog owner is a WordPress plugin developer. Looking in the WordPress plugin directory, the user will find the new payment processing plugin. However, the main HTML form within the plugin was tampered with, and the original POST endpoint for the payment data was commented out and replaced with a new one.

POSTing to the original endpoint requires that the Referer header is set to the HTML form and the User-Agent header contains 'Mozilla/5.0'. If these conditions are satisfied, the flag is returned.
