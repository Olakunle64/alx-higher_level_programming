#!/usr/bin/node

let count = Number(process.argv[2]);
if (Number.isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  while (count > 0) {
    console.log('C is fun');
    count -= 1;
  }
}
