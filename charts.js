// Create System Usage Chart
function createSystemChart(cpu, memory, disk) {

    const ctx = document.getElementById('systemChart').getContext('2d');

    new Chart(ctx, {
        type: 'bar',

        data: {
            labels: ['CPU', 'Memory', 'Disk'],

            datasets: [{
                label: 'Usage %',

                data: [cpu, memory, disk],

                backgroundColor: [
                    'rgba(13, 110, 253, 0.7)',
                    'rgba(25, 135, 84, 0.7)',
                    'rgba(220, 53, 69, 0.7)'
                ],

                borderColor: [
                    'rgba(13, 110, 253, 1)',
                    'rgba(25, 135, 84, 1)',
                    'rgba(220, 53, 69, 1)'
                ],

                borderWidth: 2
            }]
        },

        options: {
            responsive: true,

            plugins: {
                legend: {
                    display: true
                }
            },

            scales: {
                y: {
                    beginAtZero: true,
                    max: 100
                }
            }
        }
    });
}


// Alert Popup
function showAlert(message) {
    alert(message);
}


// Validate IP Address
function validateIP(ip) {

    const pattern =
        /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;

    return pattern.test(ip);
}


// Validate Scan Form
function scanValidation() {

    const target = document.getElementById('target').value;

    if (!validateIP(target)) {

        alert('Invalid IP Address');

        return false;
    }

    return true;
}


// Live Clock
function updateClock() {

    const now = new Date();

    const clock = document.getElementById('clock');

    if (clock) {
        clock.innerHTML = now.toLocaleTimeString();
    }
}


// Update every second
setInterval(updateClock, 1000);