// 인라인 스타일 접근
let elem = document.getElementById('elem');

elem.addEventListener('mouseover', function() {
  this.style.backgroundColor = 'Yellow';
}, false);

elem.addEventListener('mouseout', function() {
  this.style.backgroundColor = '';
}, false);
