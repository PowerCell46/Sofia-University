function average(...args) {
    return args.reduce((acc, curr) => acc + curr, 0) / args.length;
}

// A different approach where the manipulation of the data isn't from top to bottom, left to right, 
// but finding the current biggest value 
// (if there are multiple we get the one that is closer to the beginning of the matrix)
// doing the calculation and continuing with the next biggest element until we have gone through all of them.

function slidingWindowsDesc(matrix) {
    let twoDMatrix = [];

    for (let row of matrix) {
        row.forEach(value => twoDMatrix.push([value, false]));
    }

    for (let index = 0; index < twoDMatrix.length; index++) {

        let orderedMatrix = twoDMatrix.slice();
        orderedMatrix.sort((arr1, arr2) => arr2[0] - arr1[0]);
        const currentBiggestElement = orderedMatrix.filter(arr => arr[1] === false)[0];

        const current2Dindex = twoDMatrix.indexOf(currentBiggestElement);
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
        twoDMatrix[current2Dindex] = [newValue, true];
    }

    return matrix;
}


const matrixAfterSlidingWindowsFunc = slidingWindowsDesc(
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
