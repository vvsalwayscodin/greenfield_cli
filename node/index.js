const express = require('express');
const app = express();

app.use(express.json()); // Enable JSON body parsing

// POST /create-client route
app.post('/create-client', (req, res) => {
  const rpcAddr = req.body.rpcAddr;
  const chainId = req.body.chainId;

  let client = Client.create(rpcAddr, chainId)
  print(client)
  // Send a response
  res.send('Client created successfully');
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});