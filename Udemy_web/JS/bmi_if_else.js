function bmiCalculator (weight, height) {
    var results = Math.round(weight/ (height*height));
    if (results < 18.5) {var interpretation = "Your BMI is "+ results +", so you are underweight."}
    if (results > 18.5 && results < 24.9) {var interpretation = "Your BMI is "+ results +",so you have a normal weight."}
    if (results > 24.9) {var interpretation = "Your BMI is "+ results +", so you are overweight."}
    return interpretation;
}

var bmi = bmiCalculator(65, 1.8); 
console.log(bmi)