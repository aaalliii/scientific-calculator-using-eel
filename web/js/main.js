document.querySelectorAll('a').forEach(function(element) {
    element.addEventListener('click', function(event) {
        event.preventDefault();

        var elementId = element.id;

        eel.handleClick(elementId);
    });
});

eel.expose(updateDisplay);
function updateDisplay(value) {
    document.getElementById('display').value = value;
}
