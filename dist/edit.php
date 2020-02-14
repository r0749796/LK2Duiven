<?php
//Database Connection
include 'config.php';
//Get ID from Database
if(isset($_GET['id'])){
 $sql = "SELECT * FROM duiven WHERE id =" .$_GET['id'];
 $result = mysqli_query($link, $sql);
 $row = mysqli_fetch_array($result);
}
 
//Update Information
if(isset($_POST['btn-update'])){
 $naam = $_POST['naam'];
 $geboortedatum = $_POST['geboortedatum'];
 $leeftijd = $_POST['leeftijd'];
 $initialstate = $_POST['initialstate'];
 echo $naam, $geboortedatum, $leeftijd, $initialstate;
 $update = "UPDATE duiven SET naam='$naam', geboortedatum='$geboortedatum',leeftijd='$leeftijd', initialstate='$initialstate' WHERE id=". $_GET['id'];
 $up = mysqli_query($link, $update);
 if(!isset($sql)){
 die ("Error $sql" .mysqli_connect_error());
 }
 else
 {
 header("location: index.php");
 }
}
?>
<!--Create Edit form -->
<!doctype html>
<html>
<body>
<form method="post">
<h1>Bewerk Duif Gegevens</h1>
<label>Naam</label><input type="text" name="naam" placeholder="Name" value="<?php echo $row['naam']; ?>"><br/><br/>
<label>Geboortedatum:</label><input type="text" name="geboortedatum" placeholder="Gender" value="<?php echo $row['geboortedatum']; ?>"><br/><br/>
<label>Leeftijd:</label><input type="text" name="leeftijd" placeholder="Department" value="<?php echo $row['leeftijd']; ?>"><br/><br/>
<label>Link:</label><input type="text" name="initialstate" placeholder="Address" value="<?php echo $row['initialstate']; ?>"><br/><br/>
<button type="submit" name="btn-update" id="btn-update" onClick="update()"><strong>Update</strong></button>
<a href="index.php"><button type="button" value="button">Cancel</button></a>
</form>
<!-- Alert for Updating -->
<script>
function update(){
 var x;
 if(confirm("Duif is succesvol bewerkt!") == true){
 x= "update";
 }
}
</script>
</body>
</html>