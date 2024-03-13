#!/usr/bin/node
exports.callMeMoby = function (repeat, theFunction) {
  for (let i = 0; i < repeat; i++) {
    theFunction();
  }
};
