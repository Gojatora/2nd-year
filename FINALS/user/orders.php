<?php
include('../connections.php');
session_start();

if (!isset($_SESSION['user_id'])) {
    header("Location: ../login.php");
    exit;
}

$user_id = $_SESSION['user_id'];
$order_query = mysqli_query($connections, "SELECT * FROM orders WHERE id='$user_id' ORDER BY date_of_checkout DESC");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Orders</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="../style.css">
</head>
<body>
<?php include('nav.php'); ?>

<div class="container" style="max-width: 900px; margin-top: 40px;">
    <h2 class="mb-4">My Orders</h2>
    <?php if (mysqli_num_rows($order_query) == 0): ?>
        <div class="alert alert-info">You have no orders yet.</div>
    <?php else: ?>
        <div class="table-responsive">
        <table class="table table-bordered align-middle">
            <thead class="table-dark">
                <tr>
                    <th>Product</th>
                    <th>Photo</th>
                    <th>Quantity</th>
                    <th>Cost</th>
                    <th>Date Ordered</th>
                    <th>Date of Delivery</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
            <?php while($order = mysqli_fetch_assoc($order_query)): ?>
                <tr>
                    <td><?php echo htmlspecialchars($order['product_name']); ?></td>
                    <td>
                        <img src="../images/<?php echo htmlspecialchars($order['photo_name']); ?>" alt="" style="width:60px; height:60px; object-fit:contain;">
                    </td>
                    <td><?php echo $order['quantity']; ?></td>
                    <td>₱<?php echo number_format($order['cost'], 2); ?></td>
                    <td><?php echo date('M d, Y H:i', strtotime($order['date_of_checkout'])); ?></td>
                    <td><?php echo date('M d, Y', strtotime($order['date_of_delivery'])); ?></td>
                    <td>
                        <span class="badge bg-<?php echo $order['status'] == 'Processing' ? 'warning' : 'success'; ?>">
                            <?php echo htmlspecialchars($order['status']); ?>
                        </span>
                    </td>
                </tr>
            <?php endwhile; ?>
            </tbody>
        </table>
        </div>
    <?php endif; ?>
</div>
<?php include('footer.php'); ?>

    <script type="text/javascript" src="../plugin.js"></script>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>