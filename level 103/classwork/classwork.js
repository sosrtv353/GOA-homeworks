let correctAnswer = Math.floor(Math.random() * 2)
if (correctAnswer == 1) {
    alert("Arioli")
}
else if (correctAnswer == 2) {
    alert("Reshka")
    document.body.style.backgroundColor = "green"
}

let todayD = document.getElementById("date")
let time = setInterval(function() {
    todayD.textContent = `Todays date ${new Date}`
})
