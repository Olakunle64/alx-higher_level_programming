#!/usr/bin/node

function factorial (num) {
  if (num === 0 || num === 1) {
    return (1);
  }
  return (num * factorial(num - 1));
}
const number = Number(process.argv[2]);
if (Number.isNaN(number)) {
  console.log(1);
} else {
  console.log(factorial(number));
}
