paragraph = document.getElementById("first-paragraph")
paragraph.onmouseover = function() {paragraph.style.textAlign = "center"}


function func(e) {
    console.log(e.target)
    document.body.style.backgroundColor="black"
    paragraph.style.color="white"
}
button = document.getElementById("bt")
button.addEventListener('click',func(event) )

link = document.getElementById("link")
link.addEventListener(pointerover, function(e) {
    console.log(e.target.style,color)
    console.log(e.target.id)
    console.log(e.target)
})
