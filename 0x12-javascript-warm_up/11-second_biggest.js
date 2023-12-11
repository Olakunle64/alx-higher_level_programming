#!/usr/bin/node

let max = Number.NEGATIVE_INFINITY;
let smax = Number.NEGATIVE_INFINITY;
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let i = 2;
  while (process.argv[i]) {
    if (Number(process.argv[i]) > max) {
      smax = max;
      max = Number(process.argv[i]);
    } else if (process.argv[i] > smax && process.argv[i] < max) {
      smax = process.argv[i];
    }
    i++;
  }
  console.log(smax);
}
