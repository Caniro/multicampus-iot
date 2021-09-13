// ES2015 이후의 객체지향
// class 키워드

class Member {
  constructor(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
  }

  getName() {
    return this.lastName + this.firstName;
  }
}

// let m = Member('시온', '정'); // 에러
let m = new Member('시온', '정');
console.log(m.getName());
