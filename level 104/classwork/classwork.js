class Bank {
    constructor(username,balance){
        this.username = username
        this.balance = 0
    }
    deposit(money) {
        this.balance += money
    }
}

let myAcc = new Bank("Soso123",50)
myAcc.deposit(30)


class Car {
    constructor(brand, model) {
        this.brand = brand
        this.model = model
    }
    start() {
        console.log(`${brand} ${model} is running`)
    }
    }

    