<?php
include('../connections.php');
session_start();

if (isset($_GET['product_id']) && isset($_SESSION['user_id'])) {
    $product_id = intval($_GET['product_id']);
    $user_id = $_SESSION['user_id'];

    // Delete the product from the cart for the current user only
    $query = "DELETE FROM cart WHERE product_id = $product_id AND id = '$user_id'";
    mysqli_query($connections, $query);
}

// Redirect back to the cart page
header("Location: cart.php");
exit;
?>