$(document).ready(function() {

window.gcCreateMap(function() {
  console.log("map done")
});

$("#frmCategorySelect").on("change", function() {
  getCategoryDetails($(this).val());
})

$("#frmAddress").on("change", function() {
  window.gcGetLocation($(this).val(), gcSetGeoLocation);
})

var today = new Date();
var expirationDate = new Date(today.setDate(today.getDate() + 90));
var year = expirationDate.getFullYear();
var month = ('0' + (expirationDate.getMonth() + 1)).slice(-2);
var date = ('0'+ expirationDate.getDate()).slice(-2);
expirationDate = year + "-" + month + "-" + date;
document.getElementById('frmDate').max = expirationDate

var gcSetGeoLocation = function(position) {
  window.gcClearAllMarkers();
  window.gcAddMarker(position);
  $("#frmLatitude").val(position.coords.latitude);
  $("#frmLongitude").val(position.coords.longitude);
}


function getCategoryDetails(catId) {
  var endpoint = "/api/v1/categories/" + catId
  $.ajax({
    method: "GET",
    url: endpoint,
  }).done(function(result) {
    $("#frm-elements-container").empty();
    createFormElements(result.categoryproperty_set);
  })
}

// function createFormElements(categoryProperties) {
//   $(categoryProperties).each(function(i, item) {
//     console.log(item)
//     var inputId = "frm" + item.id;
//     var htmlInput = '<div class="form-group"> \
//       <label for="' + inputId + '">' + item.name + '</label> \
//       <input ' + convertInputTypeAttr(item.input_type) +
//       ' class="form-control" id="' + inputId + '" name="' + inputId + '" placeholder="'+
//       item.description +'" ' + convertInputRequiredAttr(item.mandatory) +'> \
//     </div>'
//
//     $("#frm-elements-container").append(htmlInput);
//   })
// }


function createFormElements(categoryProperties) {
  $(categoryProperties).each(function(i, item) {
    console.log(item)
    var inputId = "frm" + item.id;
    var htmlInput = '<div class="form-group has-error has-feedback"> \
    <label for="' + inputId + '" class="control-label col-md-2">' + item.name +':</label> \
     <div class="col-md-6"> \
      <input ' + convertInputTypeAttr(item.input_type) +
      ' class="form-control" id="' + inputId + '" name="' + inputId + '" placeholder="'+
      item.description +'" ' + convertInputRequiredAttr(item.mandatory) +'> \
    <span class="glyphicon glyphicon-remove form-control-feedback"></span> \
    </div>'


    $("#frm-elements-container").append(htmlInput);
  })
}


function convertInputTypeAttr(input_type) {
  if (input_type==0) {
    return 'type="text"';
  } else if (input_type==1) {
    return 'type="number" step="1" min="0"';
  } else if (input_type==2) {
    return 'type="number" step="0.1" min="0"';
  }
}

function convertInputRequiredAttr(mandatory) {
  if (mandatory) {
    return "required";
  }
  return ''
}

})
