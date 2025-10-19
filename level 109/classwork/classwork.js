function numfunc(num) {
    return new Promise((res,rej) => {
    setTimeout(() => {
        if (num > 10) {
            res("resolve")
        }
        else {
            rej("reject")
        }
    }, 2000);
    })
}

async function asyncNum() {
    let resolvedV = await numfunc(11)
    console.log(resolvedV)
}

asyncNum()

