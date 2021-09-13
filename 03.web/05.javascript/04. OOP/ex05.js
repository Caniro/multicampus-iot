// class 프로퍼티

class Member {
  constructor(firstName, lastName) {
    this._firstName = firstName; // private 설정
    this._lastName = lastName;
  }

  get firstName() {
    return this._firstName;
  }

  set firstName(value) {
    this._firstName = value;
  }

  get lastName() {
    return this._lastName;
  }

  set lastName(value) {
    this._lastName = value;
  }

  getName() {
    return this.lastName + this.firstName; // getter 호출
  }
}

let m = new Member('시온', '정');
console.log(m.getName());
