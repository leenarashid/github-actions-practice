// Load the http module
const http = require('http');

// Define server port
const PORT = process.env.PORT || 3000;

// Create the server
const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World from Node.js!\n');
});

// Start listening
server.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}/`);
});
