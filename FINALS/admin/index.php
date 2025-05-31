<?php 
    include('../connections.php'); 
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
    <br><br><br><br>
    <center><h1>Dashboard</h1></center>
    <div class="categories">
        <a href="profiles.php"><div class="card">
            <div class="imgcard">
            <img src="../images/blank_profile.png" class="img-fluid cat" alt="...">
            </div>
            <div class="textcard">
                <p>Users </p>
            </div>
        </div></a>
        <a href="products.php"><div class="card">
            <div class="imgcard">
            <img src="../images/order.jpg" class="img-fluid cat" alt="...">
            </div>
            <div class="textcard">
                <p>Orders</p>
            </div>
        </div></a>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>