// addEventListener 메서드로 선언 - 여러 개 등록 가능

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('btn').addEventListener('click', function() {
    window.alert('버튼이 클릭되었다.');
  }, false);
}, false);

/*
 * 캡처링
 *   부모에서 자식으로 이벤트가 전파되는 것 (사용 빈도 낮음)
 * 버블링
 *   자식에서 부모로 이벤트가 전파되는 것
 */
