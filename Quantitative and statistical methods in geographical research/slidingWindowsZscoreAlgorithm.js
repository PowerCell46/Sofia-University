function average(...args) {
    return args.reduce((acc, curr) => acc + curr, 0) / args.length;
}


function zScore(dataArray, absoluteValues) {
    const averageValue = average(...(Array.isArray(dataArray[0]) ? dataArray.map(nestedArr => nestedArr[0]) : dataArray));
    const calcDeviationArr = dataArray.map(value => Array.isArray(value) ? ((value[0] - averageValue) ** 2) : ((value - averageValue) ** 2));
    const standardDeviation = Math.sqrt(average(...calcDeviationArr));
    
    if (absoluteValues) {
        var zScoreArray = dataArray.map(value => Array.isArray(value) ? 
        [value[0], value[1], Math.abs((value[0] - averageValue) / standardDeviation)] : 
        [value, Math.abs((value - averageValue) / standardDeviation)]);
    } else {
        var zScoreArray = dataArray.map(value => Array.isArray(value) ?
        [value[0], value[1], (value[0] - averageValue) / standardDeviation] :
        [value, (value - averageValue) / standardDeviation]);
    }
    return zScoreArray;
}

// console.log(zScore([10, 12, 14, 16, 18], true));


// Best implementaion of the Sliding Windows algorithm where we calculate the Z-score for every value in the matrix
// and do the calculation for the value with the biggest Z-score (if there are multiple we get the one that is 
// closer to the beginning of the matrix) until we go through the whole array.


function slidingWindowsZscore(matrix) {
    let flattenedMatrix = [];

    for (let row of matrix) {
        row.forEach(value => flattenedMatrix.push([value, false]));
    }
    
    flattenedMatrix = zScore(flattenedMatrix.slice(), true);

    for (let index = 0; index < flattenedMatrix.length; index++) {

        let orderedMatrix = flattenedMatrix.slice().sort((arr1, arr2) => arr2[2] - arr1[2]);
        const currentBiggestElement = orderedMatrix.filter(arr => arr[1] === false)[0];

        const current2Dindex = flattenedMatrix.indexOf(currentBiggestElement);
        const currentColumnIndex = current2Dindex % matrix[0].length;
        const currentRowIndex = ((current2Dindex - currentColumnIndex) / matrix[0].length);

        const previousColumn = currentColumnIndex - 1 > -1;
        const nextColumn = currentColumnIndex + 1 < matrix[0].length;
        const previousRow = currentRowIndex - 1 > -1;
        const nextRow = currentRowIndex + 1 < matrix.length;

        const elements = [
            previousColumn && previousRow ? matrix[currentRowIndex - 1][currentColumnIndex - 1] : null,
            previousRow ? matrix[currentRowIndex - 1][currentColumnIndex] : null,
            previousRow && nextColumn ? matrix[currentRowIndex - 1][currentColumnIndex + 1] : null,
            previousColumn ? matrix[currentRowIndex][currentColumnIndex - 1] : null,
            matrix[currentRowIndex][currentColumnIndex],
            nextColumn ? matrix[currentRowIndex][currentColumnIndex + 1] : null,
            nextRow && previousColumn ? matrix[currentRowIndex + 1][currentColumnIndex - 1] : null,
            nextRow ? matrix[currentRowIndex + 1][currentColumnIndex] : null,
            nextRow && nextColumn ? matrix[currentRowIndex + 1][currentColumnIndex + 1] : null
        ].filter(x => x !== null);

        const newValue = average(...elements);
        matrix[currentRowIndex][currentColumnIndex] = newValue;
        flattenedMatrix[current2Dindex] = [newValue, true];
    }

    return matrix;
}


const matrixAfterSlidingWindowsFunc = slidingWindowsZscore(
    [
        [1, 19, 3, 4, 5],
        [6, 7, 20, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]
);


for (let row of matrixAfterSlidingWindowsFunc) {
    console.log(row.join(' | '));
} 
