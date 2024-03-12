function average(...args) {
    return args.reduce((acc, curr) => acc + curr, 0) / args.length;
}


function slidingWindows(matrix) {
    for (let index = 0; index < matrix.length; index++) {
        const currentRow = matrix[index]

        for (let xedni = 0; xedni < matrix[0].length; xedni++) {
            const currentElement = currentRow[xedni];
            
            const previousColumn = xedni - 1 > -1; // column |
            const nextColumn = xedni + 1 < matrix[0].length; // column |
            const previousRow = index - 1 > -1; // row --
            const nextRow = index + 1 < matrix.length; // --

            const elements = [
                previousColumn && previousRow ? matrix[index - 1][xedni - 1] : null, // ↑ ←
                previousRow ? matrix[index - 1][xedni] : null, // ↑
                previousRow && nextColumn ? matrix[index - 1][xedni + 1] : null, // ↑ →
                    previousColumn ? matrix[index][xedni - 1] : null, // ←
                    currentElement, // .
                    nextColumn ? matrix[index][xedni + 1] : null, // →
                nextRow && previousColumn ? matrix[index + 1][xedni - 1] : null, // ↓ ←
                nextRow ? matrix[index + 1][xedni] : null, // ↓
                nextRow && nextColumn ? matrix[index + 1][xedni + 1] : null // ↓ →

            ].filter(x => x !== null);

            const newCurrentElement = average(...elements);
            matrix[index][xedni] = newCurrentElement;
        }
    }
    return matrix;
}


const matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]


const matrixAfterSlidingWindowsFunc = slidingWindows(matrix);


for (let row of matrixAfterSlidingWindowsFunc) {
    console.log(row.join(" | "));
}
