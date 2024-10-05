// detection/static/detection/scripts.js
function openCamera() {
    // Show the video container and start the video feed
    document.getElementById("video-container").style.display = "block";
    document.getElementById("videoStream").src = "/detection/video_feed/";

    // Show the 'Close Camera' button and hide the 'Open Camera' button
    document.getElementById("openCamera").style.display = "none";
    document.getElementById("closeCamera").style.display = "inline";
}

function closeCamera() {
    // Hide the video container and stop the video feed
    document.getElementById("video-container").style.display = "none";
    document.getElementById("videoStream").src = "";

    // Show the 'Open Camera' button and hide the 'Close Camera' button
    document.getElementById("openCamera").style.display = "inline";
    document.getElementById("closeCamera").style.display = "none";
}




