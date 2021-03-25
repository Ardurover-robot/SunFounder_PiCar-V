<?php
shell_exec("fswebcam -r 640x480 --jpeg 85 -D 1 /var/www/html/image.jpg");
header("Content-type: image/jpeg");
$im = imagecreatefromjpeg("/var/www/html/image.jpg");
imagejpeg($im);
imagedestroy($im);
exit(0);
?>
