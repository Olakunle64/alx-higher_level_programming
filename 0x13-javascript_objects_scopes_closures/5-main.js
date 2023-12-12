#!/usr/bin/node
const Square = require('./5-square');

const s1 = new Square(4);
s1.print();
console.log(s1.width);
console.log(s1.height);
s1.double();
s1.print();
console.log(s1.width);
console.log(s1.height);
