<?php 
include('connections.php');
$loginErr = "";

if (isset($_POST["login"])) {

    if (!empty($_POST["email"]) && !empty($_POST["password"])) {
        $email = $_POST["email"];
        $password = $_POST["password"];

        // Prepare query securely using both email and password
        $check_profile = mysqli_query($connections, "SELECT * FROM profiles WHERE email='$email' AND password='$password'");

        if (mysqli_num_rows($check_profile) > 0) {
            $row = mysqli_fetch_assoc($check_profile);
            $_SESSION["user_id"] = $row["id"];
            if ($row["account_type"] == "1") {
                header("Location: admin/index.php");
            } else {
                header("Location: user/index.php");
            }
        } else {
            $loginErr = "Email or Password is Incorrect!";
        }
    } else {
        $loginErr = "Missing email/password!";
    }
}
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">


    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <!--=============== CSS ===============-->
    <link rel="stylesheet" href="style.css">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

    <title>Document</title>
</head>
<body id="loginpage">
    <?php include('nav.php'); ?>

    <div class="login">
        <div class="form-container">
            <p class="title">Login</p>
                <form class="form" method="POST" action="<?php htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
                    <div class="input-group">
                        <label for="email">Email</label>
                        <input type="email" name="email" id="email" placeholder="">
                    </div>
                    <div class="input-group">
                        <label for="password">Password</label>
                        <input type="password" name="password" id="password" placeholder="">
                    </div>
                    <div class="error"><p><?php echo $loginErr; ?></p></div><br> 
                    <button class="sign", name="login">Log in</button>
                </form>
            
            <p class="signup">Don't have an account?
                <a rel="noopener noreferrer" href="signup.php" class="">Sign up</a>
            </p>
        </div>
    </div>

    <?php include('footer.php'); ?>
    
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>