let count = 10
let timer = setInterval(function() {
    console.log(count)
    count-=1
    if (count < 0) {
        console.log("Times up!")
        clearInterval(timer)
    }
},1000)

let timeTracker = 0;
let currentWord = "Hello";

let titleChange = setInterval(function() {
    document.title = currentWord

    if (currentWord === "Hello") {
        currentWord = "Goodbye"
    } 
    else {
        currentWord = "Hello"
    }

    timeTracker +=1

    if (timeTracker == 6) {
        clearInterval(titleChange)
    }
}, 1000);


let div = document.getElementById("movingdiv")
let distance = 0

const interval = setInterval(() => {
    distance += 10
    div.style.transform = `translateX(${distance}px)`

    if (distance >= 100) {
        clearInterval(interval)
}
}, 200)

let generatedCount = 0
let randomNumGenerator = setInterval(function(){
    console.log(Math.floor(Math.random() * 10))
    if (generatedCount == 5) {
        clearInterval(randomNumGenerator)
    }
},1500)

let fruits = ['apple', 'banana', 'cherry'];

for (let i = 0; i < fruits.length; i++) {
  let upperWord = fruits[i].toUpperCase();
  console.log(upperWord);
}

let threeNums = [1,2,3]
threeNums[1] = 0
console.log(threeNums)

let programmingLanguages = ['Javascript', 'Python']
programmingLanguages[2] = 'C++'
programmingLanguages[3] = programmingLanguages[2]
programmingLanguages[2] = programmingLanguages[1]
programmingLanguages[1] = programmingLanguages[0]
programmingLanguages[0] = 'C#'
programmingLanguages.length = 3
console.log(programmingLanguages)


let arr = [10,20,25,40]    
let sum = 0
for (let s = 0; s < arr.length; s++) {
    sum+=arr[s]
}
alert(sum / arr.length)

let numbers = [5,10,15]
reverseNumbers = []
for (let r = 2; r >= 0; r--) {
    reverseNumbers.push(numbers[r])
}
console.log(reverseNumbers)

let food = ["Burger","Fried Chicken","Shaurma","Khinkali","Mtswadi"]
for (let f = 0; f < food.length; f++) {
    console.log(food[f])
}
