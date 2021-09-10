// 호이스팅, let으로 선언하면 선언 이후부터 사용가능
var scope3 = 'Global Variable'
function getValue3() {
  console.log(scope3)
  var scope3 = 'Local Variable'
  return scope3
}
console.log(getValue3())
console.log(scope3)

// Strict mode, 모든 변수를 선언 후 사용하도록 강제한다.
// 스크립트 최상단에 'use strict' 를 작성하면 된다.
