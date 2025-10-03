let quotes = ["road of a thousand miles begins with a single step.","The toughest part of getting to the top of the ladder is getting through the crowd at the bottom.",
    "The toughest part of getting to the top of the ladder is getting through the crowd at the bottom.","If the going is easy, beware ... for you may be headed downhill.",
    "Do not follow where the path may lead. Go instead where there is no path and leave a trail.",
    "There is no chance, no fate, no destiny that can hinder a determined soul.",
    "If you have faith, even as small as a mustard seed, you can say to the mountain, 'Move from here to there' and it will move."
]
let colors = ["black","green","blue","red","purple","yellow","pink"]
const quoteButton = document.getElementById("quotebtn")
const quoteP = document.getElementById("quote")
quoteButton.addEventListener('click', function() {
    quoteP.textContent = quotes[Math.floor(Math.random() * quotes.length)]
    document.body.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)]
})