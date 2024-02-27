const ARIMA = require('arima');

let options = {
    auto : true,
    approximation : 10,
    search : 100,
    p : 10,
    d : 10,
    q : 10
};

// let trainSet = ;

const autoarima = new ARIMA(options).fit(trainSet);
const [pred, err] = autoarima.predict(5);

return pred;