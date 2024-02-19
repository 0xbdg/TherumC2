<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Login</title>

    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <link rel="stylesheet" href="../static/css/login.css" />
  </head>
  <body>
    <div class="login-container">
      <h2 class="log-title">Login</h2>
      <form method="post">
        <div class="form-group">
          <label for="username">Username:</label>
          <input
            type="text"
            id="username"
            name="username"
            placeholder="Enter username"
          />
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input
            type="password"
            id="password"
            name="password"
            placeholder="Enter password"
          />
        </div>
        <input class="btn" type="submit" value="Submit" />
      </form>
    </div>
  </body>
</html>

<?php
  if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $user_db = new PDO("sqlite:/var/www/html/C2Panel/db/user.db");
    $user = $_POST["username"];
    $pass = $_POST["password"];

    $prep = $user_db->prepare("SELECT * FROM users WHERE username = ? AND password = ?");
    $prep->execute([$user,$pass]);
    $row = $prep->fetch(PDO::FETCH_ASSOC);
    if($row){
      session_start();
      $_SESSION["username"] = $user;
      $_SESSION["password"] = $pass;
      header("Location: /C2Panel/pages/index.php");
    } else {
      header("Location: /C2Panel/pages/login");
    }
  }
?>