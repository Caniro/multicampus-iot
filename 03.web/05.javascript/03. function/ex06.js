// 변수 scope - 지역 변수
let scope2 = 'Global Variable'

function getValue2() {
  let scope2 = 'Local Variable' // 지역
  this_is_global = 'global' // 전역
  let this_is_local = 'local' // 지역
  return scope2
}

console.log(getValue2())
console.log(scope2)
console.log(this_is_global)
// console.log(this_is_local) // 에러
