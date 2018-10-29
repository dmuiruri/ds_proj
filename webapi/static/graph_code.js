
console.log('Hello from graph_code.js')

// resource endpoints for different customers/usecases
const INDUSTRIAL_BUILDING= 'industry';
const COMMERCIAL_BUILDING = 'commercial-building';
const APARTMENT_BUILDING = 'apartment-building';

const BASE_URL = 'https://ds-2018-webapi.herokuapp.com/predict/'
const DEV_BASE_URL = 'http://127.0.0.1:5000/predict/'


function fetchDataAndDrawGraph(customer, sample_rate='daily'){

    console.log(`Fetching ${sample_rate} sampled ${customer} predictions.`)

    // get predictions
    fetch(`${BASE_URL}${customer}?sampling=${sample_rate}`)
    .then(
        function(response) {
            if (response.status !== 200) {
                console.log('Fetch failed. Status Code: ' +
                response.status);
                return;
            }
            response.json().then(function(data) {
                drawPredictions(data, sample_rate, customer)
            });
        }
    )
    .catch(function(err) {
        console.log('Fetch Error', err);
    });
}


function drawPredictions(data, sample_rate, customer){
    const predictionsAllData = JSON.parse(data)
    // one big object
    console.log(predictionsAllData);

    const prediction = predictionsAllData['y^'];
    const original = predictionsAllData['y'];

    const predictedConsumptionArray = Object.values(prediction)
    const originalConsumptionArray = Object.values(original)

    // array of timestamps (the dayzs)
    const timestampArray = Object.keys(prediction)
    // convert timestamps to more meaningful dates (format: 24/3/2018) 
    const dateArray = timestampArray.map(function(timestamp) {
        return new Date(parseInt(timestamp)).toLocaleDateString();
    });

    console.log(dateArray);
    console.log('PRED: ', predictedConsumptionArray);
    console.log('ORIG: ', originalConsumptionArray);

    // x axis labels for graphs
    const graphXLabelPrediction = `${sample_rate} consumption prediction`
    const graphXLabelOriginal = `${sample_rate} consumption`
    // div elements for different graphs
    const divElementId = `#${sample_rate}-${customer}GraphDiv`

    // https://c3js.org/gettingstarted.html
    c3.generate({
        bindto: divElementId,
        data: {
            //json: dailyPredictions,
          x : 'x',
          columns: [
            ['x'].concat(dateArray),
            [graphXLabelPrediction].concat(predictedConsumptionArray),
            [graphXLabelOriginal].concat(originalConsumptionArray)
            //['Daily consumption predictions', 30, 200, 100, 400, 150, 250]
          ],
           type: 'bar'
        },
        axis: {
            x: {
                type: 'category',
                tick: {
                    rotate: (sample_rate == 'daily' ? 75 : 0), // rotation based on the number of datapoints
                    multiline: false
                },
                //height: 200
            },           
            y: {
              label: { 
                text: 'Consumption (kWh)',
                position: 'outer-middle'
              }
            }
          }
    });


    // // just printing out the data
    // const graphDiv = document.getElementById('dailyIndustryGraphDiv');
    // const h4 = document.createElement("H4");
    // const t = document.createTextNode('The daily consumption data for the graph:');
    // h4.appendChild(t);
    // graphDiv.appendChild(h4)
    // const p = document.createElement("p"); 
    // const dailyData = document.createTextNode(JSON.stringify(dailyPredictions)); 
    // p.appendChild(dailyData); 
    // graphDiv.appendChild(p)

}

// do the stuff
fetchDataAndDrawGraph(INDUSTRIAL_BUILDING, 'weekly');
fetchDataAndDrawGraph(INDUSTRIAL_BUILDING, 'daily');

fetchDataAndDrawGraph(COMMERCIAL_BUILDING, 'weekly');
fetchDataAndDrawGraph(COMMERCIAL_BUILDING, 'daily');

fetchDataAndDrawGraph(APARTMENT_BUILDING, 'weekly');
fetchDataAndDrawGraph(APARTMENT_BUILDING, 'daily');
