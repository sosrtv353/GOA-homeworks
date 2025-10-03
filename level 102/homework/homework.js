function randomDecimal() {
  return Math.random();
}

function rollDice() {
  return Math.floor(Math.random() * 6) + 1;
}

function flipCoin() {
  return Math.random() < 0.5 ? "Heads" : "Tails";
}

function generatePassword() {
  const chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  let password = "";
  for (let i = 0; i < 8; i++) {
    password += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return password;
}

function randomBoolean() {
  return Math.random() < 0.5;
}


function todaysDateNumber() {
  return new Date().getDate();
}

function birthdayDateNumber(month, day) {
  return new Date(new Date().getFullYear(), month - 1, day).getDate();
}

function isTodayFirst() {
  return new Date().getDate() === 1;
}

function todaysWeekdayNumber() {
  return new Date().getDay();
}

function birthdayWeekdayNumber(month, day) {
  return new Date(new Date().getFullYear(), month - 1, day).getDay();
}

function isTodaySunday() {
  return new Date().getDay() === 0;
}

function currentYear() {
  return new Date().getFullYear();
}

function birthdayYear(month, day) {
  return new Date(new Date().getFullYear(), month - 1, day).getFullYear();
}

function isYear2025() {
  return new Date().getFullYear() === 2025;
}

function currentHour() {
  return new Date().getHours();
}

function hourOfDate(date) {
  return date.getHours();
}

function isMorning() {
  return new Date().getHours() < 12;
}

function currentMinute() {
  return new Date().getMinutes();
}

function minuteOfDate(date) {
  return date.getMinutes();
}

function isStartOfHour() {
  return new Date().getMinutes() === 0;
}


const dateNow = new Date();
console.log(dateNow.getSeconds());

alert(new Date().getSeconds());

function getSeconds(date) {
  return date.getSeconds();
}

const date1 = new Date();
const date2 = new Date(Date.now() + 5000);
console.log(date1.getSeconds() === date2.getSeconds());

setInterval(() => {
  console.log(new Date().getSeconds());
}, 1000);

const monthNow = new Date();
console.log(monthNow.getMonth());

alert(new Date().getMonth());

function getMonth(date) {
  return date.getMonth();
}

const m1 = new Date('2025-01-01');
const m2 = new Date('2025-10-01');
console.log(m1.getMonth() === m2.getMonth());

setInterval(() => {
  console.log(new Date().getMonth());
}, 5000);
