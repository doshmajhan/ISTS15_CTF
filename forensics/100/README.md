# Suspicious Images
Teams are given: The 3 images `not_a_flag.png`, `snoopy.jpg`, `treasure.tiff`

1. `not_a_flag.png` has a pdf file and 7z archive in it. Simply open the image in 7zip and find the folder with the flag txt file. (First part of flag)
2. `snoopy.jpg` has data hidden in the exif data under "Image Description". (Middle part of flag)
3. `treasure.tiff` has the last part of the flag in two places. Faintly in the image itself (opacity turned down), playing with hue/sat makes it more visible and actually just concatenated to the end of the file. So either play with it in photoshop and zoom or echo out the file.
