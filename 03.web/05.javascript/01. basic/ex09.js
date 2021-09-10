// 키워드에 따른 변수의 scope 차이 (var vs let)

console.log(`x의 값은 ${x}`)

for (var x = 8; x < 10; ++x) { // var는 함수 scope
// for (let x = 8; x < 10; ++x) { // let은 블록 scope
  console.log(`x의 값은 ${x}`)
}

console.log(`x의 값은 ${x}`)

// const도 블록 scope
