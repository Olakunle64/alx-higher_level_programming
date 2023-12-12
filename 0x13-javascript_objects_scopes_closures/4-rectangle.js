#!/usr/bin/node

/* create a class named Rectangle
 * instance attribute <width> and <height>
 * if w or h is 0 or not a positive integer create an empty object
 * add a public instance method
 */

module.exports = class Rectangle {
  constructor (w, h) {
    /* constructor for the instance attribute */
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    /* a method to print a rectangle */
    const theWidth = 'X'.repeat(this.width);
    let theHeight = this.height;
    while (theHeight > 0) {
      console.log(theWidth);
      theHeight--;
    }
  }

  rotate () {
    /* swap the width and height of the rectangle */
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    /* multiply the width and height by 2 */
    this.width *= 2;
    this.height *= 2;
  }
};
