<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Girugamap</title>
<meta name="description" content="SVG/VML Interactive USA map">
<meta name="author" content="LGLab">

<link href="css/reset.css" rel="stylesheet" type="text/css" />
<link href="css/fonts.css" rel="stylesheet" type="text/css" />
<link href="css/style.css" rel="stylesheet" type="text/css" />
<link href="css/map.css" rel="stylesheet" type="text/css" />

<script src="js/RequestAnimationFrame.js"></script>
<script src="js/jquery.js" type="text/javascript"></script>
<script type="text/javascript" src="js/jquery.mousewheel.js"></script>
<script src="js/raphael.js" type="text/javascript"></script>
<script src="js/raphaelAnimateViewBox.js" type="text/javascript"></script>
<script src="js/scale.raphael.js" type="text/javascript"></script>
<script src="js/paths.js" type="text/javascript"></script>
<script src="js/init.js" type="text/javascript"></script>

</head>

<body>
	
    <div id="container">
<?php
if ($_COOKIE["flag"] == "... ..-. ..- --.. ..- - ...- -- ... - -. --.. ..- ..-. .-. .--- ..- -.-- -.-- ..- -.- .--.") {
echo '<center>
Welcome, your highness!<br><br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/di6mwsgT1WM?autoplay=1" frameborder="0" allowfullscreen></iframe><br><br>
</center>';
} else {
echo '<p style="float: left"><a href="login.php">Log in</a></p><p style="float: right">Currently logged in: girugamesh</p><div style="clear: both;"></div><br>';
}
?>
        <div class="mapWrapper">
                
                <div id="map"></div>
                
                <div class="console">
                        
                        <ul class="left">					
                            <li>
                                <span id="zoomerIn"><img src="images/in.png"/></span>
                                <span id="zoomerOut"><img src="images/out.png"/></span>
                                <span id="zoomerUp"><img src="images/up.png"/></span>
                                <span id="zoomerDown"><img src="images/down.png"/></span>
                                <span id="zoomerLeft"><img src="images/left.png"/></span>
                                <span id="zoomerRight"><img src="images/right.png"/></span>
                            </li>
                        </ul>
                        
                        <ul class="right">
                            <li>
                                <span id="zoomerReset"><img src="images/reset.png"/></span>
                            </li>
                        </ul>
                    
                </div>
                
                <div id="text"></div>
                     
        </div>
        
    </div>
    

</body>
</html>
