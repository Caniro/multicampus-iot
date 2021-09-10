// 변수 scope - 전역 변수
scope1 = 1
function getValue() {
  scope1 = 2 // 전역
  return scope1
}
console.log(scope1)
console.log(getValue())
console.log(scope1)
