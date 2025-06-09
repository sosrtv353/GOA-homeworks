let num = Number(prompt("Enter number"))
if (num % 2 === 0) {
    console.log("Even")
}
else {
    console.log("Odd")
}
let score = Number(prompt("Whats your exam score?"))
if (score >= 90) {
    console.log("A")
}
else if (score >= 80 && score < 90) {
    console.log("B")
}
else if (score >= 70 && score < 80) {
    console.log("C")
}
else if (score >= 60 && score < 70) {
    console.log("D")
}
else {console.log("F")}

let n1 = Number(prompt("Enter number"))
let n2 = Number(prompt("Enter number"))
let n3 = Number(prompt("Enter number"))
if (n1 > n2 && n1 > n3) {
    console.log("First number is biggest")
}
else if (n2 > n1 && n2 > n3) {
    console.log("Second number is biggest")
}
else if (n3 > n2 && n3 > n1) {
    console.log("Third number is biggest")
}
else {console.log("They are same")}

let vowels = "aeiouAeiou"
let userC = prompt("Enter any charachter")
if (vowels.includes(userC)) {
    console.log("Vowel")
}
else {console.log("consonant")}

let number = Number(prompt("Enter any number"))
if (number % 3 == 0 && number % 5 == 0) {
    console.log("Divisible by both")
}
else if (number % 3 == 0 && number % 5 != 0) {
    console.log("Divisible by only 3")
}
else if (number % 3 != 0 && number % 5 == 0) {
    console.log("Divisible by only 5")
}
else {console.log("Divisible by both")}

let userage = prompt("Enter your age")
if (userage <= 12) {
    console.log("Child")
}
else if (userage > 12 && userage <= 19)  {
    console.log("Teenager")
}
else if (userage > 20 && userage <= 59)  {
    console.log("Adult")
}
else {console.log("Senior")}
let i = 2
while (i < 20) {
    console.log(i)
    i+= 1
}
let d = 11
while (d != 1) {
    d-= 1
    console.log(d)
}
for (let it = 1; it < 10; it++ ) {
    console.log(it)
}

for (let n = 3; n >15; n+=3) {
    console.log(n)
}
for (let is = 10; is < 1; is-- ) {
    console.log(it)
}
for (let even = 2; even < 21; even += 2) {
    console.log(even)
}
let sum = 0
for (let s = 1; s > 6; s++) {
    sum+=s
}
console.log(sum)