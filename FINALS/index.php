<?php 
    include('connections.php'); 
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
<body>
    <?php include('nav.php'); ?>
    <img src="images/banner.jpg" class="img-fluid" id="banner" alt="...">
    <br><br>
    <center><h1>Categories</h1></center>
    <div class="categories">
        <a href="pccomponent.php"><div class="card">
            <div class="imgcard">
            <img src="images/components.png" class="img-fluid cat" alt="...">
            </div>
            <div class="textcard">
                <p>PC COMPONENTS</p>
            </div>
        </div></a>
        <a href="peripherals.php"><div class="card">
            <div class="imgcard">
            <img src="images/peripherals.png" class="img-fluid cat" alt="...">
            </div>
            <div class="textcard">
                <p>PERIPHERALS AND ACCESSORIES</p>
            </div>
        </div></a>
        <a href="desktop.php"><div class="card">
            <div class="imgcard">
            <img src="images/desktop.png" class="img-fluid cat" alt="...">
            </div>
            <div class="textcard">
                <p>DESKTOP PCS</p>
            </div>
        </div></a>
        <a href="laptop.php"><div class="card">
            <div class="imgcard">
            <img src="images/laptop.png" class="img-fluid cat" alt="...">
            </div>
            <div class="textcard">
                <p>LAPTOPS</p>
            </div>
        </div></a>
    </div>


    <?php include('footer.php'); ?>
    
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>