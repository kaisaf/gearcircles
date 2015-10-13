$(document).ready(function() {

window.gcCreateMap(createLocations);

  // function getLocations() {
  //   $.ajax({
  //     method: "GET",
  //     url: "/api/v1/locations/",
  //   }).done(function(data) {
  //     setMarkers(data);
  //   })
  // }

  function createLocations(position) {
    var locations = []
    for (i = 0; i < 10; i++) {
      place1 = {
        "point": {
          "coordinates": [position.coords.longitude + Math.random()/10, position.coords.latitude + Math.random()/10]
        }
      }
      locations.push(place1);
      place2 = {
        "point": {
          "coordinates": [position.coords.longitude - Math.random()/10, position.coords.latitude - Math.random()/10]
        }
      }
      locations.push(place2);
      place3 = {
        "point": {
          "coordinates": [position.coords.longitude + Math.random()/10, position.coords.latitude - Math.random()/10]
        }
      }
      locations.push(place3);
      place4 = {
        "point": {
          "coordinates": [position.coords.longitude - Math.random()/10, position.coords.latitude + Math.random()/10]
        }
      }
      locations.push(place4);
    }
    setMarkers(locations);
  }

  function setMarkers(locations) {
    $.each(locations, function(index, location) {
      position = {
        "coords": {
          "latitude": location.point.coordinates[1],
          "longitude": location.point.coordinates[0]
        }
      }
      content = null;
      window.gcAddMarker(position, content, index);
    })
  }

})
