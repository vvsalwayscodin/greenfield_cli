const express = require('express');
const app = express();
const client = require('./methods/client')

app.use(express.json()); // Enable JSON body parsing

// POST /create-client route
app.post('/transfer', (req, res) => {

    // Send a response
    res.send('Client created successfully');
});

// Start the server
const port = 3000;
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});