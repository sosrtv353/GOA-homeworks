// let randomNum = Math.round(Math.random() * 100)
// let userNum = Number(prompt("შეიყვაეთ სასურველი რიცხვი"))
// alert((randomNum))
// while (true) {
//     let userNum =  Number(prompt("შეიყვაეთ სასურველი რიცხვი"))
//     if (userNum > randomNum) {
//         alert("მეტია")
//     }
//     else if (userNum < randomNum) {
//         alert("ნაკლებია")
//     }
//     else if (userNum == randomNum) {
//         alert("ტოლია")
//         break
//     }
// }


let fruits = ["apple","orange","banana","lemon","pear","grape"]
console.log(fruits[0] + " " + fruits[5])
console.log(fruits.length)

let colors = ["red", "green", "blue"];
colors[3] = "yellow"
colors[0] = "purple"
console.log(colors)

// მეორე გზაც:
let colors2 = ["red", "green", "blue"];
colors2.push("yellow")
colors2.shift()
colors2.unshift("purple")
console.log(colors2)

let arr = [1,5,6,9,14]
for (let i = 0; i < arr.length; i++) {
    console.log(arr[i] * 2)
}

function sumArray(arr) {
    let sum = 0
    for (let c = 0; c < arr.length; c++) {
        sum+= arr[c]
    }
    return sum
}

function maxArray(arr2) {
    let max = arr2[0]
    for (let m = 0; m < arr2.length; m++) {
        if (arr2[m] > max) {
            max=arr2[m]
        }
    }
    return max
}

let favMovies = ["movie1","movie2","movie3","movie4","movie5"]
let usersMovie = prompt("Enter your favorite movie")
if (favMovies.includes(usersMovie)) {
    alert("Yes, its one of my favorites!")
}
else {alert("No, i dont like that one much")}

let words = ["banana", "apple", "pear", "orange"];
words.sort();
let result = words.join(", "); 
console.log(result);

console.log(Math.floor(Math.random() * 10 ) + 1)

let decimal = prompt("Enter a decimal number (something like 5.5)")
alert("rounded:"+" "+ Math.round(decimal))
alert("rounded up:"+" "+ Math.ceil(decimal))
alert("rounded down:"+" "+ Math.floor(decimal))

let nums = [3,7,10,21,5,40]
console.log(Math.max(nums))
console.log(Math.min(nums))
