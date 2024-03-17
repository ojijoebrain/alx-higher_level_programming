#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const b in valsUniq) {
  const list = [];
  for (const a in totalist) {
    if (totalist[a][1] === valsUniq[b]) {
      list.unshift(totalist[a][0]);
    }
  }
  newDict[valsUniq[b]] = list;
}
console.log(newDict);
