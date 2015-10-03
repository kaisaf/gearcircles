$(document).ready(function() {

$("#frm-category-select").on("change", function() {
  getCategoryDetails($(this).val());
})

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

function createFormElements(categoryProperties) {
  $(categoryProperties).each(function(i, item) {
    console.log(item)
    var htmlInput = '<div class="form-group"> \
      <label for="exampleInputEmail1">'+item.name+'</label> \
      <input ' + convertInputTypeAttr(item.input_type) +
      ' class="form-control" id="exampleInputEmail1" placeholder="'+
      item.description +'" ' + convertInputRequiredAttr(item.mandatory) +'> \
    </div>'

    $("#frm-elements-container").append(htmlInput);
  })
}

function convertInputTypeAttr(input_type) {
  if (input_type==0) {
    return 'type="text"';
  } else if (input_type==1) {
    return 'type="number" step="1"';
  } else if (input_type==2) {
    return 'type="number" step="0.1"';
  }
}

function convertInputRequiredAttr(mandatory) {
  if (mandatory) {
    return "required";
  }
  return ''
}

})
