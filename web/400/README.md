# Girugamap
Users begin by sending a Facebook message to a chat bot, which gives them the challenge website and asks them to send a link to a page on the same site back to them. The site takes an ID parameter that is parsed by client-side JavaScript, and displays an error message if the provided ID is invalid.

This error message is vulnerable to DOM XSS, which the user will craft a payload for and send back to the victim via IM. If the payload is not entirely URL-encoded, it will be rejected and the user is prompted to send another link; otherwise the victim will visit the link and the payload will fire. The payload will need to steal the victim's cookie and send it back to the user.

The cookie is actually the flag after being ran through a very insecure client-side "hashing" algorithm (the code for this algorithm is on the site's login page). The user will have to reverse the algorithm to get the flag in its original form.
