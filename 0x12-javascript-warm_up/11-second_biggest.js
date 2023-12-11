#!/usr/bin/node

let max = Number.NEGATIVE_INFINITY;
let smax = Number.NEGATIVE_INFINITY;
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let i = 2;
  while (process.argv[i]) {
    if (Number(process.argv[i]) > max) {
      max = i;
    }
    i++;
  }
  i = 2;
  while (process.argv[i]) {
    if (i === max) {
      i++;
      continue;
    }
    if (Number(process.argv[i]) > smax) {
      smax = Number(process.argv[i]);
    }
    i++;
  }
  console.log(smax);
}
