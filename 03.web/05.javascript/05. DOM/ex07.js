// 노드 워킹 - 자식 노드 취득

let s = document.getElementById('food');
let opt = s.firstChild;

while (opt) {
  if (opt.nodeType === 1) {
    console.log(opt.value);
  }
  opt = opt.nextSibling;
}

// 요소만 취득
let opt2 = s.firstElementChild;

while (opt2) {
  console.log(opt2.value);
  opt2 = opt2.nextElementSibling;
}
