
<?php
include('../connections.php');

if (!isset($_SESSION['user_id'])) {
    header("Location: ../login.php");
    exit;
}

$user_id = $_SESSION['user_id'];

// Fetch user info (username, address)
$user_query = mysqli_query($connections, "SELECT username, address FROM profiles WHERE id='$user_id'");
$user = mysqli_fetch_assoc($user_query);
$username = $user['username'];
$address = $user['address'];

// Fetch cart items
$cart_query = mysqli_query($connections, "SELECT * FROM cart WHERE id='$user_id'");
$cart_items = [];
while ($row = mysqli_fetch_assoc($cart_query)) {
    $cart_items[] = $row;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && !empty($cart_items)) {
    $date_of_checkout = date('Y-m-d H:i:s');
    $date_of_delivery = date('Y-m-d H:i:s', strtotime('+3 days'));
    foreach ($cart_items as $item) {
        $product_id = $item['product_id'];
        $product_name = $item['product_name'];
        $photo_name = $item['photo_name'];
        $cost = $item['cost'];
        $quantity = $item['quantity'];
        $status = "Processing";

        // Insert into orders table (now with date_of_delivery)
        $insert = mysqli_query($connections, "INSERT INTO orders 
            (product_id, product_name, photo_name, cost, quantity, id, username, address, date_of_checkout, date_of_delivery, status)
            VALUES (
                '$product_id',
                '".mysqli_real_escape_string($connections, $product_name)."',
                '".mysqli_real_escape_string($connections, $photo_name)."',
                '$cost',
                '$quantity',
                '$user_id',
                '".mysqli_real_escape_string($connections, $username)."',
                '".mysqli_real_escape_string($connections, $address)."',
                '$date_of_checkout',
                '$date_of_delivery',
                '$status'
            )");
    }
    // Clear cart after checkout
    mysqli_query($connections, "DELETE FROM cart WHERE id='$user_id'");
    echo "<script>alert('Order placed successfully!'); window.location='orders.php';</script>";
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Checkout</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="../style.css">
</head>
<body>
<?php include('nav.php'); ?>
<div class="container" style="max-width: 700px; margin-top: 40px;">
    <h2>Checkout</h2>
    <?php if (empty($cart_items)): ?>
        <div class="alert alert-info mt-4">Your cart is empty.</div>
    <?php else: ?>
        <form method="post">
            <div class="mb-3">
                <label class="form-label">Name:</label>
                <input type="text" class="form-control" value="<?php echo htmlspecialchars($username); ?>" readonly>
            </div>
            <div class="mb-3">
                <label class="form-label">Address:</label>
                <input type="text" class="form-control" value="<?php echo htmlspecialchars($address); ?>" readonly>
            </div>
            <h5>Order Summary:</h5>
            <ul class="list-group mb-3">
                <?php $grand_total = 0; ?>
                <?php foreach ($cart_items as $item): ?>
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <div>
                            <img src="../images/<?php echo htmlspecialchars($item['photo_name']); ?>" alt="" style="width:40px; height:40px; object-fit:contain; margin-right:10px;">
                            <?php echo htmlspecialchars($item['product_name']); ?> (x<?php echo $item['quantity']; ?>)
                        </div>
                        <span>₱<?php echo number_format($item['cost'] * $item['quantity'], 2); ?></span>
                    </li>
                    <?php $grand_total += $item['cost'] * $item['quantity']; ?>
                <?php endforeach; ?>
                <li class="list-group-item d-flex justify-content-between align-items-center fw-bold">
                    Total
                    <span>₱<?php echo number_format($grand_total, 2); ?></span>
                </li>
            </ul>
            <button type="submit" class="btn btn-success w-100">Place Order</button>
        </form>
    <?php endif; ?>
</div>

    <?php include('footer.php'); ?>
</body>
</html>