$(document).ready(function() {

  function getPosition() {
    // Create a map object and specify the DOM element for display.
    defaultPos = {
      "coords": {
        "latitude": 40.7509862,
        "longitude": -73.986871
      }
    }
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showMap, function() {
        showMap(defaultPos)
      });
    } else {
      showMap(defaultPos)
    }
  }

  function convertCoords(position) {
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;
    return {lat: latitude, lng: longitude}
  }

  function showMap(position) {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: convertCoords(position),
        scrollwheel: false,
        zoom: 6
    });
    addMArker(position, map)
    pos1 = {
      "coords": {
        "latitude": 40.7609862,
        "longitude": -73.996871
      }
    }
    pos2 = {
      "coords": {
        "latitude": 40.7519862,
        "longitude": -73.987871
      }
    }
    pos3 = {
      "coords": {
        "latitude": 40.7509062,
        "longitude": -73.956871
      }
    }
    addMArker(pos1, map, "text1")
    addMArker(pos2, map, "text2")
    addMArker(pos3, map, "text3")
  }

  function addMArker(position, map, content) {
    var marker = new google.maps.Marker({
        position: convertCoords(position),
        map: map,
        title: "I'm here!"
    });

    if (content) {
      var contentString = "<h3>"+ content +"</h3>"

      var infowindow = new google.maps.InfoWindow({
       content: contentString
      });

      marker.addListener('click', function() {
        infowindow.open(map, marker);
      });
    }

  }



    // var marker = new google.maps.Marker({
    //   position: {lat: 38.828175, lng: -97.5795},
    //   icon: "http://maps.google.com/mapfiles/ms/icons/green-dot.png",
    //   map: map,
    //   title: "I'm here!",
    // });


  getPosition();

})
