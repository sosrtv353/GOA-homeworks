function gettingUserName(e) {
    e.preventDefault()
    console.log(document.getElementById("name").value)

}

function concStrings() {
    let str1 = prompt("Please enter the first string:");
    let str2 = prompt("Please enter the second string:");
    let result = str1 + str2;
    alert(result);
}