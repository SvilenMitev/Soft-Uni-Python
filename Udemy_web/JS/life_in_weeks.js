function lifeInWeeks (age) {

    var yearsRamaining = 90 - age;
    var days = yearsRamaining * 365
    var weeks = yearsRamaining * 52
    var months = yearsRamaining * 12

    console.log("You have " + days + " days "  + weeks + " weeks, and " + months + " months left.");
}

lifeInWeeks(12)