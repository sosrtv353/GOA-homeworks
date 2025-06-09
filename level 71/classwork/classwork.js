let programmingLanguages = new Array("C++","Python","C#","Js")
console.log(programmingLanguages.length)
// ვხმარობთ new და Array ქივორდს რითიც ვქმნით სიას. იყენება უფრო კომპლექსურ დავალებებში

let fruits = ["apple","banana","orange","strawberry","pear"]
console.log(fruits.length)
// არ ვიყენებთ ქივორდებს და ისე ვქმნით სიას. უფრო სწრაფი ვერსია

let mixed = fruits.concat(programmingLanguages)
console.log(mixed)


let randomNum= Math.round(Math.random() * 100)
let guess = Number(prompt("Enter any number"))
while (randomNum != guess) {
    guess = Number(prompt("Wrong! try again: "))
}
console.log("Congrats!")


