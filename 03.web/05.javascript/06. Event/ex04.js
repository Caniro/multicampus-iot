// 이벤트 리스너 삭제

document.addEventListener('DOMContentLoaded', function() {
  let btn = document.getElementById('btn');
  let listener = function() {
    window.alert('안녕하세요, 자바스크립트!');
  };

  btn.addEventListener('click', listener, false);
  setTimeout(() => {
    console.log('3초 경과');
    btn.removeEventListener('click', listener, false);
  }, 3000);
}, false);
