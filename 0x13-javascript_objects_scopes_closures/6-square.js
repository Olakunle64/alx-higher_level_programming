#!/usr/bin/node

/* create a class called Square that inherit from another class called Square */

const squareParent = require('./5-square');

module.exports = class Square extends squareParent {
  charPrint (c) {
    let newWidth;
    if (!c) {
      newWidth = 'X'.repeat(this.width);
    } else {
      newWidth = c.repeat(this.width);
    }
    let newHeight = this.height;
    while (newHeight > 0) {
      console.log(newWidth);
      newHeight--;
    }
  }
};
