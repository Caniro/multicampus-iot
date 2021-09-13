// Array - sort
// 참고 : <https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/sort>

let ary = [5, 25, 10];

console.log(ary.sort()); // 기본은 문자열로 간주하여 처리
console.log(ary);        // 원본이 바뀜
console.log(ary.sort((x, y) => x - y));
console.log(ary.sort((x, y) => y - x));
console.log('---------------------------------------');

let classes = ['부장', '과장', '주임', '담당'];
let members = [
  { 'name': '남상미', 'class': '주임' },
  { 'name': '김준수', 'class': '부장' },
  { 'name': '정인식', 'class': '담당' },
  { 'name': '남궁민', 'class': '과장' },
  { 'name': '이상주', 'class': '담당' },
];

members.sort(function(x, y) {
  return classes.indexOf(x.class) - classes.indexOf(y.class);
});
console.log(members);
console.log('---------------------------------------');

members.sort(function(x, y) {
  return x.name === y.name ? 0 : (x.name > y.name ? 1 : -1);
});
console.log(members);
