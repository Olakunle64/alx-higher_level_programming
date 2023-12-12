#!/usr/bin/node

/* create a class called Square that inherit from Rectangle */

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    /* initialize instance attribute in both classes */
    super(size, size);
    this.size = size;
  }
};
