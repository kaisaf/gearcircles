$(document).ready(function() {
  $('#myModal').on('shown.bs.modal', function () {
    $('#myInput').focus();
    expDate = $('#expDate').text();
    var d = new Date(expDate);
    exp = convertDate(d)
    document.getElementById('startDate').max = exp;
    document.getElementById('endDate').max = exp;
    document.getElementById('endDate').min = convertDate(new Date())
    document.getElementById('startDate').min = convertDate(new Date())
  })

  var price = $('#pricePerDay').text()
  // var partsStart = null;
  // var partsEnd = null;
  // var endDate = null;
  // var startDate = null;

  function convertDate(d) {
    var year = d.getFullYear();
    var month = d.getMonth() + 1;
    var date = d.getDate();
    if (month<10) {
      month = "0"+month;
    }
    if (date<10) {
      date = "0"+date;
    }
    var dateString = year + "-" + month + "-" + date;
    console.log(dateString)
    return dateString;
  }

  function splitDate(dateString) {
    date = dateString.split('-');
    return date;
  }

  $('#startDate').on('change', function() {
    var startDate = $(this).val();
    var partsStart = splitDate(startDate);
    var endDate = $('#endDate').val();
    var partsEnd = splitDate(endDate);
    if (endDate) {
      var sDate = new Date(partsStart[0], partsStart[1], partsStart[2]);
      var eDate = new Date(partsEnd[0], partsEnd[1], partsEnd[2]);
      if (sDate > eDate) {
        endDate = startDate;
        partsEnd = splitDate(endDate);
        $('#endDate').val(startDate);
        document.getElementById('endDate').min = $(this).val();
      }
      var totalPrice = calcPrice(partsStart, partsEnd);
      $('#totalPrice span').text(totalPrice);
    }
    document.getElementById('endDate').min = $(this).val();
  })

  $('#endDate').on('change', function() {
    endDate = $(this).val();
    partsEnd = splitDate(endDate);
    startDate = $('#startDate').val();
    partsStart = splitDate(startDate)
    var sDate = new Date(partsStart[0], partsStart[1], partsStart[2]);
    var eDate = new Date(partsEnd[0], partsEnd[1], partsEnd[2]);
    totalPrice = calcPrice(partsStart, partsEnd);
    $('#totalPrice span').text(totalPrice);
    document.getElementById('endDate').min = $('#startDate').val();
  })

  function calcPrice(sDate, eDate) {
    console.log(sDate, eDate)
    var startDate = new Date(sDate[0], parseInt(sDate[1])-1, sDate[2]);
    var endDate = new Date(eDate[0], parseInt(eDate[1])-1, eDate[2]);
    var numDays = (Math.round((endDate - startDate)/(1000*60*60*24))) + 1;
    totalPrice = numDays * price;
    return totalPrice;
  }

})
