const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());

let greet = [];

// Example routes
app.get('/api/greet', (req, res) => {
    return res.status(200).json(greet);
});

app.post('/api/add-greet', (req, res) => {
    const newGreet = req.body;
    greet.push(newGreet);
    return res.status(201).send('Successfuly created new greet.').json(newGreet);
});

app.delete('/api/remove-greet/:id', (req, res) => {
    const { id } = req.params;
    greet = greet.filter(greet => greet.id !== id);
    return res.status(200).json(greet);
});

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on PORT ${PORT}`)
});