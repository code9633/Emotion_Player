// static/js/webcam.js
const video = document.getElementById('webcam-feed');
const captureButton = document.getElementById('capture-button');
const capturedImageInput = document.getElementById('captured-image');

// Access the webcam and display the feed
navigator.mediaDevices.getUserMedia({ video: true })
    .then(function (stream) {
        video.srcObject = stream;
    })
    .catch(function (error) {
        console.error('Error accessing webcam:', error);
    });

// Capture an image from the webcam and set it as the value of the hidden input
captureButton.addEventListener('click', function () {
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    capturedImageInput.value = canvas.toDataURL('image/jpeg');
});
