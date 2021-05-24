function getTotal(numbers) {
    let total = 0;
    for (let i = 0; i < numbers.length; i++) {
        total += numbers[i];
    }
    return total;
}

const num1 = getTotal([1,2,3, 3]);
console.log(num1);

function isEvenNumber(number) {
    return number % 2 === 0;
}

console.log(isEvenNumber(num1))