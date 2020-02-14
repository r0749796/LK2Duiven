<?php
require_once "config.php";
 
// Check connection
if($link === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}
 
// Escape user inputs for security
$id = mysqli_real_escape_string($link, $_REQUEST['id']);
$naam = mysqli_real_escape_string($link, $_REQUEST['naam']);
$geboortedatum = mysqli_real_escape_string($link, $_REQUEST['geboortedatum']);
$leeftijd = mysqli_real_escape_string($link, $_REQUEST['leeftijd']);
$initialstate = mysqli_real_escape_string($link, $_REQUEST['initialstate']);

 
// Attempt insert query execution
$sql = "INSERT INTO duiven (id, naam, geboortedatum, leeftijd, initialstate) VALUES ('$id', '$naam', '$geboortedatum', '$leeftijd', '$initialstate')";
if(mysqli_query($link, $sql)){
    echo "Duif is succesvol toegevoegd!";
    echo "<script>setTimeout(\"location.href = 'index.php';\",1500);</script>";

} else{
    echo "ERROR: kon de duif niet toevoegen. $sql. " . mysqli_error($link);
}
 
// Close connection
mysqli_close($link);
?>