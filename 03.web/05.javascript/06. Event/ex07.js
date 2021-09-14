// 키 정보 취득

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('key').addEventListener('keydown', function(e) {
    e.preventDefault();
    console.log('입력된 키:' + e.key);
    console.log('키 코드:' + e.keyCode);
  }, false);
}, false);
