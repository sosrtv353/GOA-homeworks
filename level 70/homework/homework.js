for (let i = 1; i < 11; i++) {
    console.log(i)
}
counter = 2
while (counter < 21) {
    console.log(counter)
    counter++
}
for (let n = 10; n > 0; n-- ) {
    console.log(n)
}
let multiplies = 3
while (multiplies < 16) {
    console.log(multiplies)
    multiplies+=3
}

let text = "hello";
for (let char of text) {
    console.log(char);
}
function changetxt() {
    document.getElementById("txt").textContent="you clicked me.."
}
function divChange() {
    let div = document.getElementById("dv")
    div.style.backgroundColor="red"

}
function headingChange() {
    let heading = document.getElementById("h")
    heading.style.fontSize="50px"
    
}
function dissapear() {
    let dissapearDiv = document.getElementById("dissapearing")
    dissapearDiv.style.display = "none"

}



























