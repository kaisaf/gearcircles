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
      <input type="text" class="form-control" id="exampleInputEmail1" placeholder="'+item.description+'"> \
    </div>'

    $("#frm-elements-container").append(htmlInput);
  })
}

})
