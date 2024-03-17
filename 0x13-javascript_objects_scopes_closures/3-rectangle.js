#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      let s = '';
      for (let b = 0; b < this.width; b++) {
        s += 'X';
      }
      console.log(s);
    }
  }
}

module.exports = Rectangle;
