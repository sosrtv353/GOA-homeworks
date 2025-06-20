let body = document.body
let p = document.createElement("p")
p.textContent="Hello!"
body.appendChild(p)

let mainDiv = document.getElementById("main-div")
let heading1 = document.createElement("h1")
heading1.textContent="Hello!"
mainDiv.appendChild(heading1)

let goaImage = document.createElement("img")
goaImage.src="goa.png"
body.appendChild(goaImage) 

let button = document.createElement("button")
button.textContent="click me"
body.appendChild(button)

let unorderedList = document.getElementById("unordered")
let list1 = document.createElement("li")
let list2 = document.createElement("li")
let list3 = document.createElement("li")
list1.textContent="list 1"
list2.textContent="list 2"
list3.textContent="list 3"
unorderedList.appendChild(list1)
unorderedList.appendChild(list2)
unorderedList.appendChild(list3)

let Div = document.getElementById("content")
let DivHeading = document.getElementById("content-heading")
Div.removeChild(DivHeading)

let sportList=document.getElementById("sports")
let listItems = sportList.getElementsByTagName("li");
sportList.removeChild(listItems[2]); 

let container = document.getElementById("textContainer")
let upperP = document.getElementById("P")
let newParagraph = document.createElement("p")
newParagraph.textContent = "paragraph"
container.replaceChild(newParagraph,upperP)

let normalDiv = document.getElementById("normal-div")
let normalButton = document.getElementById("button")
let span = document.createElement("span")
span.style.backgroundColor="green"
span.textContent="span element"
normalDiv.replaceChild(span,normalButton)

let updatedListItem = document.createElement("li")
updatedListItem.textContent="Updated text: list item"
unorderedList.replaceChild(updatedListItem,list1)

let head2 = document.createElement("h2")
head2.textContent="i was turned into level 2 heading"
mainDiv.replaceChild(head2,heading1)






