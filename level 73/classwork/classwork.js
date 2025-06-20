function addNewElement() {
    let mainDiv = document.getElementById("main-div")
    let element = document.createElement("button")
    let text = document.createTextNode("Click me")
    element.appendChild(text)
    mainDiv.appendChild(element)
}
addNewElement()

function removeNchange() {
    let paragraph = document.getElementById("para")
    let block = document.getElementById("contain")
    let button = document.getElementById("click")
    block.removeChild(button)
    let italic = document.createElement("i")
    italic.textContent="italy"
    block.replaceChild(italic,paragraph)

}
removeNchange()
