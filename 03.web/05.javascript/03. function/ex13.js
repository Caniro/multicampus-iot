// 인수 필수 처리 기법
function required() {
  throw new Error('인수가 부족합니다.')
}
function hoge(value=required()) {
  return value
}
try {
  hoge()
} catch (e) {
  console.log(e.message)
}
