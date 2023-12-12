#!/usr/bin/node

/* Write a script that concats 2 files
 * The first argument is the file path of the first source file
 * The second argument is the file path of the second source file
 * The third argument is the file path of the destination
 */

const fs = require('fs');
let fileContent;

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    return;
  }
  fileContent = data;
  fs.readFile(process.argv[3], 'utf8', (err, data) => {
    if (err) {
      return;
    }
    fs.writeFile(process.argv[4], fileContent + data, 'utf8', (err) => {
      if (err) {
        console.log('An error occured!');
      }
    });
  });
});
