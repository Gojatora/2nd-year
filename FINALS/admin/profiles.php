<?php 
    include('../connections.php'); 
?>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["save_profile"])) {
    $user_id = mysqli_real_escape_string($connections, $_POST["user_id"]);
    $username = mysqli_real_escape_string($connections, $_POST["username"]);
    $address = mysqli_real_escape_string($connections, $_POST["address"]);
    $contact = mysqli_real_escape_string($connections, $_POST["contact"]);
    $email = mysqli_real_escape_string($connections, $_POST["email"]);
    $password = mysqli_real_escape_string($connections, $_POST["password"]);

    $update_query = "UPDATE profiles SET 
                        username = '$username',
                        address = '$address',
                        contact = '$contact',
                        email = '$email',
                        password = '$password'
                     WHERE id = '$user_id'";

    if (mysqli_query($connections, $update_query)) {
        echo "<script>
                alert('User profile has been updated successfully.');
                window.location.href = '{$_SERVER["PHP_SELF"]}';
              </script>";
        exit;
    } else {
        echo "<script>alert('Error updating profile: " . mysqli_error($connections) . "');</script>";
    }
}
?>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["delete_user"])) {
    $delete_id = mysqli_real_escape_string($connections, $_POST["delete_id"]);

    $delete_query = "DELETE FROM profiles WHERE id = '$delete_id'";

    if (mysqli_query($connections, $delete_query)) {
        echo "<script>
                alert('User deleted successfully.');
                window.location.href = 'profiles.php';
              </script>";
        exit;
    } else {
        echo "<script>alert('Error deleting user: " . mysqli_error($connections) . "');</script>";
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
    <link rel="stylesheet" href="../style.css">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

    <title>Document</title>
</head>
<body>
    <?php include('nav.php'); ?>
    <br><br><br><br><br>
    <center><h1>Profiles</h1></center>
    <br>
    <center>
    <input type="text" id="searchInput" class="form-control w-50 mb-4" placeholder="Search by username, email, or any field...">
    <table>
    <thead>
        <tr class="header">
        <th scope="col">ID</th>
        <th scope="col">Username</th>
        <th scope="col">Address</th>
        <th scope="col">Contact Number</th>
        <th scope="col">Email</th>
        <th scope="col">Password</th>
        <th scope="col">Options</th>
        </tr>
    </thead>
    <tbody>
    <?php

        $view_query = mysqli_query($connections, "SELECT * FROM profiles WHERE account_type=2");

        while($row = mysqli_fetch_assoc($view_query)){
            $user_id = $row["id"];
            $username = $row["username"];
            $address = $row["address"];
            $contact = $row["contact"];
            $email = $row["email"];
            $password = $row["password"];
        
            echo"<tr>
            <td data-label='ID'>$user_id</td>
            <td data-label='Username'>$username</td>
            <td data-label='Address'>$address</td>
            <td data-label='Contact Number'>$contact</td>
            <td data-label='Email'>$email</td>
            <td data-label='Password'>$password</td>
            <td data-label='Options'>
                <div class='options'>
                    <button type='button' class='btn editBtn' data-id='$user_id'>Edit</button>

                    <form method='POST' onsubmit='return confirmDelete();' action='profiles.php' style='display:inline;'>
                        <input type='hidden' name='delete_id' value='$user_id'>
                        <button type='submit' name='delete_user' class='btn btn-danger'>Delete</button>
                    </form>
                </div>
            </td>

            </tr>
            <tr id='edit-$user_id' style='display: none;'>
            <form method='POST' action='profiles.php'>
            <input type='hidden' name='user_id' value='$user_id' />
            <td>$user_id</td>
            <td><input type='text' name='username' value='$username'/></td>
            <td><input type='text' name='address' value='$address'/></td>
            <td><input type='text' name='contact' value='$contact'/></td>
            <td><input type='email' name='email' value='$email'/></td>
            <td><input type='text' name='password' value='$password'/></td>
            <td>
                <button type='submit' name='save_profile' class='btn'>Save</button>
                <button type='button' class='btn cancelBtn' data-id='$user_id'>Cancel</button>
            </td>
            </form>
            </tr>";
        }        
    ?>
    </tbody>
    </table>
    </center>
    <br><br><br>

    <script type="text/javascript" src="../plugin.js"></script>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>