// Array - splice
data = ['A', 'B', 'C', 'D', 'E']
console.log(data.splice(3, 2, 'F', 'G'))
console.log(data)
console.log(data.splice(3, 2))
console.log(data)
console.log(data.splice(1, 0, 'H'))
console.log(data)
// slice는 원본을 건드리지 않는다.

// Date 객체는 사용에 불편해서, 실전에서는 Moment 라이브러리를 사용한다.
