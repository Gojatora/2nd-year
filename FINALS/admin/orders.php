
<?php 
    include('../connections.php'); 
?>

<?php
// Handle status update
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["save_status"])) {
    $order_id = mysqli_real_escape_string($connections, $_POST["order_id"]);
    $status = mysqli_real_escape_string($connections, $_POST["status"]);

    $update_query = "UPDATE orders SET status = '$status' WHERE order_id = '$order_id'";
    if (mysqli_query($connections, $update_query)) {
        echo "<script>
                alert('Order status updated successfully.');
                window.location.href = '{$_SERVER["PHP_SELF"]}';
              </script>";
        exit;
    } else {
        echo "<script>alert('Error updating order: " . mysqli_error($connections) . "');</script>";
    }
}

// Handle delete order
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["delete_order"])) {
    $order_id = mysqli_real_escape_string($connections, $_POST["order_id"]);
    $delete_query = "DELETE FROM orders WHERE order_id = '$order_id'";
    if (mysqli_query($connections, $delete_query)) {
        echo "<script>
                alert('Order deleted successfully.');
                window.location.href = '{$_SERVER["PHP_SELF"]}';
              </script>";
        exit;
    } else {
        echo "<script>alert('Error deleting order: " . mysqli_error($connections) . "');</script>";
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="../style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    <title>Admin Orders</title>
</head>
<body>
    <?php include('nav.php'); ?>
    <br><br><br><br><br>
    <center><h1>Orders</h1></center>
    <br>
    <center>
    <input type="text" id="searchInput" class="form-control w-50 mb-4" placeholder="Search by username, product, status, etc...">
    <div class="table-responsive">
    <table id="ordersTable" class="table table-bordered align-middle">
    <thead class="table-dark">
        <tr>
            <th>Order ID</th>
            <th>User ID</th>
            <th>Username</th>
            <th>Address</th>
            <th>Product</th>
            <th>Photo</th>
            <th>Cost</th>
            <th>Quantity</th>
            <th>Date Ordered</th>
            <th>Date of Delivery</th>
            <th>Status</th>
            <th>Options</th>
        </tr>
    </thead>
    <tbody>
    <?php
        $view_query = mysqli_query($connections, "SELECT * FROM orders ORDER BY date_of_checkout DESC");
        while($row = mysqli_fetch_assoc($view_query)){
            $order_id = $row["order_id"];
            $user_id = $row["id"];
            $username = $row["username"];
            $address = $row["address"];
            $product_name = $row["product_name"];
            $photo_name = $row["photo_name"];
            $cost = $row["cost"];
            $quantity = $row["quantity"];
            $date_of_checkout = $row["date_of_checkout"];
            $date_of_delivery = $row["date_of_delivery"];
            $status = $row["status"];

            echo "<tr>
                <td>$order_id</td>
                <td>$user_id</td>
                <td>$username</td>
                <td>$address</td>
                <td>$product_name</td>
                <td><img src='../images/$photo_name' alt='' style='width:60px; height:60px; object-fit:contain;'></td>
                <td>₱".number_format($cost,2)."</td>
                <td>$quantity</td>
                <td>".date('M d, Y H:i', strtotime($date_of_checkout))."</td>
                <td>".date('M d, Y', strtotime($date_of_delivery))."</td>
                <td>
                    <span class='badge bg-".($status == 'Processing' ? 'warning' : ($status == 'Out for Delivery' ? 'info' : 'success'))."'>$status</span>
                </td>
                <td>
                    <button type='button' class='btn btn-primary btn-sm editStatusBtn' data-id='$order_id' data-status='$status'>Edit</button>
                    <form method='POST' action='' style='display:inline;' onsubmit=\"return confirm('Are you sure you want to delete this order?');\">
                        <input type='hidden' name='order_id' value='$order_id'>
                        <button type='submit' name='delete_order' class='btn btn-danger btn-sm ms-1'>
                            <i class='fa fa-trash'></i> Delete
                        </button>
                    </form>
                </td>   
            </tr>
            <tr id='edit-row-$order_id' style='display:none;'>
                <form method='POST' action=''>
                <input type='hidden' name='order_id' value='$order_id' />
                <td colspan='11'>
                    <div class='d-flex align-items-center gap-2 justify-content-end'>
                        <label class='me-2 text-dark'>Status:</label>
                        <select name='status' class='form-select w-auto'>
                            <option value='Processing' ".($status=='Processing'?'selected':'').">Processing</option>
                            <option value='Out for Delivery' ".($status=='Out for Delivery'?'selected':'').">Out for Delivery</option>
                            <option value='Delivered' ".($status=='Delivered'?'selected':'').">Delivered</option>
                        </select>
                        <button type='submit' name='save_status' class='btn btn-success btn-sm ms-2'>Save</button>
                        <button type='button' class='btn btn-secondary btn-sm cancelEditBtn' data-id='$order_id'>Cancel</button>
                    </div
                </td>
                </form>
            </tr>";
        }
    ?>
    </tbody>
    </table>
    </div>
    </center>
    <br><br><br>
        <script>
            document.addEventListener("DOMContentLoaded", function () {
                const searchInput = document.getElementById("searchInput");
                const table = document.getElementById("ordersTable");
                if (!searchInput || !table) return;

                searchInput.addEventListener("keyup", function () {
                    const filter = this.value.toLowerCase();
                    const rows = table.querySelectorAll("tbody tr:not([id^='edit-row-'])");
                    rows.forEach(row => {
                        const rowText = row.textContent.toLowerCase();
                        row.style.display = rowText.includes(filter) ? "" : "none";
                    });
                    // Optionally hide all edit rows when searching
                    table.querySelectorAll("tr[id^='edit-row-']").forEach(editRow => {
                        editRow.style.display = "none";
                    });
                });
            });

            document.addEventListener("DOMContentLoaded", function () {
                // Edit button: show the edit row for this order, hide others
                document.querySelectorAll('.editStatusBtn').forEach(btn => {
                    btn.addEventListener('click', function() {
                        // Hide all edit rows first
                        document.querySelectorAll("tr[id^='edit-row-']").forEach(row => row.style.display = "none");
                        // Show the edit row for this order
                        var id = this.getAttribute('data-id');
                        var editRow = document.getElementById('edit-row-' + id);
                        if (editRow) editRow.style.display = '';
                    });
                });

                // Cancel button: hide the edit row for this order
                document.querySelectorAll('.cancelEditBtn').forEach(btn => {
                    btn.addEventListener('click', function() {
                        var id = this.getAttribute('data-id');
                        var editRow = document.getElementById('edit-row-' + id);
                        if (editRow) editRow.style.display = "none";
                    });
                });

                // Search function (already present)
                const searchInput = document.getElementById("searchInput");
                const table = document.getElementById("ordersTable");
                if (!searchInput || !table) return;

                searchInput.addEventListener("keyup", function () {
                    const filter = this.value.toLowerCase();
                    const rows = table.querySelectorAll("tbody tr:not([id^='edit-row-'])");
                    rows.forEach(row => {
                        const rowText = row.textContent.toLowerCase();
                        row.style.display = rowText.includes(filter) ? "" : "none";
                    });
                    // Hide all edit rows when searching
                    table.querySelectorAll("tr[id^='edit-row-']").forEach(editRow => {
                        editRow.style.display = "none";
                    });
                });
            });
            </script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>