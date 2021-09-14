// 이벤트 전달 방지

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('inner').addEventListener('click', function(e) {
    window.alert('#inner리스너가 발생하였다.');
    e.stopPropagation(); // 이 DOM의 모든 리스너까지는 작동
    // e.stopImmediatePropagation(); // 이 리스너까지만 작동 (다른 리스너로 전파 X)
    // e.preventDefault(); // 모든 리스너는 동작, 디폴트 동작만 막음
  }, false);
  document.getElementById('inner').addEventListener('click', function(e) {
    window.alert('#inner리스너2가 발생하였다.');
  }, false);
  document.getElementById('outer').addEventListener('click', function(e) {
    window.alert('#outer리스너가 발생하였다.');
  }, false);
}, false);

/*
 * stopPropagation : 버블링 방지 (부모로 전파 X)
 * stopImmediatePropagation : 전파 방지 (다른 리스너나 부모로 전파 X)
 * preventDefault : 디폴트 동작 방지
 */
