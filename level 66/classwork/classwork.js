function compareNums(num1, num2) {
    console.log(num1 > num2)
    console.log(num1 < num2)
    console.log(num1 >= num2)
    console.log(num1 <= num2)
    console.log(num1 == num2)
    console.log(num1 === num2)
    console.log(num1 != num2)
    console.log(num1 !== num2)
}
compareNums(4,4)
compareNums(10,100)
compareNums(0.99,1)

function formData(e) {
    e.preventDefault()
    let name= form.elements.name.value
    alert(name)
    
}