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
    <div class="header-spacer"></div>
    <header class="locations-header">
        <div class="header-content">
            <h1>OUR LOCATIONS</h1>
            <p class="subtitle">Find a TechHive store near you</p>
        </div>
    </header>
    
    <div class="locations-container anim">
        <div class="locations-list">
            <div class="location-item">
                <h4 class="location-name"
                data-map="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3866.008466810367!2d121.0727628!3d14.3109408!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3397d700282ccda3%3A0x9deefb36f76a53f4!2sTechHive!5e0!3m2!1sen!2sph!4v1746367473356!5m2!1sen!2sph">
                    TechHive Main Branch
                </h4>
                <p class="location-address">
                    836F+94C Santo Tomas,<br>
                    Calabuso, Biñan,<br>
                    Laguna
                </p>
            </div>
            
            <div class="location-item">
                <h4 class="location-name" 
                    data-map="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d61830.139107068746!2d120.91141243124997!3d14.405031400000006!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3397d22d463d98c7%3A0xe48e5b9730fcfdbc!2sTech%20Hive!5e0!3m2!1sen!2sph!4v1746371314951!5m2!1sen!2sph">
                    TechHive HAL
                </h4>
                <p class="location-address">
                    CX4G+2W8,  <br>
                    Molino Rd, Espeleta, <br>
                    Bacoor, Cavite
                </p>
            </div>

            <div class="location-item">
                <h4 class="location-name" 
                    data-map="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3888.016071332049!2d77.5941603!3d12.9721908!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae1670c9b44e6d%3A0xf5df53c20bc8e3f1!2sTechHive!5e0!3m2!1sen!2sin!4v1623391234567!5m2!1sen!2sin">
                    TechHive Koramangala
                </h4>
                <p class="location-address">
                    The Forum Mall<br>
                    1st Block East, Koramangala<br>
                    Bengaluru 560034
                </p>
            </div>
                   
            <div class="location-item">
                <h4 class="location-name" 
                    data-map="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3988.797862043689!2d103.838071!3d1.300494!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31da19a936154b6d%3A0x1a9f0c0b8f8b8f8b!2s456%20Orchard%20Road%2C%20Singapore%20238879!5e0!3m2!1sen!2ssg!4v1623391234567!5m2!1sen!2ssg">
                    TechHive Singapore
                </h4>
                <p class="location-address">
                    456 Orchard Road<br>
                    #03-01 Tech Building<br>
                    Singapore 238879
                </p>
            </div>
        </div>
        
        <div class="map-container">
            <iframe id="dynamic-map" class="map-iframe" 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3866.008466810367!2d121.0727628!3d14.3109408!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3397d700282ccda3%3A0x9deefb36f76a53f4!2sTechHive!5e0!3m2!1sen!2sph!4v1746367473356!5m2!1sen!2sph" 
                allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade">
            </iframe>
        </div>

    </div>
    <div class="footer-spacer"></div>

    <?php include('footer.php'); ?>

    <script type="text/javascript" src="../plugin.js"></script>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>