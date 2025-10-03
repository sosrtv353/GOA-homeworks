let expr1 = prompt("Enter a math expression (e.g., '5+3'):");
alert("Result: " + eval(expr1));

let expr2 = prompt("Enter an expression with parentheses (e.g., '(8+2)*3'):");
alert("Result: " + eval(expr2));

let expr3 = prompt("Enter a division expression (e.g., '100/4'):");
alert("Result: " + eval(expr3));

let num = prompt("Enter a number to square:");
alert("Square: " + eval(num + "*" + num));

let exp = "20 - 7";
alert("Evaluating '20 - 7': " + eval(exp));


let input1 = prompt("Enter something:");
alert(isNaN(input1) ? "Not a number" : "It's a number");

let age = prompt("Enter your age:");
alert(isNaN(age) ? "Invalid age" : "Valid age");

let val1 = prompt("Enter first value:");
let val2 = prompt("Enter second value:");
alert("First is " + (isNaN(val1) ? "not a number" : "a number"));
alert("Second is " + (isNaN(val2) ? "not a number" : "a number"));

let anything = prompt("Type anything:");
alert(isNaN(anything) ? "That's text" : "That's a number");

let n1 = prompt("Enter first number:");
let n2 = prompt("Enter second number:");
let op = prompt("Enter operator (+, -, *, /):");

if (isNaN(n1) || isNaN(n2)) {
  alert("Invalid inputs");
} else {
  alert("Result: " + eval(n1 + op + n2));
}



let strNum = prompt("Enter a whole number as a string (e.g., '25'):");
alert("Converted number: " + parseInt(strNum));

let str1 = prompt("Enter first whole number as a string:");
let str2 = prompt("Enter second whole number as a string:");
alert("Sum: " + (parseInt(str1) + parseInt(str2)));

let pxVal = prompt("Enter a value like '55px':");
alert("Parsed number: " + parseInt(pxVal));

let valA = prompt("Enter a value like '20px':");
let valB = prompt("Enter another like '15.9':");
alert("Sum of parsed values: " + (parseInt(valA) + parseInt(valB)));

let hexVal = prompt("Enter a hex value like '0xF':");
alert("Converted value: " + parseInt(hexVal));



let price1 = prompt("Enter first item price (e.g., '19.99'):");
let price2 = prompt("Enter second item price (e.g., '5.50'):");
alert("Total price: " + (parseFloat(price1) + parseFloat(price2)));

let bill = prompt("Enter bill amount (e.g., '45.75'):");
let tipPercent = prompt("Enter tip percentage (e.g., '15'):");
let tip = parseFloat(bill) * (parseFloat(tipPercent) / 100);
alert("Tip: " + tip + "\nTotal: " + (parseFloat(bill) + tip));

let celsius = prompt("Enter temperature in Celsius (e.g., '36.6'):");
let fahrenheit = parseFloat(celsius) * 9/5 + 32;
alert("Fahrenheit: " + fahrenheit);

let weight = prompt("Enter weight in kg (e.g., '70.5'):");
let height = prompt("Enter height in meters (e.g., '1.75'):");
let bmi = parseFloat(weight) / (parseFloat(height) ** 2);
alert("BMI: " + bmi);

let distance = prompt("Enter distance traveled (e.g., '350.7'):");
let fuel = prompt("Enter fuel used (e.g., '28.5'):");
let efficiency = parseFloat(distance) / parseFloat(fuel);
alert("Kilometers per liter: " + efficiency);
