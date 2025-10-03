console.log("This is the first line of code in app.js.");
// Keep the line above as the first line of code
// Write your code here:

function usingSTO() {
  console.log("Hello World!")
}

setTimeout(usingSTO,2500)






// Keep the line below as the last line of code:
console.log("This is the last line of code in app.js.");



const {checkInventory} = require('./library.js');

const order = [['sunglasses', 1], ['bags', 2]];

// Write your code below:
function handleSuccess(resolveVal) {
  console.log(resolveVal)
}

function handleFailure(failureVal) {
  console.log(failureVal)
}

checkInventory(order).then(handleSuccess, handleFailure)




