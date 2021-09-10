// 변수 scope - 전역 변수
let value1 = 10
function decrementValue(value1) {
  value1--
  return value1
}
console.log(decrementValue(value1))
console.log(value1)
