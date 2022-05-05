function onPageLoad() {
  console.log("document is loaded");
  const url = "http://127.0.0.1:5000/get_location_names";
  $.get(url, function (data, status) {
    console.log("got response for get location names");
    if (data) {
      const locations = data.locations;
      const uilocations = document.getElementById("uilocations");
      $("#uilocations").append(opt);
    }
  });
}

window.onload = onPageLoad;
