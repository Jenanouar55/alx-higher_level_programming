#!/usr/bin/node
import { dict } from './101-data';

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const j in valsUniq) {
  const list = [];
  for (const k in totalist) {
    if (totalist[k][1] === valsUniq[j]) {
      list.unshift(totalist[k][0]);
    }
  }
  newDict[valsUniq[j]] = list;
}
console.log(newDict);
