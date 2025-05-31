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
     
    <<div class="cart-container">
    <h1 style="text-align:center; margin: 30px 0 20px 0;">Shopping Cart</h1>
    <div class="listCart">
    <?php
        $view_query = mysqli_query($connections, "SELECT * FROM cart WHERE id='$_SESSION[user_id]'");
        $cart_items = [];
        $total = 0;
        while($row = mysqli_fetch_assoc($view_query)){
            $cart_items[] = $row;
        }
        if (empty($cart_items)) {
            echo '
            <div class="empty-cart text-center py-5">
                <img src="../images/emptycart.png" alt="Empty Cart" class="mb-4">
                <h2 class="mb-3">Your Cart is <span class="text-danger">Empty!</span></h2>
                <p class="mb-4 text-muted">
                    Must add items to the cart before you proceed to check out.
                </p>
                <a href="index.php" class="btn btn-primary">
                    RETURN HOME
                </a>
            </div>';
        } else {
            echo '
                <div class="cart-headers">
                    <div style="padding-left: 10px;">Product</div>
                    <div class="price-column">Price</div>
                    <div class="quantity-column">Quantity</div>
                    <div class="total-column">Total</div>
                    <div style="text-align:center;">Remove</div>
                </div>
                <div class="cart-items-container">';
            foreach ($cart_items as $row) {
                $product_id = $row["product_id"];
                $db_productname = $row["product_name"];
                $db_photoname = $row["photo_name"];
                $quantity = $row["quantity"];
                $db_cost = $row["cost"];
                $itemTotal = $db_cost * $quantity;
                $total += $itemTotal;
                echo '
                <div class="cart-item">
                    <div style="display: flex; align-items: center;">
                        <img src="../images/'.htmlspecialchars($db_photoname).'" alt="'.htmlspecialchars($db_productname).'" />
                        <span style="margin-left: 15px; font-weight: 600; color: #222;">'.htmlspecialchars($db_productname).'</span>
                    </div>
                    <div class="price-column">
                        ₱'.number_format($db_cost, 2).'
                    </div>
                    <div class="quantity-column">
                        <form method="post" action="update_cart_quantity.php" style="display:inline;">
                            <input type="hidden" name="product_id" value="'.$product_id.'">
                            <input type="number" name="quantity" value="'.$quantity.'" min="1" style="width:60px; text-align:center; border-radius:5px; border:1px solid #ccc;">
                            <button type="submit" class="btn btn-sm btn-primary" style="margin-left:5px;">Update</button>
                        </form>
                    </div>
                    <div class="total-column" style="font-weight: bold;">
                        ₱'.number_format($itemTotal, 2).'
                    </div>
                    <div style="text-align:center;">
                        <a href="delete_cart.php?product_id='.$product_id.'" style="color: #d32f2f;">
                            <i class="fa fa-trash"></i>
                        </a>
                    </div>
                </div>';
            }
            echo '
                </div>
                <div class="cart-summary">
                    <h3>Total: ₱'.number_format($total, 2).'</h3>
                    <div style="display: flex; justify-content: center; gap: 10px;">
                        <a href="checkout.php" class="checkout-btn">Proceed to Checkout</a>
                    </div>
                </div>';
        }
    ?>
    </div>
    <div style="display: flex; justify-content: center; margin-top: 20px;">
        <a href="orders.php" class="btn btn-outline-secondary">View My Orders</a>
    </div>
</div>
        
    
    <?php include('footer.php'); ?>

    <script type="text/javascript" src="../plugin.js"></script>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>