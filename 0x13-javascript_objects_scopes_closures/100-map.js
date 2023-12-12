#!/usr/bin/node

/* Write a script that imports an array and computes a new array */

const list = require('./100-data').list;

let index = -1;
const newList = list.map(function (element) {
  index++;
  return (element * index);
});
console.log(list);
console.log(newList);
