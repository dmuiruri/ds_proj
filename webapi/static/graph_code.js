
console.log('Hello from graph_code.js')

const INDUSTRY_URL = 'https://ds-2018-webapi.herokuapp.com/predict/industry';
//const CONSUMER_URL = 'https://ds-2018-webapi.herokuapp.com/predict/consumer';
//const BUILDING_URL = 'https://ds-2018-webapi.herokuapp.com/predict/building';


function fetchDataAndDrawGraph(electricity_api_url, sample_rate='daily'){

    console.log(`Fetching ${sample_rate} sampled industry predictions.`)

    // get daily sampled industry predictions
    fetch(`${electricity_api_url}?sampling=${sample_rate}`)
    .then(
        function(response) {
            if (response.status !== 200) {
                console.log('Fetch failed. Status Code: ' +
                response.status);
                return;
            }
            response.json().then(function(data) {
                drawPredictions(data, sample_rate)
            });
        }
    )
    .catch(function(err) {
        console.log('Fetch Error', err);
    });
}


function drawPredictions(data, sample_rate){
    const predictions = JSON.parse(data)
    // one big object
    console.log(predictions);

    // array of consumption
    const consumptionArray = Object.values(predictions)
    // array of timestamps (the dayzs)
    const timestampArray = Object.keys(predictions)
    // convert timestamps to more meaningful dates (format: 24/3/2018) 
    const dateArray = timestampArray.map(function(timestamp) {
        return new Date(parseInt(timestamp)).toLocaleDateString();
    });

    console.log(dateArray);
    console.log(consumptionArray);

    // kind of a haxxx
    const graphXLabel = `${sample_rate} consumption predictions`
    const divElementId = `#${sample_rate}IndustryGraphDiv`

    // https://c3js.org/gettingstarted.html
    c3.generate({
        bindto: divElementId,
        data: {
            //json: dailyPredictions,
          x : 'x',
          columns: [
            ['x'].concat(dateArray),
            [graphXLabel].concat(consumptionArray)
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
//fetchDataAndDrawGraph(INDUSTRY_URL, 'monthly');
fetchDataAndDrawGraph(INDUSTRY_URL, 'weekly');
fetchDataAndDrawGraph(INDUSTRY_URL, 'daily');
