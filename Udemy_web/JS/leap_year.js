function isLeap(year) {

    /**************Don't change the code above****************/

    //Write your code here.    
    var status = "Not leap year."
    if (year % 4 == 0) {
        status = "Leap year."
        if (year % 100 == 0) {
            status = "Not leap year."
            if (year % 400 == 0) { status = "Leap year." }
        }
    }
    return status




    /**************Don't change the code below****************/

}

console.log(isLeap(2000))