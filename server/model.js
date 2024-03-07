const arima = require('arima');
const fs = require('fs');
const readline = require('readline');

const stream = fs.createReadStream('./data/energy_consumption.csv');
const reader = readline.createInterface({ input: stream });

let options = {
    p : 1,
    d : 0,
    q : 0,
    P : 1,
    D : 1,
    Q : 1,
    s : 60,
};

let data = [];
let timestamp = [];
let temp = [];
let humidity = [];
let sqft = [];
let occupancy = [];
let hvac = [];
let light = [];
let renewable = [];
let dayOfWeek = [];
let holiday = [];
let energy = [];

reader.on("line", row => {
    data.push(row.split(","));
});

reader.on("close", () => {
    data.shift();
    // const partData = data.slice(-5);
    
    for (let i = 0; i < data.length; i++) {

        timestamp.push(new Date(data[i][0]));
        temp.push(data[i][1]);
        humidity.push(data[i][2]);
        sqft.push(data[i][3]);
        occupancy.push(data[i][4]);
        hvac.push(data[i][5]);
        light.push(data[i][6]);
        renewable.push(data[i][7]);
        dayOfWeek.push(data[i][8]);
        holiday.push(data[i][9]);
        energy.push(parseFloat(data[i][10]));
    }

    const model = new arima(options).fit(energy);
    const [pred, err] = model.predict(5);
    console.log(`Predictions: ${pred}`);
    console.log(`Error: ${err}`);
});

// fs.createReadStream("./example.csv")
//   .pipe(
//     parse({
//       delimiter: ",",
//       columns: true,
//       ltrim: true,
//     })
//   )
//   .on("data", function (row) {
//     data.push(row);
//   })
//   .on("error", function (error) {
//     console.log(error.message);
//   })
//   .on("end", function () {
//     console.log("parsed csv data:");
//     console.log(data);
//   });

