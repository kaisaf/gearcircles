$(document).ready(function() {

  window.gcGetPosition();

  var categoriesQuery = {"categories":[]}

  /*
  EVENT HANDLERS
  */
  $("#map").on("click", ".infoWindow", function() {
    console.log("got a click");
    console.log($(this).data());
    window.location.href="/products/" + $(this).data().gearid
  })

  $("#choiceMenu").on("click", ".btnChoiceMenuItem", function() {
    var isEmpty = true
    var $activePanel = $("#"+$(this).data().panelid)
    $.each($(".pnlChoiceMenu"), function(index, panel) {
      if ($(panel).is(":visible")) {
        isEmpty = false
        if ($activePanel.data() == $(panel).data()) {
          $(panel).slideToggle("slow")
        } else {
          $(panel).slideToggle("slow", function() {
            $activePanel.slideToggle("easy");
          });
        }
      }
    })
    if (isEmpty) {
      $activePanel.slideToggle("easy");
    }
  })


  $("#categoryMenu").on("click", ".catMenuItem", function() {
    catMenuItemHandler(this);
  })

  $("#btnSearch").on("click", function() {
    window.gcClearAllMarkers();
    if ($("#priceMenu").is(":visible")) {
      $("#priceMenu").slideToggle();
    } else if ($("#categoryMenu").is(":visible")) {
      $("#categoryMenu").slideToggle();
    }
    getApiData("/api/v1/locations", categoriesQuery, setMarkers);
  })


  /*
  GET DATA ON PAGE LOAD
  */
  getApiData("/api/v1/locations", categoriesQuery, setMarkers);
  getApiData("/api/v1/categories", null, createMenu);

  /*
  RUNS AJAX CALL TO ENDPOINT PARAMETER AND CALLBACK PARAMETER ON SUCCESS
  */
  function getApiData(endpoint, data, callback) {
    $.ajax({
      method: "GET",
      url: endpoint,
      data: data,
    }).done(function(data) {
      callback(data);
    })
  }

  function createMenu(categories) {
    $("#categoryMenu").empty();
    $.each(categories, function(index, category) {
      $("#categoryMenu").append("<li class='catMenuItem' data-catId=" + category.id + "> \
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

  function catMenuItemHandler(obj) {
    //window.gcClearAllMarkers()
    if ($(obj).hasClass("selectedCat")) {
      $(obj).removeClass("selectedCat");
      var index = categoriesQuery["categories"].indexOf($(obj).data().catid);
      if (index == 0) {
        categoriesQuery["categories"].splice(index, index+1)
      }
      categoriesQuery["categories"].splice(index, index)
    } else {
      $(obj).addClass("selectedCat");
      categoriesQuery["categories"].push($(obj).data().catid);
    }
    console.log(categoriesQuery["categories"])
  }

})
