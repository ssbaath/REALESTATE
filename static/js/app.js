function BathroomVal() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function CarVal() {
  var uiCar = document.getElementsByName("uiCar");
  for(var i in uiCar) {
    if(uiCar[i].checked) {
    debugger;
        return parseInt(i);
    }
  }
  return -1; // Invalid Value
}

function BedroomVal() {
  var uiBHK = document.getElementsByName("uiBedroom");
  for(var i in uiBHK) {
    if(uiBHK[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var bhk = BedroomVal();
  var bathrooms = BathroomVal();
  var Car =CarVal();
  var sqm = document.getElementById("uiSqm");
  var location = document.getElementById("uiLocations");
  var estPrice = document.getElementById("uiEstimatedPrice");


  debugger;
  var url = window.document.location.origin +"/predict_house_price";
  $.post(url, {
      bedroom2: bhk,
      bathroom: bathrooms,
      car: Car,
      buildingarea: parseFloat(sqm.value),
      suburbs: location.value
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" +"$"+ data.estimated_price.toString();
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
    debugger;

var url = window.document.location.origin + "/get_location_names";
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var locations = data.locations;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;