// 상속

class Member {
  constructor(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
  }

  getName() {
    return this.lastName + this.firstName;
  }
}

class BusinessMember extends Member {
  constructor(firstName, lastName, clazz) {
    super(firstName, lastName);
    this.clazz = clazz;
  }

  getName() {
    return super.getName() + ' / 직책: ' + this.clazz;
  }

  work() {
    return this.getName() + '은 일하고 있습니다.';
  }
}

let bm = new BusinessMember('시온', '정', '과장');
console.log(bm.getName());
console.log(bm.work());
