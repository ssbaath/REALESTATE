function Bathroom() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function Garage() {
  var uiCar = document.getElementsByName("uiCar");
  for(var i in uiCar) {
    if(uiCar[i].checked) {
        return parseInt(i);
    }
  }
  return -1; // Invalid Value
}

function Bedroom() {
  var uiBHK = document.getElementsByName("uiBedroom");
  for(var i in uiBHK) {
    if(uiBHK[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function onClickEstimatePrice() {
  console.log("Clicked Estimate Price: Button");
  var bhk = Bedroom();
  var bathrooms = Bathroom();
  var Car =Garage();
  var sqm = document.getElementById("uiSqm");
  var location = document.getElementById("uiLocations");
  var estPrice = document.getElementById("uiEstimatedPrice");


  var url = window.document.location.origin +"/price";
  $.post(url, {
      bedroom2: bhk,
      bathroom: bathrooms,
      car: Car,
      buildingarea: parseFloat(sqm.value),
      suburbs: location.value
  },function(data, status) {
      console.log(data.suburb_price);
      estPrice.innerHTML = "<h2>" +"$"+ data.suburb_price.toString();
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "Information Uploaded" );

var url = window.document.location.origin + "/suburbs";
  $.get(url,function(data, status) {
      console.log("Suburbs Information Received");
      if(data) {
          var sub = data.sub;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for(var i in sub) {
              var opt = new Option(sub[i]);
              $('#uiLocations').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;
