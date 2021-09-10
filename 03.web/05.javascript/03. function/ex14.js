// 가변 길이 인수
function mySum(...numbers) { // 나머지 인수
  let result = 0;
  for (let num of numbers) {
    if (typeof num !== 'number') {
      throw new Error('지정값이 숫자가 아닙니다:' + num);
    }
    result += num;
  }
  return result;
}
try {
  console.log(mySum(1, 3, 5, 7, '9'));
} catch (e) {
  console.log(e.message);
}
// 대입문의 왼쪽이나 함수의 매개변수 자리에 있으면 나머지 연산자로 작동한다.
