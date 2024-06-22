#!/usr/bin/node

export function converter (base) {
  return function (num) {
    return num.toString(base);
  };
}
