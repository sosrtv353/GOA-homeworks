// console.log( 2 == 2)
// console.log(10 > 5)
// console.log(21 <= 21)
// console.log(50 != 50)
// console.log(99 >= 100)
// console.log(confirm("Are you 18 or older?"))

function confirmer() {
    let bool= confirm("You love Goa?")
    console.log(bool)
}
alert(confirm("Press ok or cancel"))
let form = document.getElementById("simpleform")
form.onsubmit=function username(e) {
    e.preventDefault()
    console.log("sshshsh")
    console.log(form.elements.username.value)

    
}
let button1 = document.getElementById("bt")
bt.onclick=function emailRefresh(e) {
    e.preventDefault()
    form.elements.email.value=""
    
}
let button2 = document.getElementById("bt2")
bt2.onclick= function phoneNum() {
    alert(form.elements.phonenumber.value)

}