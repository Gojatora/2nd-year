<?php
include('../connections.php');
if (isset($_POST['product_id'], $_POST['quantity'], $_SESSION['user_id'])) {
    $product_id = intval($_POST['product_id']);
    $quantity = max(1, intval($_POST['quantity']));
    mysqli_query($connections, "UPDATE cart SET quantity=$quantity WHERE product_id=$product_id AND id='$_SESSION[user_id]'");
}
header("Location: cart.php");
exit;
?>
?