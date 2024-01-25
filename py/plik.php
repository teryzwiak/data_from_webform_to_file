<?php
$number = $_POST['liczba'];
$myfile = fopen("testfile.txt", "w");
fwrite($myfile, $number);
header("Location: index.php");
?>