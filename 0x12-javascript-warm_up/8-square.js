#!/usr/bin/node

let count = Number(process.argv[2]);
if (Number.isNaN(count)) {
  console.log('Missing size');
} else {
  let square = '';
  for (let i = 0; i < count; i++) {
    square += 'X';
  }
  while (count > 0) {
    console.log(square);
    count -= 1;
  }
}
