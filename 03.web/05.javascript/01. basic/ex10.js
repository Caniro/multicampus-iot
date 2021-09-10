// for 반복문

// for ~ in
// 객체 - key를 순회한다.
// let data = {
//   apple: 150,
//   orange: 100,
//   banana: 120
// }
// for (let key in data) {
//   console.log(key + '=' + data[key])
// }

// 배열 - 인덱스를 순회한다.
let data = ['apple', 'orrange', 'banana']
for (let index in data) {
  console.log(index + '=' + data[index])
}

// for ~ of
// 열거 가능한 객체를 값으로 순회한다.
for (let value of data) {
  console.log(value)
}
