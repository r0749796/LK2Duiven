<?php
//delete.php
include('config.php');
$id = $_GET['id']; //this needs to be sanitized 
if(!empty($id)){
    $sql="DELETE FROM duiven WHERE id=".$id.";";
    mysqli_query($link, $sql);
}
header("Location: index.php");
?>