<?php

$product_id = $_REQUEST["product_id"];
include("../connections.php");

// Get product details
$view_query = mysqli_query($connections, "SELECT * FROM products WHERE product_id='$product_id'");
$row = mysqli_fetch_assoc($view_query);

if ($row) {
    $product_id_check = $row["product_id"];
    $db_productname = $row["product_name"];
    $db_photoname = $row["photo_name"];
    $quantity = 1;
    $db_cost = $row["cost"];

    // Check if product is already in user's cart
    $view_query_cart = mysqli_query($connections, "SELECT * FROM cart WHERE product_id='$product_id' AND id='$_SESSION[user_id]'");
    if (mysqli_num_rows($view_query_cart) > 0) {
        echo "<script>alert('Product is already in your cart!'); window.location=document.referrer;</script>";
        exit;
    } else {
        // Add to cart
        $query = mysqli_query($connections, "INSERT INTO cart(product_id, id, product_name, photo_name, quantity, cost)
            VALUES('$product_id_check', '$_SESSION[user_id]', '$db_productname', '$db_photoname', '$quantity', $db_cost)");
        echo "<script>alert('Added to cart!'); window.location=document.referrer;</script>";
        exit;
    }
} else {
    echo "<script>alert('Product not found!'); window.history.back();</script>";
    exit;
}
?>