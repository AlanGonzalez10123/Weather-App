// Function to get the user's current location
function getLocation() {
    if (navigator.geolocation) {
        // If geolocation is supported by the browser, get the current position
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        // If geolocation is not supported, show an alert
        alert("Geolocation is not supported by this browser.");
    }
}

// Function to handle the successful retrieval of the user's position
function showPosition(position) {
    const lat = position.coords.latitude; // Get the latitude from the position object
    const lon = position.coords.longitude; // Get the longitude from the position object

    // Make a fetch request to the OpenWeatherMap API to get the weather data for the user's location
    fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}&units=imperial`)
        .then(response => response.json()) // Convert the response to JSON
        .then(data => {
            console.log(data); // Log the weather data to the console
            const city = data.name; // Get the name of the city from the weather data
            document.getElementById('city').value = city; // Set the value of the 'city' input field to the city name
            document.getElementById('location-form').submit(); // Submit the form
        })
        .catch(error => {
            console.error('Error getting city:', error); // Log an error message to the console
            alert('Could not determine city from your location.'); // Show an alert to the user
        });
}

// Function to handle errors that occur during geolocation
function showError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
            alert("User denied the request for Geolocation."); // Show an alert to the user
            break;
        case error.POSITION_UNAVAILABLE:
            alert("Location information is unavailable."); // Show an alert to the user
            break;
        case error.TIMEOUT:
            alert("The request to get user location timed out."); // Show an alert to the user
            break;
        case error.UNKNOWN_ERROR:
            alert("An unknown error occurred."); // Show an alert to the user
            break;
    }
}
