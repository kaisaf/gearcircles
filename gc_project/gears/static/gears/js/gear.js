$(document).ready(function() {
  $('#myModal').on('shown.bs.modal', function () {
    $('#myInput').focus();
    expDate = $('#expDate').text();
    var d = new Date(expDate);
    var year = d.getFullYear();
    var month = d.getMonth() + 1;
    var date = d.getDate();
    exp = year + "-" + month + "-" + date;
    document.getElementById('startDate').max = exp;
    document.getElementById('endDate').max = exp;
  })

  var startDate = null;
  var endDate = null;
  var price = $('#totalPrice span').text()

  function splitDate(dateString) {
    return dateString.split('-');
  }

  $('#startDate').on('change', function() {
    startDate = $(this).val();
    partsStart = splitDate(startDate);
    $('#endDate').val(startDate);
    document.getElementById('endDate').min = $(this).val();
    if (endDate) {
      startDate = new Date(partsStart[0],partsStart[1],partsStart[2]);
      endDate = new Date(partsEnd[0],partsEnd[1],partsEnd[2]);
      var difference = Math.round((endDate - startDate)/(1000*60*60*24));
      totalPrice = (difference + 1)*price;
      $('#totalPrice span').text(totalPrice);
    }
  })

  $('#endDate').on('change', function() {
    endDate = $(this).val();
    partsEnd = splitDate(endDate);
    if (startDate) {
      startDate = new Date(partsStart[0],partsStart[1],partsStart[2]);
      endDate = new Date(partsEnd[0],partsEnd[1],partsEnd[2]);
      var difference = Math.round((endDate - startDate)/(1000*60*60*24));
      totalPrice = (difference + 1)*price;
      $('#totalPrice span').text(totalPrice);
    }
  })

})
