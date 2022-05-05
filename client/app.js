function getFurnishedVal() {
  const furnishedVal = document.getElementById("furnished");
  console.log("furnishedVal", furnishedVal.checked);
  for (let i in furnishedVal) {
    if (furnishedVal[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function getTerracedVal() {
  const terracedVal = document.getElementById("terrace");
  for (let i in terracedVal) {
    if (terracedVal[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1;
}

function getGardenVal() {
  const gardenVal = document.getElementById("garden");
  for (let i in gardenVal) {
    if (gardenVal[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1;
}

function getFireVal() {
  const fireVal = document.getElementById("openfire");
  for (let i in fireVal) {
    if (fireVal[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1;
}

function getPoolVal() {
  const poolVal = document.getElementById("pool");
  for (let i in poolVal) {
    if (poolVal[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1;
}

function estimatedPriceOnclick() {
  console.log("Estimate price button clicked");
  const livingArea = document.getElementById("uiLivingArea").value;
  const surfaceArea = document.getElementById("uiSurfaceArea").value;
  const condition = document.getElementById("uiCondition").value;
  const numOfBedrooms = document.getElementById("uiBedrooms").value;
  const location = document.getElementById("uiLocations").value;
  const furnished = getFurnishedVal().value;
  const terrace = getTerracedVal().value;
  const garden = getGardenVal().value;
  const openFire = getFireVal().value;
  const pool = getPoolVal().value;
  const estPrice = document.getElementById("uiEstimatedPrice");
  console.log(
    livingArea,
    surfaceArea,
    condition,
    numOfBedrooms,
    location,
    furnished,
    terrace,
    garden,
    openFire,
    pool,
    estPrice
  );
  const url = "http://127.0.0.1:5000/predict_house_price"; //Use this if you are NOT using nginx which is first 7 tutorials
  //const url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(
    url,
    {
      location: location,
      number_of_bedrooms: numOfBedrooms,
      living_area: parseFloat(livingArea),
      furnished: furnished,
      open_fireplace: openFire,
      terrace: terrace,
      garden: garden,
      surface_area_land: parseFloat(surfaceArea),
      pool: pool,
      condition: condition,
    },
    function (data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " €</h2>";
      console.log(status);
    }
  );
}

function onPageLoad() {
  console.log("document loaded");
  const url_loc = "http://127.0.0.1:5000/get_location_names";
  const url_cond = "http://127.0.0.1:5000/get_condition";

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

  $.get(url_cond, function (data, status) {
    console.log("got response for get_condition request");
    if (data) {
      const condition = data.condition;
      const uiCondition = document.getElementById("uiCondition");
      $("#uiCondition").empty();
      for (let i in condition) {
        const opt = new Option(condition[i]);
        $("#uiCondition").append(opt);
      }
    }
  });
}

window.onload = onPageLoad();
