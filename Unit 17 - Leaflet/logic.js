var apiKey = "pk.eyJ1Ijoia3VsaW5pIiwiYSI6ImNpeWN6bjJ0NjAwcGYzMnJzOWdoNXNqbnEifQ.jEzGgLAwQnZCv9rA6UTfxQ";

var lightmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
  accessToken: apiKey
});

var map = L.map("map", {
  center: [
    40, -118
  ],
  zoom: 5
});

// 'lightmap' tile layer to the map.
lightmap.addTo(map);

// bring in geoJSON data.
d3.json("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson", function(data) {


  function styleInfo(feature) {
    return {
      opacity: 1,
      fillOpacity: 1,
      fillColor: getColor(feature.properties.mag),
      color: "#000000",
      radius: getRadius(feature.properties.mag),
      stroke: true,
      weight: 0.5
    };
  }


  function getColor(magnitude) {
    switch (true) {
    case magnitude > 5:
      return "#22460D";
    case magnitude > 4:
      return "#2B5810";
    case magnitude > 3:
      return "#366E14";
    case magnitude > 2:
      return "#448A19";
    case magnitude > 1:
      return "#55AD1F";
    default:
      return "#6AD827";
    }
  }


  function getRadius(magnitude) {
    if (magnitude === 0) {
      return 1;
    }

    return magnitude * 4;
  }

  // Add circle markers.

  L.geoJson(data, {
    pointToLayer: function(feature, latlng) {
      return L.circleMarker(latlng);
    },

    style: styleInfo,
    // Add pop up captions with json reference.

    onEachFeature: function(feature, layer) {
      layer.bindPopup("<h3>Event: " + feature.properties.type + 
      "<hr>Location: " + feature.properties.place+ "</h3>"
      + "<h3><hr>Magnitude: " + feature.properties.mag + "</h3>");
    }
  }).addTo(map);

  var legend = L.control({
    position: "bottomright"
  });

  legend.onAdd = function() {
    var div = L.DomUtil.create("div", "info legend");

    var grades = [0, 1, 2, 3, 4, 5];
    var colors = [
        "#6AD827",
        "#55AD1F",
        "#448A19",
        "#366E14",
        "#2B5810",
        "#22460D"
    ];


    for (var i = 0; i < grades.length; i++) {
      div.innerHTML +=
        "<i style='background: " + colors[i] + "'></i> " +
        grades[i] + (grades[i + 1] ? "&ndash;" + grades[i + 1] + "<br>" : "+");
    }
    return div;
  };

  legend.addTo(map);
});
