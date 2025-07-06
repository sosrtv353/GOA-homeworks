let allP = document.querySelectorAll("p")
alert(allP.length)

let headingsLevel2 = document.querySelectorAll("h2")
for (let h2 = 0; h2 < headingsLevel2.length; h2++) {
    headingsLevel2[h2].style.color="blue"
}

let lists = document.querySelectorAll("li")
for (let li = 0; li < lists.length; li++) {
    console.log(lists[li].textContent)
}

let divs = document.querySelectorAll("div")
for (let d = 0; d < divs.length; d++) {
    divs[d].style.color="lightgray"
}

let images = document.querySelectorAll("img")
images[0].src='./image.png'

let highlights = document.getElementsByClassName("highlight")
for (let h = 0; h < highlights.length; h++) {
    highlights[h].style.backgroundColor="yellow"
}

console.log(document.getElementsByClassName("card").length)


let errors = document.getElementsByClassName("error")
for (let e = 0; e < errors.length; e++) {
    errors[e].style.color="red"
}

let items = document.getElementsByClassName("item")
for (let t = 0; t < items.length; t++) {
    console.log(items[t].innerHTML)
}

let buttons = document.getElementsByClassName("button") 
for (let b = 0; b < buttons.length; b++) {
    buttons[b].textContent = "clicked"
}

let movingDiv = document.getElementById("moving")
let position = 0
setInterval(() => {
    position += 5
    movingDiv.style.left = position + "px"
},100)