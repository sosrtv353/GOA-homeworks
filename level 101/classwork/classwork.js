let name = "soso"
let letters = []
for (let i of name) {
    letters.push(i)
}
letters2 = letters.join("")
console.log(letters2)

function abs(number) {
    return number * -1
}
console.log(abs(-5))

for (let i = 1; i < 5; i++) {
    console.log(Math.pow(10,i))
}