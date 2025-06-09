function userLoop() {
    let num1 = Number(prompt("Enter a number"))
    let num2 = Number(prompt("Enter a second number"))
    for (num1; num1 < num2; num1++) {
        console.log(num1)
    }


}
function changeElements() {
    console.log(document.getElementById("inp").value)
    let button = document.getElementById("submiter")
    let heading = document.getElementById("heading")
    button.style.backgroundColor="black"
    button.style.color="white"
    heading.style.textAlign="center"
    document.body.style.backgroundColor="green"
}
changeElements()