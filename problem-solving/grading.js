// https://www.hackerrank.com/challenges/grading/problem

'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function gradingStudents(grades) {
    for (let i = 0; i < grades.length; i++) {
        if(grades[i]< 38){
            continue;
        }
        if(grades[i]%5 >= 3){
            grades[i] += 5 - grades[i]%5;
        }
    }
    return grades;
}

function main() {
    const gradesCount = parseInt(readLine().trim(), 10);
    let grades = [];
    for (let i = 0; i < gradesCount; i++) {
        const gradesItem = parseInt(readLine().trim(), 10);
        grades.push(gradesItem);
    }
    const result = gradingStudents(grades);
    console.log(result.join('\n'));
}
