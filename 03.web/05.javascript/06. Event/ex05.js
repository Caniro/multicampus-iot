// 이벤트 객체 사용

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('btn').addEventListener('click', function(e) {
    console.log(e);
    console.log('발생원:' + e.target.nodeName + '/' + e.target.id);
    console.log('종류:' + e.type);
  }, false);
}, false);
