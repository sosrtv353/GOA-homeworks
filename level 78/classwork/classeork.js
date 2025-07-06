const paragraphs = document.getElementsByTagName("p")
let textontents = []
for (let i = 0; i < paragraphs.length; i++) {
    textontents[i] = paragraphs[i].textContent
}

const div1 = document.getElementById("div1")
let texts = ["hello","js","glass","world","typescript","python"]
for (let x = 0; x < 5; x++) {
    const p = document.createElement("p")
    p.textContent = texts[x] 
    div1.appendChild(p)
}

let div2 = document.getElementsByTagName("div")
const div2P = div2.getElementsByTagName("p")

for (let p = 0; p < div2P.length; p++) {
    div2P[p].style.color="green"
    div2P[p].style.backgroundColor="black"
}
