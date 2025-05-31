<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

// For demo/testing: set a default user_id if not logged in
if (empty($_SESSION["user_id"])) {
    // You can set a default user id for testing, e.g. 1
    $_SESSION["user_id"] = 0;
}


$connections = mysqli_connect("localhost", "root", "", "db_computer_retail");
    if (mysqli_connect_errno()){
        echo "Failed to connect to MySQL: " . mysqli_connect_error();
    }
?>


<?php
echo"<script>
window.addEventListener('pageshow', function(event) {
    if (event.persisted) {
        window.location.reload();
    }
});
</script>";
?>


