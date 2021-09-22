// Initialize and add the map
function initMap() {
  // The map, centered at Uluru
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 18,
    center: lat_longs[0],
  });
  // The marker, positioned at Uluru
  for (let step = 0; step < lat_longs.length; step++) {
    const marker = new google.maps.Marker({
      position: lat_longs[step],
      map: map,
    });
  }
}