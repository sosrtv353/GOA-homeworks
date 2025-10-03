const num1 = prompt("Enter a number: ")
const num2 = prompt("Enter a number: ")

for (let i of [num1,num2]) {
    if (isNaN(i)) {
        console.log("isnt a number")
    }
    else {
        console.log("is a number")
    }
}




let number1 = prompt("Enter any decimal number: ")
let number2 = prompt("Enter any decimal number: ")

parseInt(number1) + parseInt(number2) === parseFloat(number1) + parseFloat(number2)





const expression = prompt("Enter a expression: ")
const calculated = eval(expression)
console.log(`Original expression: ${expression}`)
console.log(`Result of expression: ${calculated}`)
console.log(`Integer version: ${parseInt(calculated)}`)
console.log(`Float version: ${parseFloat(calculated)}`)
