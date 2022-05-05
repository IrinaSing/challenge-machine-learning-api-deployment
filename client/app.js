function getFurnishedVal() {
  var furnishedVal = document.getElementsByName("furnished");
  for (var i in furnishedVal) {
    if (furnishedVal[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function getTerracedVal() {
  var terracedVal = document.getElementsByName("terrace");
  for (var i in terracedVal) {
    if (terracedVal[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1;
}

function getGardenVal() {
  var gardenVal = document.getElementsByName("garden");
  for (var i in gardenVal) {
    if (gardenVal[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function getFireVal() {
  var fireVal = document.getElementsByName("openfire");
  for (var i in fireVal) {
    if (fireVal[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1;
}

function getPoolVal() {
  var poolVal = document.getElementsByName("pool");
  for (var i in poolVal) {
    if (poolVal[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1;
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  const livingArea = getElementById("uiLivingArea");
  const surfaceArea = getElementById("uiSurfaceArea");
  const condition = getElementById("uiCondition");
  const numOfBedrooms = getElementById("uiBedrooms");
  const location = document.getElementById("uiLocations");
  const furnished = getFurnishedVal();
  const terrace = getTerracedVal();
  const garden = getGardenVal();
  const openFire = getFireVal();
  const pool = getPoolVal();
  const estPrice = document.getElementById("uiEstimatedPrice");

  // var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
  var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(
    url,
    {
      location: location.value,
      number_of_bedrooms: numOfBedrooms,
      living_area: parseFloat(livingArea.value),
      furnished: furnished.value,
      open_fireplace: openFire.value,
      terrace: terrace.value,
      garden: garden.value,
      surface_area_land: parseFloat(surfaceArea.value),
      pool: pool.value,
      condition: condition.value,
    },
    function (data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " €</h2>";
      console.log(status);
    }
  );
}

function onPageLoad() {
  console.log("document is loaded");
  const url = "http://127.0.0.1:5000/get_location_names";
  $.get(url, function (data, status) {
    console.log("got response for get location names");
    if (data) {
      var locations = data.locations;
      var uiLocations = document.getElementById("uiLocations");
      $("#uiLocations").empty();
      for (var i in locations) {
        var opt = new Option(locations[i]);
        $("#uiLocations").append(opt);
      }
    }
  });
}

function onPageLoad() {
  console.log("document loaded");
  var url = "http://127.0.0.1:5000/get_location_names";
  $.get(url, function (data, status) {
    console.log("got response for get_location_names request");
    if (data) {
      var locations = data.locations;
      var uiLocations = document.getElementById("uiLocations");
      $("#uiLocations").empty();
      for (var i in locations) {
        var opt = new Option(locations[i]);
        $("#uiLocations").append(opt);
      }
    }
  });
}

window.onload = onPageLoad();
