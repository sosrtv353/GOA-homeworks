let count = 0
let counter = setInterval(function() {
    count++
    console.log(count)
    if (count == 5) {
        clearInterval(counter)
    }
}, 1000)

let count2 = 0
time = setInterval(function() {
    count2 += 2
    console.log(count)
    if (count == 10) {
        clearInterval(time)
    }
},2000)

document.body.style.transition = "background-color 1s ease"
let colors = ["red","blue","green","orange","purple"]
counting = 0
let colorChange = setInterval(function() {
    document.body.style.backgroundColor = colors[counting]
    counting+=1
    if (counting == colors.length) {
        clearInterval(colorChange)
    }
},3000)

let stopTime = 0
let currentTime = setInterval(function() {
    let currentDate = new Date
    console.log(currentDate)
    count++
    if (count == 15) {
        clearInterval(currentTime)
    }
},1000)

let count3 = 1
let t = setInterval(function(){
    console.log(count3)
    count3+=1

    if (count3 == 11) {
        clearInterval(t)
    }
},1000)

let nums = [1,2,3,4,5]
console.log(nums[1])

nums[0] = 100
console.log(nums)

let words = ["text","file","meniu"]
console.log(words[0],words[1],words[2])

let numbers = [21,34,25,40,100]
console.log(numbers[0] + numbers[numbers.length - 1])