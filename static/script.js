document.getElementById('routeForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const source = document.getElementById('source').value;
    const destination = document.getElementById('destination').value;
    const transport = document.getElementById('transport').value;
    const priority = document.getElementById('priority').value;

    fetch('/find_route', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ source, destination, transport, priority }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = 
            `Path: ${data.path}\n` +
            (data.distance ? `Distance: ${data.distance} km\n` : '') +
            (data.time ? `Time: ${data.time.toFixed(2)} minutes\n` : '') +
            (data.cost ? `Cost: Rs. ${data.cost.toFixed(2)}\n` : '');
    })
    .catch(error => {
        document.getElementById('result').innerText = 'Error finding route!';
    });
});
