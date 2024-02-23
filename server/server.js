const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());

let greet = [{id : 'hello', message : 'Hello, World!'}];

// Example route
app.get('/api/greet', (req, res) => {
    res.json(greet);
});

app.post('/api/greet', (req, res) => {
    const newGreet = req.body;
    greet.push(newGreet);
});

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on PORT ${PORT}`)
});