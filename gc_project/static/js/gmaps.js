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
      zoom: 6
  });
  google.maps.event.addListenerOnce(gcMap, 'tilesloaded', function() {
    gcOnMapReady(callback);
  });
}


function gcAddMarker(position, content) {
  var marker = new google.maps.Marker({
      position: convertCoords(position),
      map: gcMap,
      title: "I'm here!"
  });

  if (content) {
    var contentString = content;

    var infowindow = new google.maps.InfoWindow({
     content: contentString
    });

    marker.addListener('click', function() {
      infowindow.open(map, marker);
    });
  }
  markers.push(marker);
}

function gcClearAllMarkers() {
  console.log("clear markers")
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(null);
  }
}
