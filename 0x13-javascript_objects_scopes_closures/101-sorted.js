#!/usr/bin/node

/* Write a script that imports a dictionary of occurrences by user
 * id and computes a dictionary of user ids by occurrence
 */

const dict = require('./101-data').dict;
const bigDict = {};
for (const key in dict) {
  const value = dict[key];
  if (!bigDict[dict[key]]) {
    bigDict[value] = [];
  }
  bigDict[value].push(key);
}
console.log(bigDict);
