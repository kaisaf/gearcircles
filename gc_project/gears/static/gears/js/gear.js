$(document).ready(function() {
  $('#myModal').on('shown.bs.modal', function () {
    console.log("modal");
    $('#myInput').focus();
  })

  var startDate = null;
  var endDate = null;

  $('#startDate').on('change', function() {
    startDate = $(this).val();
    console.log(startDate);
  })

  $('#endDate').on('change', function() {
    endDate = $(this).val();
    if (startDate) {
      var partsStart = startDate.split('-');
      var partsEnd = endDate.split('-');
      startDate = new Date(partsStart[0],partsStart[1],partsStart[2]);
      endDate = new Date(partsEnd[0],partsEnd[1],partsEnd[2]);
      var difference = Math.Abs(endDate - startDate);
      console.log(difference)
      $('#totalPrice').text("PRICE: " + difference);
    }
  })



})
