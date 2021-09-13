// CSS 선택자를 통해 선택

let list = document.querySelectorAll('#list .external');

for (let i = 0; i < list.length; ++i) {
  console.log(list[i].href);
}
