let str1 = prompt("Enter string: ")
let str2 = prompt("Enter another string: ")
console.log(str1.concat(str2,""))

let word1 = prompt("Enter string: ")
let word2 = prompt("Enter string: ")
let word3 = prompt("Enter string: ")
console.log(word1.concat(word2,word3,""))


let w1 = "happy"
let w2 = "birthday!"

console.log(w1.concat(" ",w2))




let url = prompt("Enter Url: ")
if (url.endsWith("/")) {
    console.log("Url ends with /")
}
else {console.log("Url dosent end with /")}


function endWithS(word) {
    console.log(word.endsWith("s"))
}


function punctuation(text) {
    return text.endsWith(".") || text.endsWith("?") || text.endsWith("!")
}

