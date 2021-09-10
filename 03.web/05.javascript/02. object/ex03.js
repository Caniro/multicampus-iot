// Number 객체

let num1 = 255
console.log(num1.toString(16))
console.log(num1.toString(8))

let num2 = 123.45678
console.log(num2.toExponential(2))
console.log(num2.toFixed(3))
console.log(num2.toFixed(7))
console.log(num2.toPrecision(9))
console.log(num2.toPrecision(6))

let n = parseInt('123')
console.log(n, typeof n)

let f = parseFloat('23.567')
console.log(f, typeof f)
