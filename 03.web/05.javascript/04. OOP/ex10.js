// 동적으로 프로퍼티명 설정

let i = 0;
let member = {
  name: '김성룡',
  birth: new Date(1970, 5, 25),
  ['memo' + ++i]: '정규회원',
  ['memo' + ++i]: '지부회장',
  ['memo' + ++i]: '경기'
};

console.log(member);
