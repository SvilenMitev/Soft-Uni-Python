
// const readline = require('readline');

// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout
// });

// rl.question('Enter your age: ', (humanAge) => {
//   const dogAge = (parseInt(humanAge, 10) - 2) * 4 + 21;
//   console.log("Your dog's age is approximately:", dogAge);
//   rl.close();
// });

function readNumber(input) {
    let hummanAge = Number(input[0]);

    let dogAge = (hummanAge-2)*4 + 21 ;
    console.log (dogAge);
}
readNumber([7])
