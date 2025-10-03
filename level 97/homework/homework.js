const dateStr = "2025-08-17";
const dateParts = dateStr.split("-");
console.log(dateParts);

const sentence = "one two three four five";
const wordsArray = sentence.split(" ");
console.log(wordsArray);

const csv = "John,Doe,25,Developer";
const csvArray = csv.split(",");
console.log(csvArray);

const chars = "abc".split("");
console.log(chars);

const phrase = "JavaScript is fun";
const wordList = phrase.split(" ");
console.log(wordList[1]);


function startsWithHello(str) {
  return str.startsWith("Hello");
}
console.log(startsWithHello("Hello there"));

function checkImageFile(filename) {
  return filename.startsWith("img_") ? "Image file" : "Not an image file";
}
console.log(checkImageFile("img_123.png"));

const sentence2 = "Once upon a time in a faraway land";
console.log(sentence2.startsWith("Once upon"));

function startsWithAt(str, substr, position) {
  return str.startsWith(substr, position);
}
console.log(startsWithAt("JavaScript is fun", "Script", 4));

function countDoctors(names) {
  return names.filter(name => name.startsWith("Dr.")).length;
}
console.log(countDoctors(["Dr. Smith", "Mr. Brown", "Dr. Adams", "Ms. Lee"]));


function cleanString(str) {
  return str.trim();
}
console.log(cleanString("   Hello world   "));

const withLeading = "   Leading space";
const cleanedStart = withLeading.trimStart();
console.log(cleanedStart);

const withTrailing = "Trailing space   ";
const cleanedEnd = withTrailing.trimEnd();
console.log(cleanedEnd);

function cleanUsernames(usernames) {
  return usernames.map(name => name.trim());
}
console.log(cleanUsernames(["  alice ", "bob  ", "  charlie  "]));

function isEmptyAfterTrim(input) {
  return input.trim() === "";
}
console.log(isEmptyAfterTrim("     "));


function allPassed(students) {
  return students.every(s => s.score >= 50);
}
console.log(allPassed([{name: "Alice", score: 60}, {name: "Bob", score: 55}, {name: "Eve", score: 49}]));

const numbers = [2, 4, 6, 8];
console.log(numbers.every(n => n % 2 === 0));

function allEmailsValid(emails) {
  return emails.every(email => email.includes("@"));
}
console.log(allEmailsValid(["user1@example.com", "user2@gmail.com", "invalidemail.com"]));

const ages = [20, 25, 30, 17];
console.log(ages.every(age => age >= 18));

const prices = [45, 80, 99, 100];
console.log(prices.every(price => price < 100));


