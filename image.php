<?php
//get the last used number for naming file
/*
This is the camera interface between the web and the RPi.
    Copyright (C) 2019 Jeremiah ONeal and Natalie ONeal 

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/
header("Content-type: image/jpeg");
$im = imagecreatefromjpeg("/work/video.jpg");
imagejpeg($im);
imagedestroy($im);

exit(0);
?>
