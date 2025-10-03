const paragraph = document.querySelectorAll('p')[0]
const button = document.querySelectorAll('button')[0]
const strArray = ["hello","goodbye","welcome","goodnight","nice to meet you"]

button.addEventListener('click', function() {
    paragraph.textContent = `Random string from array: ${strArray[Math.floor(Math.random() * strArray.length)]}`
})

const paragraph2 = document.querySelectorAll('p')[1]
const button2 = document.querySelectorAll('button')[1]

const days = ["კვირა","ორშაბათი","სამშაბათი","ოთხშაბათი","ხუთშაბათი","პარასკევი","შაბათი"]
button2.addEventListener('click', function() {
    paragraph2.textContent = `Today: ${days[new Date().getDate()]}`
})

let time = setInterval(function() {
    let todayTime = new Date
    console.log(`${todayTime.getFullYear()} - ${todayTime.getMonth()} - ${todayTime.getHours()} - ${todayTime.getMinutes()} - ${todayTime.getSeconds()}`)

},1000)
