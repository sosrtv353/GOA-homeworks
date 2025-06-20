let button = document.getElementById("button")
button.addEventListener('click',function() {
    alert("Hello! this is a alert message")
})

let hoveredP = document.getElementById("hoverP")
hoveredP.addEventListener('pointerover', function() {hoveredP.textContent="You hovered over me!"}
)

let backgroundDiv = document.getElementById("backgroundDiv")
backgroundDiv.addEventListener('click', function() {backgroundDiv.style.backgroundColor="lightgreen"})

let input = document.getElementById("inp")
input.addEventListener('click',function() {console.log(input.value)})

let image = document.getElementById("cookieImage")
let hiderButton = document.getElementById("hider")

hiderButton.addEventListener('click', function(){
    image.style.display="none"
})