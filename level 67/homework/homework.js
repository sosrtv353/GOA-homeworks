let empty = {}
let me = {
    name: "soso",
    age: 14,
    city: "Tbilisi"
}
let myName= me.name
me.surname="Rtveliashvili"

let user = {
    location: "Usa",
    client: true,
    username:"dav33",
    userFullInfo() {
        let info = {
            Name: "David",
            lastname: "Cooper",
            age: 25
        }
        console.log(info)
    }

}
me.city="Kaspi"
console.log(20 > 10 && 15 > 10)
console.log(10 == 10 || 10==11)
console.log(10!=11)
console.log(10 == 10 || 10==11 && 20 > 10 && 15 > 10)
let price = String(17)
let truth = String(true)
let num = Number("111")
let lie = Number(false)

console.log(Number("Hello")) 
// it will cause a error