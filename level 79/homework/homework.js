let h1 = document.querySelectorAll("h1")
let h3 = document.querySelectorAll("h3")
h1[0].style.color="green"
h1[0].style.border="1px black solid"
h1[0].style.fontSize="30px"
for (let i = 0; i < h3.length; i++) {
    h3[i].style.color="green"
    h3[i].style.border="1px black solid"
    h3[i].style.fontSize="24px"
}

let paragraphs = document.querySelectorAll("p")
for (let p = 0; p < paragraphs.length; p++) {
    console.log(paragraphs[p].textContent.length)
}
let images = document.querySelectorAll("img")
for (let m = 0; m < images.length; m++) {
    if (images[m].alt == "cat") {
        images[m].style.border="1px orange solid"
    }

}

const circles = document.querySelectorAll(".circle")

circles.forEach(circle => {
    let position = 0
    setInterval(() => {
    position += 10
    circle.style.left = position + "px"
}, 200)
})

let listItems = document.querySelectorAll("li")
for (let index = 0; index < listItems.length; index++) {
    if (index % 2 == 0) {
        listItems[index].style.backgroundColor="skyblue"
    }
    else {
        listItems[index].style.backgroundColor="lightgray"
    }
}

const box = document.getElementById("box")
    const button = document.getElementById("moveBtn")

    let left = 0

    button.onclick = function() {
      left += 20;
      box.style.left = left + "px"
      box.style.backgroundColor = "green"
    }

const inputs = document.querySelectorAll('input[type="text"]')


    for (let i = 0; i < inputs.length; i++) {
      inputs[i].addEventListener("input", function() {
        if (inputs[i].value.length > 20) {
          inputs[i].style.backgroundColor = "red"
        } else {
          inputs[i].style.backgroundColor = "white"
        }
      })
    }

let listOrdered = document.getElementById("orderedlist")
let message=0
counter = 0
let interval = setInterval(function() {
    message+=1
    let element = document.createElement('li')
    element.textContent="message" + " " + String(message)
    listOrdered.appendChild(element)
    counter+=1
    if (counter == 10) {
        clearInterval(interval)
    }

})

const box2 = document.getElementById("myBox")
const button2 = document.getElementById("toggleBtn")
button2.onclick = function () {
      box2.style.display = "none"
      setTimeout(function () {
        box2.style.display = "block"
}, 5000)
}

 let tagName = prompt("Enter a tag name (like div, p, img):");

if (tagName) {
    tagName = tagName.toLowerCase();
    const elements = document.getElementsByTagName(tagName);
    const count = elements.length;
    alert(`There are ${count} <${tagName}> elements on this page.`);
} 
else {
      alert("You didn't enter a tag name.");
}