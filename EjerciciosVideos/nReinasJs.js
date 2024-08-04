class QueenPosition{
    constructor(rowIndex, columnIndex){
        this.rowIndex = rowIndex
        this.columnIndex = columnIndex
    }

    get leftDiagonal(){
        return this.rowIndex - this.columnIndex
    }

    get rigthDiagonal(){
        return this.rowIndex + this.columnIndex
    }
}


function isSafe(queensPsition, rowIndex, columnIndex){
    const newQueenPosition = new QueenPosition(rowIndex, columnIndex)

    for(let queenIndex = 0; queenIndex < queensPsition.length; queenIndex +=1){
        const currentPosition = queensPsition[queenIndex]

        if(
            currentPosition &&
            (
                newQueenPosition.columnIndex === currentPosition.columnIndex ||
                newQueenPosition.rowIndex === currentPosition.rowIndex ||
                newQueenPosition.leftDiagonal === currentPosition.leftDiagonal ||
                newQueenPosition.rigthDiagonal === currentPosition.rigthDiagonal
            )
        ){
            return false
        }
    }

    return true
}

function allQueensSet(queensPositions){
    return queensPositions.every(position => position !== null)
}

function nQueensRecursive(solutions, previosQueensPositions, queensCount, columIndex){
    const queenPositions = [...previosQueensPositions].map(queenPosition => {
        return !queenPosition ? queenPosition : new QueenPosition(queenPosition.rowIndex, queenPosition.columIndex)
    })

    if(allQueensSet(queenPositions)){
        solutions.push(queenPositions)
        return true
    }

    for(let rowIndex = 0; rowIndex < queensCount; rowIndex +=1){
        if(isSafe(queenPositions, rowIndex, columIndex)){
            queenPositions[rowIndex] = new QueenPosition (rowIndex, columIndex)

            nQueensRecursive(solutions, queenPositions, queensCount, columIndex + 1)

            queenPositions[rowIndex] = null
        }
    }


}

function nQueens(queensCount){
    const queensPositions = Array(queensCount).fill(null)
    const solutions = []

    nQueensRecursive(solutions, queensPositions, queensCount, 0)
    return solutions
}






const reults = nQueens(4)
console.log(reults)