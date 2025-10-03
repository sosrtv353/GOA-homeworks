const task = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Task complete");
  }, 3000);
});