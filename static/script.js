// Function to display a loading spinner
function showLoadingSpinner() {
    // Create a div element for the spinner
    var spinner = document.createElement("div");
    spinner.className = "spinner-border text-primary";
    spinner.setAttribute("role", "status");

    // Create a visually hidden span for screen readers
    var span = document.createElement("span");
    span.className = "visually-hidden";
    span.textContent = "Loading...";

    // Append the span to the spinner
    spinner.appendChild(span);

    // Append the spinner to the container
    var container = document.querySelector(".container");
    container.appendChild(spinner);
}
