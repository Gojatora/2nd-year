
<?php
  include('../connections.php');

  if($_SESSION['user_id'] == 0){
    header("Location: ../index.php");
  }

  if (isset($_POST["logout"])) {
    session_unset();
    session_destroy();
    header("Location: ../index.php");
    exit;
  }
?>


<link rel="stylesheet" href="https://unpkg.com/boxicons@latest/css/boxicons.min.css">
<link rel="stylesheet" href="style.css">

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
        <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle custom-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Products
        </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="pccomponent.php">PC Components</a></li>
            <li><a class="dropdown-item" href="peripherals.php">Peripherals and Accessories</a></li>
            <li><a class="dropdown-item" href="desktop.php">Desktop PCs</a></li>
            <li><a class="dropdown-item" href="laptop.php">Laptops</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="location.php">Locations</a>
        </li>
        <li class="nav-item">
            <a class="nav-link cart-link" href="cart.php">
                <span class="cart-icon">
                    <i class='bx bx-shopping-bag'></i>
                    <span class="cart-count">
                      <?php

                        $i = 0;

                        $view_query = mysqli_query($connections, "SELECT * FROM cart WHERE id='$_SESSION[user_id]'");
                        while($row = mysqli_fetch_assoc($view_query)){
                            
                            $quantity = $row["quantity"];
                            
                            $i += $quantity; 
                        }

                        echo "<span>$i</span>";
                        ?>
                    </span>
                </span>
            </a>
        </li>
        <li class="nav-item dropdown" id="login">
        <a class="nav-link dropdown-toggle custom-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            <svg class='w-6 h-6 text-gray-800 dark:text-white' aria-hidden='true' xmlns='http://www.w3.org/2000/svg' width='24' height='24' fill='currentColor' viewBox='0 0 24 24'>
                  <path fill-rule='evenodd' d='M12 4a4 4 0 1 0 0 8 4 4 0 0 0 0-8Zm-2 9a4 4 0 0 0-4 4v1a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2v-1a4 4 0 0 0-4-4h-4Z' clip-rule='evenodd'/>
                </svg>
                <?php

                $get_record = mysqli_query($connections, "SELECT * FROM profiles WHERE id='$_SESSION[user_id]'");

                      while($row_edit = mysqli_fetch_assoc($get_record)){

                          $db_name = $row_edit["username"];

                          echo "$db_name";
                      };

                ?>
        </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="edit_profile.php">Manage Account</a></li>
            <form method="POST" action="<?php htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
              <li><input type="submit" name="logout" value="Log Out"  class="dropdown-item"></a></li>
            </form>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</nav>
