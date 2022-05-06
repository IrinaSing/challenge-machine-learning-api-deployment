function getPoolVal() {
  const poolVal = document.getElementById("pool");
  return poolVal.checked;
}

function numberWithCommas(x) {
  return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function estimatedPriceOnclick() {
  console.log("Estimate price button clicked");
  const livingArea = document.getElementById("uiLivingArea").value;
  const surfaceArea = document.getElementById("uiSurfaceArea").value;
  const condition = document.getElementById("uiCondition").value;
  const numOfBedrooms = document.getElementById("uiBedrooms").value;
  const location = document.getElementById("uiLocations").value;
  const pool = getPoolVal();
  const estPrice = document.getElementById("uiEstimatedPrice");

  const url = "http://127.0.0.1:5000/predict_house_price"; //Use this if you are NOT using nginx which is first 7 tutorials
  //const url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(
    url,
    {
      location: location,
      number_of_bedrooms: numOfBedrooms,
      living_area: parseFloat(livingArea),
      surface_area_land: parseFloat(surfaceArea),
      pool: pool,
      condition: condition,
    },
    function (data, status) {
      calculated_price = data.estimated_price;
      formatted_price = numberWithCommas(calculated_price);
      estPrice.innerHTML = "<h2>" + formatted_price + " €</h2>";
      console.log(status);
    }
  );
}

function onPageLoad() {
  console.log("document loaded");
  const url_loc = "http://127.0.0.1:5000/get_location_names";

  $.get(url_loc, function (data, status) {
    console.log("got response for get_location_names request");
    if (data) {
      const locations = data.locations;
      const uiLocations = document.getElementById("uiLocations");
      $("#uiLocations").empty();
      for (let i in locations) {
        const opt = new Option(locations[i]);
        $("#uiLocations").append(opt);
      }
    }
  });
}

window.onload = onPageLoad();
