// 객체 리터럴
// 최상위 객체는 Object이며, 모든 객체는 Object를 상속한다.

let member = {
  name: '김성룡',
  birth: new Date(1970, 5, 25),
  toString() { // 오버라이딩
    return (this.name + '/생일： ' + 
            this.birth.toLocaleDateString());
  }
};

console.log(member);
console.log(member.toString);
console.log(member.toString());
console.log(String(member));
console.log(`${member}`);
console.log('---------------------------');

let member2 = {
  name: '정시온',
  birth: new Date(1970, 5, 25),
};

console.log(member2);
console.log(member2.toString); // 모든 객체는 toString 을 가지고 있음
console.log(member2.toString());
console.log(String(member2));
console.log(`${member2}`);
