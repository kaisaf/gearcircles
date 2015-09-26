$(document).ready(function() {

  function initMap() {
    // Create a map object and specify the DOM element for display.
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 39.828175, lng: -98.5795},
      scrollwheel: false,
      zoom: 5
    });
  }

  initMap();

})
