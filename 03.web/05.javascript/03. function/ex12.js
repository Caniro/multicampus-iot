// 인수 디폴트 값
function getTriangleArea6(base=1, height=1) {
  return base * height / 2
}
console.log(getTriangleArea6(10))
// 옛날버전 (ECMA2015 이전)
function getTriangleArea7(base, height) {
if (base === undefined) { base = 1 } // base = base || 1
if (height === undefined) { height = 1 } // height = height || 1
return base * height / 2
}
console.log(getTriangleArea7(10))
