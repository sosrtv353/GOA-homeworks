function evens(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10) {
    for (const n of arguments) {
        if (n % 2 == 0) {
            console.log(n)
        }
    }
}

evens(2,4,55,67,31,22,31,10,20,100)

// ეს არის ანონიმური რადგან ფუნქციას არ გააჩნია სახელი
const hello = function() {
    console.log("hello")
}

// არ არის
const hello2 = () => console.log("hello")


(() => console.log("Text"))()


// block function >
{
    let age = 14
}
console.log(age)
// error becuse of block scope (you cant access variable outside of code block)

{
    var name = "soso"
}
console.log(name)
// not error on var keyword defined variables 

// block function <

// global scope (they can always be accesed anywhere) >
let txt = "word"

console.log(txt)

function func() {
    console.log(txt)

}
func()

// global scope (they can always be accesed anywhere) <

function func2() {
    let v = 0
    console.log(v)
}
console.log(v)