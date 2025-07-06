let image  = document.getElementById('image')
let hider = document.getElementById('hide')
let shower = document.getElementById('show')

hider.addEventListener('click', function() {
    if (image.style.display == "none") {
        image.style.display="block"
    }
    else {image.style.display = "none"}
})

let evens = [2,4,6,8,10]
let timer = setInterval(function(){
    for (let i = 0; i < evens.length; i++) {
        console.log(i)
    }

},1000)

let change = [12,14,16,18,20]
for (let x = 0; x < evens.length; x++) {
    evens[x] = change[x]
}