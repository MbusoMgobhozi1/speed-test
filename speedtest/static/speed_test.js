async function startSpeedTest() {
    const startTestElement = document.getElementById('start_test');
    const downloadSpeedElement = document.getElementById('download-speed');
    const uploadSpeedElement = document.getElementById('upload-speed');

    startTestElement.innerText = "Testing...";

    // Call the Django API endpoint
    const response = await fetch('/speedtest');
    const data = await response.json();

    if (data.error) {
        alert(data.error);
        startTestElement.innerText = "START";
        return;
    }

    // Update UI with results
    downloadSpeedElement.innerText = `${data.download_speeds} Mbps`;
    uploadSpeedElement.innerText = `${data.upload_speeds} Mbps`;
    startTestElement.innerText = "DONE";
}

document.querySelector('.speedometer').addEventListener('click', startSpeedTest);
