// 클래스명으로 선택
let list = document.getElementsByClassName('link')

console.log(list);
for(let i = 0; i < list.length; ++i) {
  console.log(list.item(i).href);
}
