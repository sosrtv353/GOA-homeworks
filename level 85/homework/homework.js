function arguments1(arg1,arg2,arg3) {
    for (let a of arguments) {
        console.log(a)
    }
}
arguments1("w","S","d")

function argumentCount(a1,a2,a3,a4,a5,a6,a7) {
    console.log(arguments.length)
}

argumentCount(1,2,3,4,5,6,7)

function numericSum(num,str,num2,bool) {
    let numSum = 0
    for (let n of arguments ) {
        if (typeof n == "number") {
            numSum+=n
        }
    }
    console.log(numSum)

}
numericSum(5,"string",11,false)

function NO_ZEROES(number1,number2,number3,number4,number5,number6) {
    for (let z of arguments) {
        if (z == 0){
            break
        }
        console.log(z)
    }
}
NO_ZEROES(1,3,22,45,0,32)

function logOnlyNums(uknownArg1,uknownArg2,uknownArg3,uknownArg4) {
    for (let l of arguments) {
        if (typeof l == "string") {
            continue
        }
        else {
            console.log(l)
        }
        
    }
}
logOnlyNums("soso","rtveliashvili",33,55)


const Multiply = function(integer, integer2) {
    return integer * integer2
}

let interval = setInterval(function(){
    console.log("2 seconds have passed")
},2000)

let button = document.getElementById("bt") 
button.addEventListener('click', function() {
    alert("ALERT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
})

(() => {
    console.log("Hello world!")
})()

((sqNum) => {
    return sqNum * sqNum
})(5)

((numbers) => {
    return numbers.reduce((total, num) => total + num, 0)
})()



function nums() {
    Numbers = [1,2,3,4,5,6,7,8,9,10]
    console.log(Numbers)
}
console.log(Numbers) 
// error becuse of function scope. you cant access variable thats inside a function outside of function

let fruit = "Apple"
console.log(fruit) // Apple

function juice() {
    fruit = "Banana"
    console.log(fruit) // Banana
}


{
    let a = "a"
    const b = "b"
    var c = "c"
}
console.log(a)
console.log(b)
console.log(c)
 // only c is printed

function example() {
    let car = "mercedes"
    const pi = 3.14
    var isAdmin = true
}
console.log(car)
console.log(pi)
console.log(isAdmin)
// none of them is printed
