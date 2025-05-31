
<?php
  include('../connections.php');

  if($_SESSION['user_id'] == 0){
    header("Location: ../index.php");
    exit;
  }

  if (isset($_POST["logout"])) {
    session_unset();
    session_destroy();
    header("Location: ../index.php");
    exit;
  }
?>

<nav class="navbar fixed-top navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="index.php">TechHive</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item">
          <a class="nav-link" aria-current="page" href="index.php">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="profiles.php">Profiles</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="products.php">Products</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="orders.php">Orders</a>
        </li>
        <li class="nav-item dropdown" id="login">
        <a class="nav-link dropdown-toggle custom-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false">
        <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
          <path fill-rule="evenodd" d="M12 20a7.966 7.966 0 0 1-5.002-1.756l.002.001v-.683c0-1.794 1.492-3.25 3.333-3.25h3.334c1.84 0 3.333 1.456 3.333 3.25v.683A7.966 7.966 0 0 1 12 20ZM2 12C2 6.477 6.477 2 12 2s10 4.477 10 10c0 5.5-4.44 9.963-9.932 10h-.138C6.438 21.962 2 17.5 2 12Zm10-5c-1.84 0-3.333 1.455-3.333 3.25S10.159 13.5 12 13.5c1.84 0 3.333-1.455 3.333-3.25S13.841 7 12 7Z" clip-rule="evenodd"/>
        </svg> 
        <?php $view_query = mysqli_query($connections, "SELECT * FROM profiles where id='$_SESSION[user_id]'"); 
                while($row = mysqli_fetch_assoc($view_query)){

                    $username = $row["username"];

                    echo "$username";

                  };?>
        </a>
          <ul class="dropdown-menu">
            <li><form action="<?php htmlspecialchars($_SERVER["PHP_SELF"]); ?>", method="post"><button class="dropdown-item" name="logout">Log Out</button></form></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</nav>