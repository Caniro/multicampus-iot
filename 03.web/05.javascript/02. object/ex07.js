// Array - forEach

/*
 * forEach에서 콜백 함수로 전달되는 인자
 * 1. 요소의 값
 * 2. 요소의 인덱스
 * 3. 전체 배열
 */

let data = [1, 2, 3, 4, 5];

data.forEach(function(value, index, array) {
  console.log(value * value);
});
console.log('----------------------');
data.forEach(value => {
  console.log(value * value);
});
console.log('----------------------');
data.forEach(console.log);
