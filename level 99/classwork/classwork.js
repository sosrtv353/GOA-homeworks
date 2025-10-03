const products = [
  { name: "Pen", price: 20 },
  { name: "Notebook", price: 120 },
  { name: "Pencil", price: 5 },
  { name: "Bag", price: 150 },
  { name: "Eraser", price: 15 }
];

const filtered = products.filter(product => product.price < 100);
console.log(filtered);


const words = ["apple", "cat", "banana", "ball", "orange"];

const firstBWord = words.find(word => word.startsWith("b"));
console.log(firstBWord);


const numbers = [10, 20, 30, 40, 50];

numbers.splice(2, 0, 99);
console.log(numbers);
