for (let i = 0 ; i < 20; i++) {
    if (i === 13) {
        break
    }
    console.log(i)
}

let colors = ["red","green","yellow","blue","purple","black","white"]

for (let color of colors) {
    if (color == "blue") {
        break
    }
    console.log(color)
}

for (let c = 1; c < 50; c++) {
    if (c % 4 == 0 && c % 5 == 0) {
        break
    }
    console.log(c)
}

let academy = "Goa"
for (let letter of academy) {
    if (letter === "a") {
        break
    }
    console.log(letter)
}

let sums = 0
for (let s = 0; s < 100; s++) {
    if (sums >= 100) {
        break
    }
    sums+=s
}

for (let f = 0; f < 20; f++) {
    if (f === 13) {
        continue
    }
    console.log(f)
}

let fruits = ["apple","banana","strawberry","blueberry","peach","watermelon","cherry"]
for (let fruit of fruits) {
    if (fruit === "banana") {
        continue
    }
    console.log(fruit)
}

for (let n = 0; n < 30; n++) {
    if (n % 3 == 0) {
        continue
    }
    console.log(n)
}

let review = "very good academy"
for (let r of review) {
    if (r === "e") {
        continue
    }
    console.log(r)
}

for (let o = 0; o < 50; o++) {
    if (o % 2 == 0) {
        continue
    }
    console.log(o)
}

const add = (num1,num2) => num1 + num2
console.log(add(5,10))

const greet = name => "Hello," + " " + name + "!"
console.log(greet("Soso"))

const arrDoubler = arr => {
    let saver = []
    for (let number of arr) {
        saver.push(number * 2)
    }
    return saver
}
console.log(arrDoubler([1,5,6,20]))

const isEven = num => num % 2 == 0
console.log(isEven(98))

const stringLength = str => str.length
console.log(stringLength("arrtew"))