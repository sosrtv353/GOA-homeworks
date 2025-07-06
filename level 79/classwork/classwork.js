let images = document.querySelectorAll("img")
images[0].src = "./newJava.png"

const divs = document.querySelectorAll("div")

divs.forEach(div => {
    let position = 0
    setInterval(() => {
    position += 5
    div.style.left = position + "px"
}, 100)
})

const box = document.getElementById("box");
const button = document.getElementById("moveBtn");
let leftPosition = 0;
button.addEventListener("click", () => {

      leftPosition += 10
      box.style.left = leftPosition + "px"


      let secondsPassed = 0;
      const colorInterval = setInterval(() => {
        box.style.backgroundColor = getRandomColor()
        secondsPassed++

        if (secondsPassed >= 10) {
          clearInterval(colorInterval)
        }
      }, 1000)
    })