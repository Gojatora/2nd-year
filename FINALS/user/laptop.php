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
    <div class="main">

        <div class="btn-box">
            <div class="nav d-flex align-items-center justify-content-between" style="gap: 16px;">
                <div class="d-flex align-items-center" style="gap: 12px;">
                    <label for="filterDropdown" class="me-2 mb-0" style="font-weight:600; color:#171717;">Filter By</label>
                    <div class="filter-dropdown mb-3">
                        <select id="filterDropdown" class="form-select" style="max-width:260px;">
                            <option value="all" selected>Show All</option>
                        <option value="Intel">Intel</option>
                        <option value="AMD">AMD</option>
                        </select>
                    </div>
                </div>
                <div class="item" style="min-width:220px;">
                    <div class="search-box mb-3">
                        <input type="text" id="productSearch" class="form-control" placeholder="Search products...">
                    </div>
                </div>
            </div>
        </div>
        
        <div class="product-view">
        <?php
            $view_query = mysqli_query($connections, "SELECT * FROM products where category='Laptops'");
            while($row = mysqli_fetch_assoc($view_query)){
                    
                $product_id = $row["product_id"];
                $category = $row["category"];
                $sub_category = $row["sub_category"];
                $product_name = $row["product_name"];   
                $photoname = $row["photo_name"];
                $description = $row["description"];
                $cost = $row["cost"];
                $quantity = $row["quantity"];
            echo "
                <div class='cardproduct' data-name='$sub_category'>
                    <div class='image'>
                        <img src='../images/$photoname' alt=''>
                    </div>
                    <div class='namePrice'>
                        <h3 id='name'>$product_name</h3>
                        <span>₱ $cost</span>
                    </div>
                    <p class='product-description collapsed' id='desc-$product_id'>
                        <span class='short-description'>".substr($description, 0, 100)."...</span>
                        <span class='full-description' style='display:none;'>$description</span>
                    </p>
                    <button class='toggle-description'>View Detail</button>
                    <div style='display:flex; gap:10px; justify-content:center; margin-top:10px;'>
                        <a href='cart_actions.php?product_id=$product_id'>
                            <button type='button' class='btn btn-success btn-sm'>
                                <i class='fa fa-cart-plus'></i> Add to Cart
                            </button>
                        </a>
                    </div>
                </div>  ";
            }
        ?>
        </div> 
    </div>  
     
    
    <?php include('footer.php'); ?>

    <script type="text/javascript" src="../plugin.js"></script>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>