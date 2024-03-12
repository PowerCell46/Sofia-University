const matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

function average(...args) {
    return args.reduce((acc, curr) => acc + curr, 0) / args.length;
}

// console.log(average(3, 5, 7));


function slidingWindows(matrix) {
    for (let index = 0; index < matrix.length; index++) {
        const currentRow = matrix[index]

        for (let xedni = 0; xedni < matrix[0].length; xedni++) {
            const currentElement = currentRow[xedni];
            const newCurrentElement = average(
                index - 1 > -1 && xedni - 1 > -1 ? matrix[index - 1][xedni - 1] : null, matrix[index - 1][xedni], matrix[index - 1][xedni + 1],
                matrix[index][xedni - 1], matrix[index][xedni], matrix[index][xedni + 1],
                matrix[index + 1][xedni - 1], matrix[index + 1][xedni], matrix[index + 1][xedni + 1]
            );
            console.log(currentElement, newCurrentElement);
        }
    }
}

slidingWindows(matrix);