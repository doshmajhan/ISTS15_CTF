<?php
#TODO note to self: do a blog post on this
# ^^ resolved: (site3 URL)

$fileName = $_GET["file"];
$fileSig = $_GET["accesstoken"]; # LOL theyll never crack this one

if (substr($fileName, 0, 6) !== 'images') {
	die("That's not an image!");
}

if (file_exists($fileName)) {
	$handle = fopen($fileName, "rb");
	$contents = fread($handle, 4);
	fclose($handle);
	if (hex2bin($fileSig) === $contents) {
		$imageInfo = getimagesize($fileName);
		switch ($imageInfo[2]) {
			case IMAGETYPE_JPEG:
				header("Content-Type: image/jpeg");
				break;
			case IMAGETYPE_GIF:
				header("Content-Type: image/gif");
				break;
			case IMAGETYPE_PNG:
				header("Content-Type: image/png");
				break;
			default:
				break;
		}
		header('Content-Length: ' . filesize($fileName));
		readfile($fileName);
	}
	else {
		die("Invalid access token!");
	}
}
else {
	die("File not found");
}
?>
