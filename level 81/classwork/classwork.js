let sum=0
do {
    let userNum= Number(prompt("Enter number"))
    sum+=userNum
}
while (sum <= 100)



let myObj = {
    name: "David",
    surname: "Tezelashvili",
    academy: "GOA",
    isMentor: true,
    num: 100,
    hobbies: ["programming", "bike", "basketball"],
    favColor: "Blue"
}
let ul = document.getElementById("main-ul")
for (let key in myObj) {
    let li1 = document.createElement("li")
    let li2 = document.createElement("li")
    li1.textContent = String(key)
    li2.textContent = String(myObj[key])
    ul.appendChild(li1)
    ul.appendChild(li2)
}






let arr = ["soso","rtveliashvili",1,4,true,false]
for (let e of arr) {
    if (typeof e == "string") {
        console.log(e)
    }
    else if (typeof e == "number") {
        console.log(e + 10)
    }
    else if (typeof e == "boolean" && e == true) {
        console.log(false)
    }
    else {
        console.log(true)
    }
}
