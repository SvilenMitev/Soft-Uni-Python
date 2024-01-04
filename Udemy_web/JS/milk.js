function getMilk (money) {
    return money % 1.5;
}

var change = getMilk(14);
console.log ("Your change is " + change)