// 비구조화 할당 (분할 대입)

let data = [56, 40, 26, 82, 19, 17, 73, 99]
let [x0, x1, x2, x3, x4, x5, x6, x7] = data

console.log(x0)
console.log(x1)
console.log(x2)
console.log(x3)
console.log(x4)
console.log(x5)
console.log(x6)
console.log(x7)

// 나머지 연산자
let data2 = [56, 40, 26, 82, 19, 17, 73, 99]
let [y0, y1, y2, ...y_other] = data2

console.log(y0)
console.log(y1)
console.log(y2)
console.log(y_other)

// 응용 : 가변 인수 처리
function f1(...arr) {
  console.log(arr)
}
f1([1, 2, 3])

// 객체
let book = {
  title: 'Java포켓 레퍼런스',
  publish: '기술평론사',
  price: 2680,
  other: {
    keywd: 'Java SE 8',
    logo: 'logo.jpg'
    }
}
let { price, title, memo = '없음' } = book
console.log(title)
console.log(price)
console.log(memo)

// 중첩
let { other, other: { keywd } } = book
console.log(other)
console.log(keywd)

// 별칭
let { title: name, publish: company} = book
console.log(name)
console.log(company)

