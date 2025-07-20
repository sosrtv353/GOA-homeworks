let numbers = [4,10,25,21]
let sum = 0
for (let n of numbers) {
    if (sum >= 50) {
        break
    }
    sum+=n
}

const onlyFiveStr = str => {
    for (let s of str)
        if (s.length < 5) {
            continue
        }
        console.log(s)
}

onlyFiveStr(["GOA","tea","coffe","pizza","khinkali","academy","text",'MENU',"water","Laptop"])

const onlyevens = num => {
    let count = 0
    for (let i of num) {
        if (i % 2 != 0) continue
        if (count == 5) break
        console.log(i)
        count++
        
    }
    
}

