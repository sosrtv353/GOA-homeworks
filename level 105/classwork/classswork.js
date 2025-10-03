function hasKey(obj,key) {
    return Object.hasOwn(obj,key)
}

let person = {
    name: "josh",
    surname: "miller",
    country: "Usa"
}

let person2 = {
    name: "jack",
    surname: "james",
    country: "Usa"
}

let person3 = {
    name: "allen",
    surname: "pol",
    country: "poland"
}


hasKey(person,"country")
hasKey(person2,"password")
hasKey(person3,"money")


