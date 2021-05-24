const x = 1;
const y = 2;
const z = x + y; // 3;
// - + * /

const array1 = [1,2,3,4,5,6,7,8,9,10];

for(let i = 0; i < array1.length; i++) {
    // true && true = true;
    // true && false = false;
    // false && false = false;
    // false && true = false;
    if (i < 5 && array1[i] > 2) {
        console.log(i)
    }

    // true && true = true;
    // true && false = true;
    // false && false = false;
    // false && true = true;
    if (i < 5 || array1[i] > 2 ) {
        console.log(i)
    }
}