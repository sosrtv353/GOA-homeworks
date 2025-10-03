function coinflip(resolve, reject) {
    if (Math.random() < 0.5) {
        reject("Tail")
    } else {
        resolve("Head")
    }
}

function randomStringCheck() {
    const strings = ["apple", "banana", "kiwi", "orange", "grape"]

    return new Promise((resolve, reject) => {
        const randomIndex = Math.floor(Math.random() * strings.length)
        const selected = strings[randomIndex]

        console.log("Selected string:", selected)

        if (selected.length % 2 === 0) {
            resolve("success")
        } else {
            reject("failure")
        }
    })
}

randomStringCheck()
    .then(result => console.log(result))
    .catch(error => console.log(error))
