#!/usr/bin/node

function factorial (num) {
  if (num === 0 || num === 1) {
    return (1);
  }
  return (num * factorial(num - 1));
}
number = Number(process.argv[2])
if (number) {
	console.log(factorial(number));
}
