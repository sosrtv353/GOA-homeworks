let hobby = prompt("Whats your hobby?")
alert(hobby)
let name = prompt("Whats your name")
let surname = prompt("Whats your surname?")
alert("User full name:" + name + " "+ surname)
let message = prompt("Enter any message: ")
document.getElementById("txt").textContent=message
let favEmoji = prompt("What is your favorite emoji?")
alert("Thank you"+favEmoji)
let title = prompt("What would you like this websites title to be?")
document.title=title

function inputAlert(e) {
    e.preventDefault()
    alert(document.getElementById("inp").value)
}
function bgChange(e) {
    e.preventDefault()
    document.body.style.backgroundColor=document.getElementById("bg").value
}
function nameSurname(e) {
    e.preventDefault()
    let name2 = document.getElementById("name").value
    let lastname = document.getElementById("lastname").value
    document.getElementById("fullname").textContent=name2 + " " + lastname
}