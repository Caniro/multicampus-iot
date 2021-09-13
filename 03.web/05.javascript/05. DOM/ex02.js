// 태그명으로 선택
let list = document.getElementsByTagName('a');

console.log('HTMLCollection : ', list);

for (let i = 0; i < list.length; ++i) {
  console.log(list.item(i).href);
  console.log(list[i].href);
};
