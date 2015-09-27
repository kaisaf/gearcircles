$(document).ready(function() {

  window.gcGetPosition();

  $.ajax({
    method: "GET",
    url: "/api/v1/locations",
  }).done(function(data) {
    setMarkers(data);
  })

  function setMarkers(locations) {
    $.each(locations, function(index, location) {
      position = {
        "coords": {
          "latitude": location.point.coordinates[1],
          "longitude": location.point.coordinates[0]
        }
      }
      window.gcAddMarker(position, window.gcMap);
    })
  }

})
