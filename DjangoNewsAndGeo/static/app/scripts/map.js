document.addEventListener('DOMContentLoaded', function () {
    const latitude = document.getElementById('id_latitude');
    const longitude = document.getElementById('id_longitude');
    let coords, timer, map, point;
    function updateFields() {
        latitude.value = coords[0].toFixed(8);
        longitude.value = coords[1].toFixed(8);
        point.geometry.setCoordinates(coords);
    }

    ymaps.ready(() => {
        map = new ymaps.Map("map", {
            center: [latitude.value, longitude.value],
            zoom: 12,
            controls: ['zoomControl']
        });
        map.cursors.push('arrow');
        point = new ymaps.Placemark(map.getCenter(), {}, {
            draggable: true
        });
        map.geoObjects.add(point);
        map.events.add('click', (e) => {
            coords = e.get('coords');
            updateFields();
        });
        point.events.add('dragend', (e) => {
            coords = e.originalEvent.target.geometry.getCoordinates();
            updateFields();
        });
    });
    [latitude, longitude].forEach(c => {
        c.addEventListener('input', (e) => {
            clearTimeout(timer);
            timer = setTimeout(() => {
                coords = [latitude.value, longitude.value];
                map.setCenter(coords, 12);
                point.geometry.setCoordinates(coords);
            }, 5000);
        });
    });
});