fetch("https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t=Arsenal")
    .then(response => response.json())
    .then(json => console.log(json))




async function randomNum() {
    return new Promise((res, rej) => {
        setTimeout(() => {
            const randNum = Math.random()
            if (randNum <= 0.5) {
                res("Success")
            } else {
                rej("Fail")
            }
        }, 2000)
    })
}

async function random() {
    try {
        const result = await random()
        console.log(result)
    }
    catch(err) {
        console.log(err)
    }
}



async function link() {
    return new Promise((res, rej) => {
        setTimeout(async () => { 
            try {
                const fetched = await fetch("https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t=Arsenal")
                const resultF = await fetched.json();
                console.log(resultF)
                res(resultF)
            } catch (error) {
                console.error(error)
                rej(error)
            }
        }, 3000)
    })
}
