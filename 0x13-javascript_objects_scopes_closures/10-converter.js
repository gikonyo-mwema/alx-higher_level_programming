#!/usr/bin/node
exports.converter = function (base) {
  return function (num) {
    if (num === 0) {
      return '0';
    } else if (num < base) {
      return num.toString();
    } else {
      return (exports.converter(base)(Math.floor(num / base)) + (num % base).toString());
    }
  };
};
