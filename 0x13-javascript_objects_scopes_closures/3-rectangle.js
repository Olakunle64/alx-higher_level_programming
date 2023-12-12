#!/usr/bin/node

/* create a class named Rectangle
 * instance attribute <width> and <height>
 * if w or h is 0 or not a positive integer create an empty object
 * add a public instance method
 */

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const theWidth = 'X'.repeat(this.width);
    let theHeight = this.height;
    while (theHeight > 0) {
      console.log(theWidth);
      theHeight--;
    }
  }
};
