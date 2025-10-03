function wordCount(word) {
    let trimmed = word.trim()
    return trimmed.split(" ").length
}



let strings = ["hi","txt","Goa","pencil"]
console.log(strings.every(str => typeof str == "string"))

let activity = [{status: "Active"},
    {status: "Active"},
    {status: "Active"},
    {status: "Active"},
    {status: "Offline"}

]

let activityChecker = () => {
    for (let i of activity) {
        if(i["status"] != "Active") {
            return false
            }
        }
    }


activity.every(activityChecker)
