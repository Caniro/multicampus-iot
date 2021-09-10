// 여러 개의 리턴값 (언팩)
function getMaxMin(...nums) {
  return [Math.max(...nums), Math.min(...nums)];
}

let result = getMaxMin(10, 35, -5, 78, 0);
console.log(result);

let [max, min] = getMaxMin(10, 35, -5, 78, 0);
console.log(max);
console.log(min);

// 두 번째 요소만 받기
let [,min2] = getMaxMin(1, 2, -10, 7, 3);
console.log(min2);