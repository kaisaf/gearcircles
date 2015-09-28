$(document).ready(function() {

  window.gcGetPosition();

  $("#map").on("click", ".infoWindow", function() {
    console.log("got a click");
    console.log($(this).data());
    window.location.href="/products/" + $(this).data().gearid
  })

  $("#choiceMenu").on("click", "#btnCategory", function() {
    if ($("#priceMenu").is(":visible")) {
      $("#priceMenu").slideToggle("easy", function() {
        $("#categoryMenu").slideToggle("easy");
      });
    } else {
      $("#categoryMenu").slideToggle("easy");
    }
  })

  $("#choiceMenu").on("click", "#btnPrice", function() {
    if ($("#categoryMenu").is(":visible")) {
      $("#categoryMenu").slideToggle("easy", function() {
        $("#priceMenu").slideToggle("easy");
      });
    } else {
      $("#priceMenu").slideToggle("easy");
    }
  })

  getApiData("/api/v1/locations", setMarkers);
  getApiData("/api/v1/categories", createMenu);

  function getApiData(endpoint, callback) {
    $.ajax({
      method: "GET",
      url: endpoint,
    }).done(function(data) {
      callback(data);
    })
  }

  function createMenu(categories) {
    console.log("kukkuu")
    console.log(categories)
    $("#categoryMenu").empty();
    $.each(categories, function(index, category) {
      $("#categoryMenu").append("<li> \
        <a href=#>" + category.name + "</a></li>")
    })
  }

  function setMarkers(locations) {
    $.each(locations, function(index, location) {
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
    var content = "<div class='infoWindow' data-gearId=" + location.gear_set[0].id + "> \
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
