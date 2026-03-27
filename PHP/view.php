<?php
$fsid = $_GET['user']; // Captured from the URL
$fid  = $_GET['fid'];  // Captured from the URL

// Your real file path on Windows 10
$ppm_path = "uploads/" . $fid . ".ppm";

if (file_exists($ppm_path)) {
    // This is where you'll load your "Pixel Perfect" Frog Player
    $page_title = "Viewing Flipnote " . $fid . " by " . $fsid;
    include('ugoplayer_template.php');
} else {
    header("HTTP/1.0 404 Not Found");
    echo "This Flipnote doesn't exist on the Jeraldmemo Flipnote server!";
}
?>
