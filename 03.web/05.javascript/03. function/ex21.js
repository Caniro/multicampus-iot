// 클로저
function closure(init) {
  let counter = init;

  return function () { // 함수를 리턴
    return ++counter;
  }
}

let myClosure1 = closure(1);
let myClosure2 = closure(100);
console.log(myClosure1());
console.log(myClosure2());
console.log(myClosure1());
console.log(myClosure2());

/*
 * js 특징
 * 1. 인자를 체크하지 않는다.
 * 2. 나머지 연산자로 가변인수를 처리한다.
 * 3. 객체 분해로 키워드 인수를 전달한다.
 * 4. 익명 함수를 화살표 함수 형태로 자유롭게 사용할 수 있다.
 */
