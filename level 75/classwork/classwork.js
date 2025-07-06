function nameAndSurname() {
    console.log("Soso Rtveliashvili")
}
let timer = setInterval(nameAndSurname,10000)

let button = document.getElementById("stop")
button.addEventListener('click', function(){
    clearInterval(timer)
})

const obj1 = {
    name: 'soso',
    surname: 'rtveliashvili'
}
const arr1 = ['string',33,true,obj1,[1,2,3]]
console.log(arr1)

function travserseArr(Arr) {
    for (let i = 0; i < Arr.length; i++)
        console.log(Arr[i])
}

travserseArr([1,"hello",false])
travserseArr([200,100,"String"])