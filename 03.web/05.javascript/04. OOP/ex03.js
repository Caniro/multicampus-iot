// this

function Member(firstName, lastName) {
  this.firstName = firstName;
  this.lastName = lastName;
}

// new를 빠뜨리면 단순 함수 호출이 되므로 결과가 달라진다.
let m = Member('인식', '정'); // this가 top level 객체(Window)
console.log(m);
console.log(firstName); // Window.firstName
// console.log(m.firstName); // 에러

// new를 쓰면 this는 새로운 인스턴스를 참조하게 된다.
let m2 = new Member('철수', '강');
console.log(m2);
console.log(firstName); // Window.firstName
console.log(m2.firstName);
