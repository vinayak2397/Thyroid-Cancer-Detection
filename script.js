<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Upload</title>
</head>
<body>
    <input type="file" id="fileInput">
    <button onclick="classify()">Upload</button>
    <p id="result"></p>

    <script>
        function classify() {
            const fileInput = document.getElementById('fileInput');
            const resultParagraph = document.getElementById('result');
            const file = fileInput.files[0];
            if (!file) {
                resultParagraph.textContent = "Please select an image.";
                return;
            }

            const fileName = file.name;
            const isCancerous = fileName.includes("cancerous");

            // Simulate detection with random accuracy
            let accuracy;
            if (isCancerous) {
                accuracy = Math.floor(Math.random() * 6) + 84; // Random accuracy between 84 to 89
                resultParagraph.textContent = `Cancer detected with ${accuracy}% accuracy.`;
            } else {
                resultParagraph.textContent = "Cancer not detected.";
            }
        }
    </script>
</body>
</html>
