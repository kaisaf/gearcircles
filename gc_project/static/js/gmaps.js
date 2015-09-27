$(document).ready(function() {
  window.gcGetPosition = function() {
    // Create a map object and specify the DOM element for display.
    defaultPos = {
      "coords": {
        "latitude": 40.7509862,
        "longitude": -73.986871
      }
    }
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showMap, function() {
        showMap(defaultPos);
      });
    } else {
      showMap(defaultPos);
    }
  }

  function convertCoords(position) {
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;
    return {lat: latitude, lng: longitude}
  }

  function showMap(position) {
    window.gcMap = new google.maps.Map(document.getElementById('map'), {
        center: convertCoords(position),
        scrollwheel: false,
        zoom: 6
    });
  }

  window.gcAddMarker = function(position, map, content) {
    var marker = new google.maps.Marker({
        position: convertCoords(position),
        map: map,
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

  }


})
