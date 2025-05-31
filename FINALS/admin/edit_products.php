'<?php 
    include('../connections.php'); 
?>



<?php

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["save_product"])) {
    $product_id = $_POST["product_id"];
    $new_product_name = $_POST["new_product_name"];
    $new_category = $_POST["new_category"];
    $new_sub_category = $_POST["new_sub_category"];
    $new_description = $_POST["new_description"];
    $new_cost = $_POST["new_cost"];
    $new_quantity = $_POST["new_quantity"];

    // Get the current values from the database
    $result = mysqli_query($connections, "SELECT category, sub_category, photo_name FROM products WHERE product_id='$product_id'");
    $row = mysqli_fetch_assoc($result);
    $current_category = $row['category'];
    $current_sub_category = $row['sub_category'];
    $current_photo_name = $row['photo_name'];

    // Use current value if "unchanged" is selected
    if ($new_category == "unchanged") {
        $new_category = $current_category;
        $new_sub_category = $current_sub_category;
    }
    if ($new_sub_category == "") {
        $new_sub_category = $current_sub_category;
    }
    // Check if a new image is uploaded
    if (isset($_FILES['new_image']) && $_FILES['new_image']['error'] == 0) {
        $new_photo_name = $_FILES['new_image']['name'];
        $tempname = $_FILES['new_image']['tmp_name'];
        $folder = '../images/' . $new_photo_name;

        // Validate image file extension (allow only jpg, jpeg, png)
        $allowed_extensions = ['jpg', 'jpeg', 'png'];
        $file_extension = pathinfo($new_photo_name, PATHINFO_EXTENSION);

        if (!in_array(strtolower($file_extension), $allowed_extensions)) {
            echo "<script language='javascript'>alert('Only JPG, JPEG, and PNG files are allowed!')</script>";
            exit;
        }

        // Move the new image to the folder
        if (move_uploaded_file($tempname, $folder)) {
            // If a new image is uploaded, update the database with the new image
            mysqli_query($connections, "UPDATE products SET product_name='$new_product_name', category='$new_category', sub_category='$new_sub_category', description='$new_description', quantity='$new_quantity', photo_name='$new_photo_name', cost='$new_cost' WHERE product_id='$product_id'");

            echo "<script language='javascript'>alert('Product has been updated!')</script>";
            echo "<script>window.location.href='products.php?';</script>";
        } else {
            echo "<script language='javascript'>alert('Failed to upload new image!')</script>";
        }
    } else {
        // If no new image is uploaded, update without changing the photo (maintaining the old photo)
        mysqli_query($connections, "UPDATE products SET product_name='$new_product_name', category='$new_category', sub_category='$new_sub_category', description='$new_description', quantity='$new_quantity', cost='$new_cost' WHERE product_id='$product_id'");

        echo "<script language='javascript'>alert('Product has been updated!')</script>";
        echo "<script>window.location.href='products.php?';</script>";
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
    <br>
    <br>
    <br>
    <br>
    <center>
    <table>
    <thead>
        <tr class="header">
        <th scope="col">Current Product</th>
        <th scope="col">Edit</th>
        </tr>
    </thead>
    <tbody>
    <?php
        
        $product_id = $_REQUEST["product_id"];

        $view_query = mysqli_query($connections, "SELECT * FROM products WHERE product_id='$product_id'");


        while($row_edit = mysqli_fetch_assoc($view_query)){

            $db_product_name = $row_edit["product_name"];
            $db_category = $row_edit["category"];
            $db_sub_category = $row_edit["sub_category"];
            $db_photo_name = $row_edit["photo_name"];
            $db_description = $row_edit["description"];
            $db_cost = $row_edit["cost"];
            $db_quantity = $row_edit["quantity"];

        echo"
        
        <form method='POST' action='edit_products.php' enctype='multipart/form-data'>
    
        <input type='hidden' name='product_id' value=' $product_id '>

        <tr><td data-label='Product Name'>Product Name: $db_product_name</td><td><input class='editform' type='text' name='new_product_name' value='$db_product_name'></td></tr>
        <tr>
            <td data-label='Category'>Category: $db_category</td>
            <td>
                <select class='editform' name='new_category' id='categorySelect'>
                    <option value='unchanged' selected>Unchanged (<?php echo $db_category; ?>)</option>
                    <option value='PC Components'>PC Components</option>
                    <option value='Peripherals'>Peripherals</option>
                    <option value='Desktops'>Desktops</option>
                    <option value='Laptops'>Laptops</option>
                </select>
            </td>
        </tr>
        <tr>
            <td data-label='Sub-Category'>Sub-Category: $db_sub_category</td>
            <td>
                <select class='editform' name='new_sub_category' id='subCategorySelect'>
                    <option value='unchanged' selected>Unchanged (<?php echo $db_sub_category; ?>)</option>
                    <!-- Options will be populated by JavaScript -->
                </select>
            </td>
        </tr>
        <tr><td data-label='Product Name'>Product Name: $db_product_name</td><td><input class='editform' type='text' name='new_product_name' value='$db_product_name'></td></tr>
         <tr>
            <td data-label='Description'>Description: $db_description</td>
            <td>
                <textarea class='editform' id='description' name='new_description' rows='4' cols='40'>$db_description</textarea>
            </td>
        </tr>
         <tr><td data-label='Image'><img src='../images/$db_photo_name'></td><td><input class='editform' type='file' name='new_image'></td></tr>
         <tr><td data-label='Cost'>Cost: ₱$db_cost</td><td> <input class='editform' type='text' name='new_cost' value=' $db_cost '></td></tr>
         <tr><td data-label='Quantity'>Quantity: $db_quantity</td> <td><input class='editform' type='text' name='new_quantity' value=' $db_quantity'></td></tr>
         ";
        }
    ?>
    
    </tbody>
    </table>
    <br>
    <input class='btn btn-primary' name='save_product' type='submit' value='Update'>
    </form>
    
    <a href="products.php"><button class="btn btn-primary">Cancel</button><a>  
    </center>        
    <script>
        window.currentSubCategory = <?php echo json_encode($db_sub_category); ?>;
    </script>
    <script type="text/javascript" src="../plugin.js"></script>


    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>