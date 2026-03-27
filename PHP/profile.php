<?php
// 1. Get the ID from the URL (provided by the .htaccess rewrite)
$fsid = $_GET['id'] ?? null;

if (!$fsid) {
    die("Oops! The service cannot process this Flipnote Studio ID!");
}

// 2. Load your User Database (users.json)
$database_path = "database/users.json"; // Adjust this to your actual path
if (file_exists($database_path)) {
    $users = json_decode(file_get_contents($database_path), true);
} else {
    $users = [];
}

// 3. Find the specific user
if (isset($users[$fsid])) {
    $userData = $users[$fsid];
    $username = $userData['nickname'];
    $stars = $userData['stars'] ?? 0;
    $bio = $userData['bio'] ?? "Welcome to the Jeraldmemo Flipnote service!";
} else {
    // Fallback if the user doesn't exist in your JSON yet
    $username = "Jeraldmemo User";
    $stars = 0;
    $bio = "This user hasn't set up their Jeraldmemo profile yet.";
}

// 4. Load your HTML Template (profile.htm)
// We use 'include' so that the HTML can access the $username and $fsid variables
include('profile.htm');
?>
