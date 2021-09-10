// 키워드 인수 (비구조화 할당)
function getTriangleArea({ base, height }) {
  return base * height / 2
}
console.log(getTriangleArea({ height: 4, base: 5 }))
