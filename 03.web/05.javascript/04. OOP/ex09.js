// 변수를 동일 명칭의 프로퍼티에 할당

let name = '김성룡';
let birth = new Date(1970, 5, 25);
// let member = { name: name, birth: birth };
let member = { name, birth };
console.log(member);
