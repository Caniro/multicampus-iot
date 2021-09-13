// 클래스 조작
let elem = document.getElementById('toggle');

elem.addEventListener('click', function() {
  // 다른 클래스에 영향을 끼쳐서 좋지 않음
  // this.className = 
  //   (this.className === 'highlight' ? '' : 'highlight');
  this.classList.toggle('highlight');
}, false);
