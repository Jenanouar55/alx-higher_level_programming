#!/usr/bin/node
let narg = 0;

export function logMe (item) {
  console.log(narg + ': ' + item);
  narg++;
}
