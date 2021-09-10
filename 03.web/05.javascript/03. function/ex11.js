// 인수 개수
function showMessage2(value) {
  if (arguments.length !== 1) {
    throw (new Error('인수의 수가 서로 다릅니다： ' +
                      arguments.length))
  }
  console.log(value)
}
try {
  showMessage2(' 철수', ' 영희')
} catch(e) {
  console.log(e.message)
}
