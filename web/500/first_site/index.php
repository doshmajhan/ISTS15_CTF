<?php
if (strpos($_SERVER[HTTP_USER_AGENT], 'curl') !== false) {
echo("<html>
<head>
<title>RESTRICTED ZONE</title>
<style type='text/css'>
body {
  font-family:Courier;
 color: #CCCCCC;
  background: #000000;
  border: 3px double #CCCCCC;
  padding: 10px;
}
</style>
</head>
<body>
<p>Alright, here's the scoop. We're selling all the shit we stole from Girugamesh! We've got boatloads of his stuff in the warehouse, all ready to go. Discount prices! Just wire us the dough directly through Western Union and the goods will show up on your doorstep the next morning.</p>
<p>Not convinced? Sigh, no one ever is... I guess if you wanna see some pics of the goods, head on over to (second_site). But after give me your money!</p>
</body>
</html>
");
}
else {
echo("
<html>
<head>
<link rel='stylesheet' href='style.css' type='text/css'>
<title>Gilgamesh's House of Curl</title>
</head>

<body>
<center><img src='images/banner.gif'>
<div class='container'>
    <div class='column-left'>
        <img src='images/curl1.PNG' width=75%><br><br><br>
        <img src='images/curl5.jpg' width=75%><br>
    </div>
   <div class='column-center'>
        <h1>Heh heh nothing out of the ordinary here! Just a normal gym website, now move along please!</h1>
        <img src='images/curl2.jpg' width=75%>
    </div>
   <div class='column-right'>
        <img src='images/curl4.jpg' width=50%><br><br><br>
        <img src='images/curl3.jpg' width=50%>
   </div>
</div>
</center>
</body>
</html>");
}
?>
