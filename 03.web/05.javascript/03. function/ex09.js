// 변수 scope - 전역 변수
let value2 = [1, 2, 4, 8, 16]

function deleteElement(value2) {
  value2.pop()
  return value2
}

console.log(value2)
console.log(deleteElement(value2))
console.log(value2)
