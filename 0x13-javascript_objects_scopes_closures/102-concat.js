#!/usr/bin/node
import { readFileSync, writeFileSync } from 'fs';

const fArg = readFileSync(process.argv[2]).toString();
const sArg = readFileSync(process.argv[3]).toString();
writeFileSync(process.argv[4], fArg + sArg);
