<?php 
    include('connections.php'); 

    $username  = $address = $contact= $email = $password = $cpassword = "";
    $usernameErr = $addressErr = $contactErr = $emailErr = $passwordErr = $cpasswordErr = "";

    if ($_SERVER["REQUEST_METHOD"] == "POST"){

        if(empty($_POST["username"])){
            $usernameErr = "First Name is required!";
        }else{
            $username = $_POST["username"];
        }

        if(empty($_POST["address"])){
            $addressErr = "Address is required!";
        }else{
            $address = $_POST["address"];
        }

        if(empty($_POST["contact"])){
            $contactErr = "Contact Number is required!";
        }else{
            $contact = $_POST["contact"];
        }

        if(empty($_POST["email"])){
            $emailErr = "Email is required!";
        }else{
            $email = $_POST["email"];
        }

        if(empty($_POST["password"])){
            $passwordErr = "Password is required!";
        }else{
            $password = $_POST["password"];
        }

        if(empty($_POST["cpassword"])){
            $cpasswordErr = "Confirm Password is required!";
        }else{
            $cpassword = $_POST["cpassword"];
        }

        if($username && $address && $contact && $email && $password && $cpassword) {

            $check_email = mysqli_query($connections, "SELECT * FROM profiles WHERE email='$email'");
            $check_email_row = mysqli_num_rows($check_email);

            if($check_email_row > 0) {

                $emailErr = "Email is already registered!"; 

            }else{

                if ($password != $cpassword){
                    $cpasswordErr = "Confirm Password does not match!";
                }else{
                    $query = mysqli_query($connections, "INSERT INTO profiles(username, address, contact, email, password, account_type)
                
                VALUES('$username', '$address', '$contact', '$email', '$cpassword', '2')");

                echo"<script language='javascript'>alert('Your account has been registered!')</script>";
                echo"<script>window.location.href='login.php';</script>";
                }
            }
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
            <p class="title">Sign Up</p>
                <form class="form" method="POST" action="<?php htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
                    <div class="input-group">
                        <label for="username">Username</label>
                        <input type="text" name="username" id="username" value="<?php echo $username; ?>"/>
                    </div>
                    <div class="error"><?php echo $usernameErr; ?></div><br>
                    <div class="input-group">
                        <label for="address">Address</label>
                        <input type="text" name="address" id="address" value="<?php echo $address; ?>">
                    </div>
                    <div class="error"><?php echo $addressErr; ?></div><br>
                    <div class="input-group">
                        <label for="contact">Contact Number</label>
                        <input type="text" name="contact" id="contact" value="<?php echo $contact; ?>">
                    </div>
                    <div class="error"><?php echo $contactErr; ?></div><br>
                    <div class="input-group">
                        <label for="email">Email</label>
                        <input type="email" name="email" id="email" value="<?php echo $email; ?>">
                    </div>
                    <div class="error"><?php echo $emailErr; ?></div><br>
                    <div class="input-group">
                        <label for="password">Password</label>
                        <input type="password" name="password" id="password" value="<?php echo $password; ?>">
                    </div>
                    <div class="error"><?php echo $passwordErr; ?></div><br>
                    <div class="input-group">
                        <label for="cpassword">Confirm Password</label>
                        <input type="password" name="cpassword" id="cpassword" value="<?php echo $cpassword; ?>">
                    </div>
                    <div class="error"><?php echo $cpasswordErr; ?></div><br><br>
                    <button class="sign" type="submit" value="Submit">Sign Up</button>
                </form>
            <p class="signup">Already have an account?
                <a rel="noopener noreferrer" href="login.php" class="">Log In</a>
            </p>
        </div>
    </div>

    <?php include('footer.php'); ?>
    
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>    