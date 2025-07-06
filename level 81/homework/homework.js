count = 1
do {
    console.log(count)
    count+=1
}
while (count == 5)

even = 2
do {
    console.log(even)
    even+=2
}
while (even == 10)

upsideCount = 10
do {
    console.log(upsideCount)
    upsideCount-=1
}
while (upsideCount == 1)

let sum=0
do {
    let userNum= Number(prompt("Enter number"))
    sum+=userNum
}
while (sum <= 100)

let sums = 0
let num = 1
do {
    sums+=num
    num+=1
}
while (num == 10)
console.log(sums)

let numArr = [1,2,3,4,5]
for (let n of numArr) {
    console.log(n)
}

let computer = "Computer"

for (let letter of computer) {
    console.log(letter)
}

numsSum = 0
for (let s of numArr) {
    s+=numsSum
}
console.log(numsSum)

let mixedNums = [1,3,4,5,77,13,15,18]
for (let numbers of mixedNums) {
    if (numbers % 2 == 0) {
        console.log(numbers)
    }
}

let names = ["soso","taso","nika","david","mari","nino","ana"]
for (let name of names) {
    console.log(name)
}

let obj = {
    job: "web developer",
    age: 33,
    hobby: "basketball"
}
for (let key in obj) {
    console.log(key)
}

for (let key in obj) {
    console.log(obj[key])
}

len = 0
for (let l in obj ) {
    len+=1
}

console.log(len)

for (let k in obj) {
    if ("name" in obj) {
        console.log("Key is in the object")
    }
    else {
        console.log("Key is not in the object")
    }
}


let strKey = ""

for (let keys in obj) {
    strKey+=keys+= " "
}
console.log(strKey.trim())