// from data.js
var tableData = data;

// YOUR CODE HERE!
var newUFO = [];

var table = d3.select("table");
var tbody = d3.select("tbody");

function buildTable(data) {
  tbody.html("");
  data.forEach((dataRow) => {
    var row = tbody.append("tr");

    Object.values(dataRow).forEach((val) => {
      var cell = row.append("td");
        cell.text(val);
      }
    );
  });
}

function handleClick() {
  d3.event.preventDefault();
  var date = d3.select("#datetime").property("value");
  let filteredData = tableData;

  if (date) {
    filteredData = filteredData.filter(row => row.datetime === date);
  }

  buildTable(filteredData);
}

d3.selectAll("#filter-btn").on("click", handleClick);

buildTable(tableData);

// // Append one table row `tr` to the table body
// var row = tbody.append("tr");

// // Append one cell for sighting data
// row.append("td").text(datetime, [0]);
// row.append("td").text(city, [1]);
// row.append("td").text(state, [2]);
// row.append("td").text(country, [3]);
// row.append("td").text(shape, [4]);
// row.append("td").text(comments, [5]);

// var date = d3.select("#date");
// var output = d3.select("ufo-table");

// function handleChange(event) {
//     // grab the value of the input field
//     var inputText = d3.event.target.value;}
  
  


// var tbody = d3.select("tbody");

// var table = d3.select("ufo-table");

// var button = d3.select("#filter-btn");

// d3.event.preventDefault(handleClick);

// function handleClick() {

//   button.on("click", function() {
//   d3.select("tbody")
//   .selectAll("tr")
//   .data(data)
//   .enter()
//   .append("tr")
//   .html(function(d) {
//     return `<td>${d.datetime}</td><td>${d.city}</td><td>${d.state}</td><td>${d.country}</td><td>${d.shape}</td><td>${d.comments}</td>`;
//   });
//   });

//   inputField.on("change", function(handleClick) {
//     var newText = d3.event.target.value;
//     console.log(newText);
//   });
// }


