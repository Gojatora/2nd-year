<?php 
    include('../connections.php'); 
?>

<?php
    $error = "";

    // Handle form submission
    if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["add_product"])) {
        $product_name = trim($_POST["product_name"]);
        $category = $_POST["category"];
        $sub_category = $_POST["sub_category"];
        $description = trim($_POST["description"]);
        $cost = $_POST["cost"];
        $quantity = $_POST["quantity"];
        $photo_name = "";

        // Check for missing inputs
        if (
            empty($product_name) ||
            empty($category) ||
            empty($sub_category) ||
            empty($description) ||
            empty($cost) ||
            empty($quantity) ||
            !isset($_FILES['image']) || $_FILES['image']['error'] != 0
        ) {
            $error = "Please fill in all fields and upload a valid image.";
        } else {
            // Handle image upload
            $photo_name = $_FILES['image']['name'];
            $tempname = $_FILES['image']['tmp_name'];
            $folder = '../images/' . $photo_name;

            $allowed_extensions = ['jpg', 'jpeg', 'png'];
            $file_extension = pathinfo($photo_name, PATHINFO_EXTENSION);

            if (!in_array(strtolower($file_extension), $allowed_extensions)) {
                $error = "Only JPG, JPEG, and PNG files are allowed!";
            } else {
                move_uploaded_file($tempname, $folder);

                // Insert into database
                $query = "INSERT INTO products (product_name, category, sub_category, description, photo_name, cost, quantity) VALUES (
                    '$product_name', '$category', '$sub_category', '$description', '$photo_name', '$cost', '$quantity'
                )";
                if (mysqli_query($connections, $query)) {
                    echo "<script>alert('Product added successfully!'); window.location.href='products.php';</script>";
                    exit;
                } else {
                    $error = "Failed to add product!";
                }
            }
        }
    }
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
    <div class="add-product-container">
        <div class="add-product-card" id="add-only">
            <h2><i class="fa fa-plus-circle"></i> Add New Product</h2>
            <?php if (!empty($error)): ?>
                <div class="alert alert-danger text-center mb-3"><?php echo $error; ?></div>
            <?php endif; ?>
            <form method="POST" action="add_product.php" enctype="multipart/form-data" autocomplete="off">
                <div class="mb-3">
                    <label for="product_name" class="form-label">Product Name</label>
                    <input class="form-control" type="text" name="product_name" id="product_name" required>
                </div>
                <div class="mb-3">
                    <label for="category" class="form-label">Category</label>
                    <select class="form-control" name="category" id="categorySelect" required>
                        <option value="" disabled selected>Select Category</option>
                        <option value="PC Components">PC Components</option>
                        <option value="Peripherals">Peripherals</option>
                        <option value="Desktops">Desktops</option>
                        <option value="Laptops">Laptops</option>
                    </select>
                </div>
                <div class="mb-3">
                    <label for="sub_category" class="form-label">Sub-Category</label>
                    <select class="form-control" name="sub_category" id="subCategorySelect" required>
                        <option value="" disabled selected>Select Sub-Category</option>
                        <!-- Options will be populated by JS -->
                    </select>
                </div>
                <div class="mb-3">
                    <label for="description" class="form-label">Description</label>
                    <textarea class="form-control" name="description" id="description" rows="4" required></textarea>
                </div>
                <div class="mb-3">
                    <label for="image" class="form-label">Image</label>
                    <input class="form-control" type="file" name="image" id="image" accept="image/*" required>
                </div>
                <div class="mb-3">
                    <label for="cost" class="form-label">Cost (₱)</label>
                    <input class="form-control" type="number" name="cost" id="cost" min="0" step="0.01" required value="0">
                </div>
                <div class="mb-3">
                    <label for="quantity" class="form-label">Quantity</label>
                    <input class="form-control" type="number" name="quantity" id="quantity" min="0" required value="0">
                </div>
                <div class="btn-row">
                    <button class="btn btn-primary" type="submit" name="add_product">Add Product</button>
                    <a href="products.php" class="btn btn-secondary">Cancel</a>
                </div>
            </form>
        </div>
    </div>

    <script type="text/javascript" src="../plugin.js"></script>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>