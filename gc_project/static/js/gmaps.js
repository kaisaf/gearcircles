var markers = [];
var gcMap = null;

function gcOnMapReady(callback) {
  callback();
}

function gcCreateMap(callback) {
  // Create a map object and specify the DOM element for display.
  defaultPos = {
    "coords": {
      "latitude": 40.7509862,
      "longitude": -73.986871
    }
  }
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function (param) {
      // ON SUCCESS
      showMap(param, callback)
    },function() {
      // USER BLOCKED LOCATION
      showMap(defaultPos, callback)
    });
  } else {
    // GEOLOCATION NOT SUPPORTED
    showMap(defaultPos, callback);
  }
}

function convertCoords(position) {
  var latitude = position.coords.latitude;
  var longitude = position.coords.longitude;
  return {lat: latitude, lng: longitude}
}

function showMap(position, callback) {
  gcMap = new google.maps.Map(document.getElementById('map'), {
      center: convertCoords(position),
      scrollwheel: false,
      zoom: 12
  });
  google.maps.event.addListenerOnce(gcMap, 'tilesloaded', function() {
    gcOnMapReady(callback);
  });
}


function gcAddMarker(position, content, index) {
  window.setTimeout(function() {
  var marker = new google.maps.Marker({
      position: convertCoords(position),
      map: gcMap,
      title: "I'm here!",
      animation: google.maps.Animation.DROP
  });

  (function (marker, content) {
                google.maps.event.addListener(marker, "click", function (e) {
                    infoWindow.setContent(content);
                    infoWindow.open(gcMap, marker);
                });
            })(marker, content);

    markers.push(marker);
  }, (100*index));
}

var infoWindow = new google.maps.InfoWindow();

function gcClearAllMarkers() {
  console.log("clear markers")
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(null);
  }
}

function gcGetLocation(address, callback) {
  var geocoder = new google.maps.Geocoder();
  geocoder.geocode({'address': address}, function(results, status) {
    if (status === google.maps.GeocoderStatus.OK) {
      gcMap.setCenter(results[0].geometry.location);

      // new location to be stored for the gear:
      var new_lat = results[0].geometry.location.lat();
      var new_lgn = results[0].geometry.location.lng();

      pos = {
        "coords": {
          "latitude": new_lat,
          "longitude": new_lgn
        }
      }
      console.log(pos)
      callback(pos);

    } else {
      alert('Geocode was not successful for the following reason: ' + status);
    }

  });
}
