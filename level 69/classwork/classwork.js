function discountFunc(age) {
    age= Number(prompt("Whats your age"))
    if (age < 18) {
        alert("Discount: 20%")
    }
    else if (age <= 18 && age < 65) {
        alert("Discount: 5%")
    }
    else {alert("Discount: 10%")}
}

let count = 0
while (count < 100) {
    console.log("Iterating...")
    count+=5
}
for (let i = 0; i < 10; i++) {
    console.log("hello")
}