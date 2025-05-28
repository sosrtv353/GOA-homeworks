let myself = {
    name: "soso",
    surname: "rtveliashvili",
    academy: "Goa",
    city: "Tbilisi",
    role: "mini-leader",
    favcolor: "green",
    
    fullname() {
        console.log(this.name +" "+ surname)
    },
    color() {
        console.log(this.favcolor)
    }

}
myself.city="kaspi"
console.log(myself.city)
console.log(myself)
console.log(myself.academy)
myself.fullname()

function checking() {
    let check = document.Basic.check.checked;
    let check2 = document.Basic.anotheCheck.checked;
    console.log(check && check2);
    console.log(check || check2);
}
checking()