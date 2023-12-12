#!/usr/bin/node
const Rectangle = require('./3-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1.height);
r1.print();
console.log(r1.height);

const r2 = new Rectangle(10, 5);
r2.print();
