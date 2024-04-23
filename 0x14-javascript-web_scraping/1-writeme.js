#!/usr/bin/node

const fs = require('fs');

// Import the built-in Node.js 'fs' module.

fs.writeFile(process.argv[2], process.argv[3], 'utf-8',
  function (err) {
    if (err) {
      console.log(err);
    }
  });
