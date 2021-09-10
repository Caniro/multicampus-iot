// 예외처리

let i = 1
try {
  i = i * j
} catch (e) {
  console.log(e.message)
} finally {
  console.log('처리 완료')
}

try {
  throw new Error('ㅇㅅㅇ')
} catch (e) {
  console.log(e.message)
}
