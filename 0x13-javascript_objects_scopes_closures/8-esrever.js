#!/usr/bin/node

/* Write a function that returns the reversed version of a list */

exports.esrever = function (list) {
  const newList = [];
  let listLen = list.length - 1;
  while (listLen >= 0) {
    newList.push(list[listLen]);
    listLen--;
  }
  return newList;
};
