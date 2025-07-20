const onlyPositives = (numArr) => {
    for (let p of numArr) {
        if (p > 0) {
            console.log(p)
        }
    }
}


const longerThanFiveLetters = (words) => {
    for (let l of words) {
        if (l.length > 5) {
            console.log(l)
            break
        }
    }
}

const sumUntilNegative = (numbers) => {
    let sum = 0
    for (let i of numbers) {
        if (i >= 0) {
            sum+=i
        }
        else {
            break 
        }
    }
    console.log(sum)
}

const noThreeMultiplies = (ints) => {
    for (let int of ints) {
        if (int % 3 == 0) {
            continue
        }
        console.log(int)
    }
}


const AaCounter = (words2) => {
    count = 0
    for (let w of words2)
        for (let w2 of w) {
            if (w2.toLowerCase == "a") {
                count++
            }
        }
    return count
}

const NoFourOrSixMultiplies = () => {
    for (let i = 0; i < 30; i++) {
        if (i % 4 == 0 || i % 6 == 0) {
            continue
        }
        console.log(i)
    }
}

const longerLengthThan8 = (txts) => {
    for (let t of txt) {
        if (t.length > 8) {
            return t
        }
    }
}

const OnlyOdds = (lst) => {
    oddSum = 0
    for (let o of lst) {
        if (o % 2 != 0) {
            oddSum++
        }
    }
    return oddSum
}

const onlyPositivesAndEvens = (Arr) => {
    for (let u of Arr) {
        if (u > 0 && u % 2 == 0) {
            console.log(p)
            
        }
    }
    
}
