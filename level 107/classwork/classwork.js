function getRandomNumberPromise() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const randomNumber = Math.random();
      if (randomNumber > 0.5) {
        resolve(`Resolve: ${randomNumber}`);
      } else {
        reject(`Reject: ${randomNumber}`);
      }
    }, 1000);
  });
}

getRandomNumberPromise()
  .then(result => {
    console.log(result);
  })
  .catch(error => {
    console.log(error);
  });


function resolver() {
     return new Promise((resolve, reject) => {
        resolve("resolved")
})}

Promise.all(resolver(),resolver(),resolver())
.then(result => console.log(result))



function workingOnPromise(str) {
  const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
      if (str.length > 5) {
        resolve(`Resolve: "${str}" has length ${str.length}`);
      } else {
        reject(`Reject: "${str}" has length ${str.length}`);
      }
    }, 500);
  });

  promise
    .then(result => {
      console.log(result);
    })
    .catch(error => {
      console.log(error);
    });
}

workingOnPromise("hello");
workingOnPromise("worldwide");
workingOnPromise("hi");

