
console.log('Hello from graph_code.js')

const INDUSTRY_URL = 'https://ds-2018-webapi.herokuapp.com/predict/industry';
//const CONSUMER_URL = 'https://ds-2018-webapi.herokuapp.com/predict/consumer';
//const BUILDING_URL = 'https://ds-2018-webapi.herokuapp.com/predict/building';


function fetchDataAndDrawGraph(electricity_api_url){

    console.log('Fetching daily sampled industry predictions')

    // get daily sampled industry predictions
    fetch(electricity_api_url + '?sampling=daily')
    .then(
        function(response) {
            if (response.status !== 200) {
                console.log('Fetch failed. Status Code: ' +
                response.status);
                return;
            }
            response.json().then(function(data) {
                drawPredictions(data)
            });
        }
    )
    .catch(function(err) {
        console.log('Fetch Error', err);
    });
}


function drawPredictions(data){
    const dailyPredictions = JSON.parse(data)
    // one big object
    console.log(dailyPredictions);

    // array of daily consumption
    const consumptionArray = Object.values(dailyPredictions)
    // array of timestamps (the dayzs)
    const timestampArray = Object.keys(dailyPredictions)
    // convert timestamps to more meaningful dates (format: 24/3/2018) 
    const dateArray = timestampArray.map(function(timestamp) {
        return new Date(parseInt(timestamp)).toLocaleDateString();
    });
    
    console.log(dateArray);
    console.log(consumptionArray);

    //TODO: draw some graphs
    const graphDiv = document.getElementById('industryGraphDiv');

    // just printing out the data
    const h4 = document.createElement("H4");
    const t = document.createTextNode('The daily consumption data for the graph:');
    h4.appendChild(t);
    graphDiv.appendChild(h4)
    const p = document.createElement("p"); 
    const dailyData = document.createTextNode(JSON.stringify(dailyPredictions)); 
    p.appendChild(dailyData); 
    graphDiv.appendChild(p)

}


fetchDataAndDrawGraph(INDUSTRY_URL);