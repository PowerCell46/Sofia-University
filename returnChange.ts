interface MachineCoins {
    200: number,
    100: number,
    50: number,
    20: number,
    10: number,
    5: number,
    2: number,
    1: number
};


function returnChange(returnAmount: number, machineCoins: MachineCoins): boolean {
    returnAmount *= 100;

    const returnedMoney: MachineCoins = {
        200: 0,
        100: 0,
        50: 0,
        20: 0,
        10: 0,
        5: 0,
        2: 0,
        1: 0
    }

    for (let currentCoin of Object.keys(returnedMoney).reverse()) {
        while (returnAmount >= Number(currentCoin) && machineCoins[Number(currentCoin)] > 0) {
            returnAmount -= Number(currentCoin);
            returnedMoney[Number(currentCoin)]++;
            machineCoins[Number(currentCoin)]--;
        }
    }

    for (let currentCoin of Object.keys(returnedMoney).reverse()) {
        console.log(`Coin: ${currentCoin}, Amount: ${returnedMoney[currentCoin]}.`);
    }

    return returnAmount === 0;
} 


const machineCoins: MachineCoins = {
    200: 1,
    100: 10,
    50: 5,
    20: 10,
    10: 10,
    5: 50,
    2: 10,
    1: 100 
};

console.log(returnChange(4.03, machineCoins));
