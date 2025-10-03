const sentence = "The quick brown fox jumps over the lazy dog";
console.log(sentence.includes("dog"));

function hasAtSymbol(str) {
  return str.includes("@");
}
console.log(hasAtSymbol("example@email.com"));

const lang = "JavaScript";
console.log(lang.includes("Java"));

const fruit = "pineapple";
console.log(fruit.includes("apple"));

function containsNot(str) {
  return str.includes("not");
}
console.log(containsNot("This is not good"));


const text = "The quick brown fox jumps over the lazy dog";
console.log(text.indexOf("fox"));

const greeting = "Hello world";
console.log(greeting.indexOf("o"));

const message = "Happy New Year 2025!";
console.log(message.indexOf("2025"));

const testStr = "This is a simple test";
console.log(testStr.indexOf("is"));

function findAtSymbol(str) {
  return str.indexOf("@");
}
console.log(findAtSymbol("user@example.com"));


const str1 = "Hello world";
console.log(str1.lastIndexOf("o"));

const str2 = "banana";
console.log(str2.lastIndexOf("a"));

const str3 = "This is a test, and it is simple";
console.log(str3.lastIndexOf("is"));

const str4 = "dog dog dog";
console.log(str4.lastIndexOf("dog"));

const str5 = "Happy 2025, welcome 2025!";
console.log(str5.lastIndexOf("2025"));


const laugh = "ha".repeat(3);
console.log(laugh);

const stars = "*".repeat(10);
console.log(stars);

const dashedLine = "---".repeat(5);
console.log(dashedLine);

function repeatWord(word, n) {
  return word.repeat(n);
}
console.log(repeatWord("echo", 3));

const helloRepeat = "Hello ".repeat(4);
console.log(helloRepeat);


const sentence1 = "The cat chased the cat";
console.log(sentence1.replace("cat", "dog"));

const sentence2 = "JavaScript is cool";
console.log(sentence2.replace("Java", "Type"));

function replaceFirstSpace(str) {
  return str.replace(" ", "-");
}
console.log(replaceFirstSpace("Hello world"));

const word = "banana";
console.log(word.replace("a", "@"));

const newYear = "Happy New Year 2024!";
console.log(newYear.replace("2024", "2025"));


const text1 = "The cat chased another cat and found a cat";
console.log(text1.replaceAll("cat", "dog"));

const text2 = "I love JavaScript so much";
console.log(text2.replaceAll(" ", "-"));

const text3 = "banana";
console.log(text3.replaceAll("a", "@"));

const text4 = "2024 was great, but 2024 is over";
console.log(text4.replaceAll("2024", "2025"));

const text5 = "Wait. Stop. Go. Run.";
console.log(text5.replaceAll(".", "!"));


const greetingStr = "Hello world";
console.log(greetingStr.slice(6));

const frameworkName = "JavaScript";
console.log(frameworkName.slice(0, 4));

const languageName = "Python";
console.log(languageName.slice(1));

const fruitName = "Banana";
console.log(fruitName.slice(-3));

function getFirstHalf(textStr) {
  return textStr.slice(0, Math.floor(textStr.length / 2));
}
console.log(getFirstHalf("Sunshine"));

