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

  var price = $('#pricePerDay').text()

  function splitDate(dateString) {
    return dateString.split('-');
  }

  $('#startDate').on('change', function() {
    startDate = $(this).val();
    partsStart = splitDate(startDate);
    var endDate = $('#endDate').val();
    if (endDate) {
      sDate = new Date(partsStart[0], partsStart[1], partsStart[2]);
      eDate = new Date(partsEnd[0], partsEnd[1], partsEnd[2]);
      if (sDate > eDate) {
        $('#endDate').val(startDate);
        endDate = startDate
        partsEnd = splitDate(endDate);
        document.getElementById('endDate').min = $(this).val();
      }
    } else {
      document.getElementById('endDate').min = $(this).val();
    }
    if (endDate) {
      totalPrice = calcPrice(partsStart, partsEnd);
      $('#totalPrice span').text(totalPrice);
    }
  })

  $('#endDate').on('change', function() {
    endDate = $(this).val();
    partsEnd = splitDate(endDate);
    if (startDate) {
      totalPrice = calcPrice(partsStart, partsEnd);
      $('#totalPrice span').text(totalPrice);
    }
  })

  function calcPrice(sDate, eDate) {
    console.log(sDate[0], parseInt(sDate[1])-1, sDate[2])
    var startDate = new Date(sDate[0], parseInt(sDate[1])-1, sDate[2]);
    var endDate = new Date(eDate[0], parseInt(eDate[1])-1, eDate[2]);
    var numDays = (Math.round((endDate - startDate)/(1000*60*60*24))) + 1;
    totalPrice = numDays * price;
    return totalPrice;
  }

})
