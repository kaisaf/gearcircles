$(document).ready(function() {

  $("#cards").hide();

  window.gcCreateMap(function() {
    getApiData("/api/v1/locations", queryFilter, setMarkers);
  });

  var queryFilter = {"categories":[]}

  /*
  EVENT HANDLERS
  */

  $("#switchView").on("change", function() {
    if (this.checked) {
      $("#cards").show();
      $("#map").hide();
    } else {
      $("#map").show();
      $("#cards").hide();
    }
  })

  $("#map").on("click", ".infoWindow", function() {
    window.location.href="/gear/" + $(this).data().gearid
  })

  $("#cards").on("click", ".card", function() {
    window.location.href="/gear/" + $(this).data().gearid
  })

  $("#choiceMenu").on("click", ".btnChoiceMenuItem", function() {
    var isEmpty = true
    var $activePanel = $("#"+$(this).data().panelid)
    $.each($(".pnlChoiceMenu"), function(index, panel) {
      if ($(panel).is(":visible")) {
        isEmpty = false
        if ($activePanel.data() == $(panel).data()) {
          $(panel).slideToggle("easy")
        } else {
          $(panel).slideToggle("easy", function() {
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
    $.each($(".pnlChoiceMenu"), function(index, panel) {
      if ($(panel).is(":visible")) {
        $(panel).slideToggle("easy");
      }
    })
    var startDate = $("#startDate").val();
    var endDate = $("#endDate").val();
    var minPrice = $("#minPrice").val();
    var maxPrice = $("#maxPrice").val();
    var txtSearch = $("#txtSearch").val();
    queryFilter["startDate"] = startDate;
    queryFilter["endDate"] = endDate;
    queryFilter["minPrice"] = minPrice;
    queryFilter["maxPrice"] = maxPrice;
    queryFilter["txtSearch"] = txtSearch;
    //getApiData("/api/v1/locations", queryFilter, setMarkers);
    getApiData("/api/v1/locations", queryFilter, function(locations) {
      setMarkers(locations);
      createCards(locations);
    });
  })


  /*
  GET DATA ON PAGE LOAD
  */
  // getApiData("/api/v1/locations", queryFilter, setMarkers);
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
      window.gcAddMarker(position, createMapInfoContent(location));
    })
  }

  function createCards(locations) {
    $("#cards").empty();
    $.each(locations, function(index, location) {
      var card = "<div class='card col-md-3 col-sx-6' data-gearId=" + location.gear_set[0].id + "> \
        <img width=128px height=128px src=" + location.gear_set[0].gearimage_set[0].photo + "> \
        <h4>" + location.gear_set[0].name + "</h4> \
        <p>" + location.gear_set[0].description + "</p> \
        <h4> $" + location.gear_set[0].price + "</h4> \
      </div>"
      $("#cards").append(card);
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
        <h4> $" + location.gear_set[0].price + "</h4> \
      </div> \
    </div>"
    return content;
  }

  function catMenuItemHandler(obj) {
    //window.gcClearAllMarkers()
    if ($(obj).hasClass("selectedCat")) {
      $(obj).removeClass("selectedCat");
      var index = queryFilter["categories"].indexOf($(obj).data().catid);
      if (index == 0) {
        queryFilter["categories"].splice(index, index+1)
      }
      queryFilter["categories"].splice(index, index)
    } else {
      $(obj).addClass("selectedCat");
      queryFilter["categories"].push($(obj).data().catid);
    }
  }

})
