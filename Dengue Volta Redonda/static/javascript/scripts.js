document.addEventListener('DOMContentLoaded', () => {

    var map = L.map('map').setView([-22.5205, -44.1017], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    var coordinates = [-22.5205, -44.1017];

    // noinspection JSUnusedLocalSymbols
    var marker = L.marker(coordinates).addTo(map)
        .bindPopup('Volta Redonda, Rio de Janeiro')
        .openPopup();
});