$(document).ready(function() {

  window.gcGetPosition();

  $.ajax({
    method: "GET",
    url: "/api/v1/locations",
  }).done(function(data) {
    setMarkers(data);
  })

  $.ajax({
    method: "GET",
    url: "/api/v1/categories",
  }).done(function(data) {
    //console.log(data);
  })

  function setMarkers(locations) {
    $.each(locations, function(index, location) {
      // console.log(location.gear_set[0].description);
      // console.log(location.gear_set[0].name);
      // console.log(location.gear_set[0].price);
      position = {
        "coords": {
          "latitude": location.point.coordinates[1],
          "longitude": location.point.coordinates[0]
        }
      }
      window.gcAddMarker(position, window.gcMap, createMapInfoContent(location));
    })
  }

  function createMapInfoContent(location) {
    console.log(location);
    var content = "<div data-gearId=" + location.gear_set[0].id + "> \
      <div> \
        <img width=128px height=128px src=" + location.gear_set[0].gearimage_set[0].photo + "> \
      </div> \
      <div> \
        <h3>" + location.gear_set[0].name + "</h3> \
        <h4>" + location.gear_set[0].description + "</h4> \
        <h4>" + location.gear_set[0].price + "</h4> \
      </div> \
    </div>"
    return content;
  }

})
