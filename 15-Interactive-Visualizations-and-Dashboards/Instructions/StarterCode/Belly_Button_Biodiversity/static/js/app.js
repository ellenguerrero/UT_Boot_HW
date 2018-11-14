

function buildMetadata(sample) {

  var sampleurl="/samples/<sample>";



  // Use `d3.json` to fetch the metadata for a sample
    // Use d3 to select the panel with id of `#sample-metadata`

    // Use `.html("") to clear any existing metadata

    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.

    }


function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots

    // @TODO: Build a Bubble Chart using the sample data

    // @TODO: Build a Pie Chart

    const toptenSamples=sample_values.slice()
    const toptenIds=otu_ids.slice()
    const toptenLabels=otu_labels.slice()
    
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).

    d3.json(sampleurl).then(function(data) {
      var data = [data];
      Plotly.plot("pie", data);
    });
  
  
  function updatePlotly(newdata) {
    Plotly.restyle("pie", "values", [newdata.values]);
    Plotly.restyle("pie", "labels", [newdata.labels]);
  }
  
  function getData(route) {
    console.log(route);
    d3.json(`/${route}`).then(function(data) {
      console.log("newdata", data);
      updatePlotly(data);
    });
  }
}




function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
