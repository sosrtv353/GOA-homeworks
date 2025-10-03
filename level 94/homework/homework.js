let str1 = "JavaScript";
console.log(str1.at(0));

let str2 = "OpenAI";
console.log(str2.at(-1));

let str3 = "Programming";
console.log(str3.at(4));

function getMiddleChar(s) {
  let middleIndex = Math.floor(s.length / 2);
  return s.at(middleIndex);
}

console.log(getMiddleChar("example"));

let str4 = "Hello World";
console.log(str4.at(-2));

console.log("Hello".concat("World"));

console.log("Good".concat(" ", "Morning"));

console.log("Number: ".concat(String(42)));

console.log("How are you doing".concat("?"));

console.log("Test".concat(""));


console.log("Hello World".endsWith("World"));

console.log("filename.pdf".endsWith(".pdf"));

console.log("https://example.com/".endsWith("/"));

function endsWithS(word) {
  return word.endsWith("s");
}

console.log(endsWithS("cats"));  
console.log(endsWithS("dog"));   

console.log("JavaScript".endsWith("Java", 4));


