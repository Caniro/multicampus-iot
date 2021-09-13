// ES2015 이전 방식의 객체지향

function Member(firstName, lastName) {
  this.firstName = firstName;
  this.lastName = lastName;

  this.getName = function() {
    return this.lastName + ' ' + this.firstName;
  };
}

let mem = new Member('철수', '강');
console.log(mem.getName());

// 동적 메서드 추가

mem.getLastName = function() {
  return this.lastName;
};

console.log(mem.getLastName());
