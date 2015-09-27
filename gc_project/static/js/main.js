$(document).ready(function() {

  window.gcGetPosition()

  $.ajax({
    method: "GET",
    url: "/api/v1/locations",
  }).done(function(data) {
    setMarkers(data.features)
  })

  function setMarkers(locations) {
    $.each(locations, function(index, location) {
      position = {
        "coords": {
          "latitude": location.geometry.coordinates[1],
          "longitude": location.geometry.coordinates[0]
        }
      }
      window.gcAddMarker(position, window.gcMap)
    })
  }

})
