function stringFunc(str) {
    return new Promise((res,rej)=> {
        setTimeout(() => {
            if (str.length % 2 == 0 ) {
                res(str)
            }
            else {rej(str)}
        }, 2000);
    })
}

let strs = [stringFunc("hello"),stringFunc("hi"),stringFunc("water")]
Promise.all(strs)
    .then(resolved => console.log(resolved))
    .catch(rejected => console.log(rejected))



fetch('https://goa-api.onrender.com/leaders/salary')
    .then(res => res.json())
    .then(jsonF => console.log(jsonF));


fetch('http://fakestoreapi.com/products') 
    .then(format => format.json)
    .then(returned => console.log(returned))

    