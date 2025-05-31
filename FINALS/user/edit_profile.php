<?php
include('../connections.php');

// Handle logout before anything else
if (isset($_POST["logout"])) {
    session_unset();
    session_destroy();
    header("Location: ../index.php");
    exit;
}

$user_id = $_SESSION['user_id'];

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $address = $_POST['address'];
    $contact = $_POST['contact'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $current_password = $_POST['current_password'];

    // Get current password from DB
    $stmt = $connections->prepare("SELECT password FROM profiles WHERE id=?");
    $stmt->bind_param("i", $user_id);
    $stmt->execute();
    $stmt->bind_result($db_password);
    $stmt->fetch();
    $stmt->close();

    if ($current_password !== $db_password) {
        echo "<script>
            alert('Incorrect current password. Changes not saved.');
            window.location.href = 'edit_profile.php';
        </script>";
        exit();
    }

    // If new password is blank, keep the old one
    if (trim($password) === "") {
        $password = $db_password;
    }

    $stmt = $connections->prepare("UPDATE profiles SET username=?, address=?, contact=?, email=?, password=? WHERE id=?");
    $stmt->bind_param("sssssi", $username, $address, $contact, $email, $password, $user_id);
    $stmt->execute();
    $stmt->close();

    echo "<script>
        alert('Your profile has been updated!');
        window.location.href = 'index.php';
    </script>";
    exit();
}


// Fetch user data to show in form
$stmt = $connections->prepare("SELECT username, address, contact, email FROM profiles WHERE id=?");
$stmt->bind_param("i", $user_id);
$stmt->execute();
$stmt->bind_result($username, $address, $contact, $email);
$stmt->fetch();
$stmt->close();
?>



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Edit Profile</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <?php include('nav.php'); ?>

    <div style="display: flex; justify-content: center; align-items: center; min-height: 100vh; margin-top: 50px; flex-direction: column;">
        <div class="form-container">
            <h2>Edit Profile</h2>
            <?php if (!empty($success)) echo "<p style='color:lightgreen; text-align:center;'>$success</p>"; ?>
		<form class="form" method="POST" action="edit_profile.php">
			<div class="input-group">
				<label>Username</label>
				<input type="text" name="username" value="<?php echo htmlspecialchars($username); ?>" required>
			</div>
			<div class="input-group">
				<label>Address</label>
				<input type="text" name="address" value="<?php echo htmlspecialchars($address); ?>" required>
			</div>
			<div class="input-group">
				<label>Contact</label>
				<input type="text" name="contact" value="<?php echo htmlspecialchars($contact); ?>" required>
			</div>
			<div class="input-group">
				<label>Email</label>
				<input type="email" name="email" value="<?php echo htmlspecialchars($email); ?>" required>
			</div>
			<div class="input-group">
				<label>Current Password</label>
				<input type="password" name="current_password" required>
			</div>
			<div class="input-group">
				<label>New Password</label>
				<input type="password" name="password" placeholder="Leave blank to keep current">
			</div>
			<div style="display: flex; gap: 10px; justify-content: center; margin-top: 20px;">
				<button type="submit" class="sign">Save Changes</button>
				<a href="index.php" class="btn btn-secondary">Cancel</a>
			</div>
		</form>

    </div>

    <?php include('footer.php'); ?>
	
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
