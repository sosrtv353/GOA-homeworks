function alerter() {
    alert("ALERT! PRESS OK")
}
alerter()
function greet(name) {
    console.log("hello", name)
}
greet("soso")

function add(num, num2) {
    return num + num2
}
add(5,2)

function multiplier(divideBy) {
    return 10 / divideBy
}
multiplier(5)

function minus(number, minus) {
    alert( number - minus )
}
function redButton() {
    let redB = document.getElementById("redbutton")
    redB.style.backgroundColor="red"
}

function changeTxtContent() {
    let paragraph = document.getElementById("clickP")
    paragraph.textContent="Hey! you clicked me!"
}
