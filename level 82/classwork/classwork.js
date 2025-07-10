function sumNumbers() {
    sum=0
    i=0
    while (i < 10) {
        i+=1
        if (i % 2 != 0) {
            continue
        }
        sum+=i
    }
}


day = Number(prompt("Enter any day of the week by number"))
switch (day) {
    case 1:
        console.log("Monday")
        break
    case 2:
        console.log("Tuesday")
         break
    case 3:
        console.log("Wednesday")
         break
    case 4:
        console.log("Thursday")
         break
    case 5:
        console.log("Friday")
         break
    case 6:
        console.log("Saturday")
         break
    case 7:
        console.log("Sunday")
         break
    default:
        console.log("Day not found")
}


const isEven = num => num % 2 == 0

