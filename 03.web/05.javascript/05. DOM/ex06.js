// 노드 워킹 - 자식 노드 취득

let s = document.getElementById('food');
let opts = s.childNodes;
console.log(opts);

opts.forEach(opt => {
  if (opt.nodeType === 1) {  // 공백 노드를 걸러내기 위함
    console.log(opt.value);
  }
});

// for (let i = 0; i < opts.length; i++) {
//   let opt = opts.item(i);
//   if (opt.nodeType === 1) {
//     console.log(opt.value);
//   }
// }

/*
 * 노드 종류
 * 1: 요소 노드
 * 2: 속성 노드
 * 3: 텍스트 노드
 * 4: CDATA 섹션
 * 5: 실제 참조 노드
 * 6: 실제 선언 노드
 * 7: 처리 명령 노드
 * 8: 주석 노드
 * 9: 문서 노드
 * 10: 문서형 선언 노드
 * 11: 문서의 단편(fragment)
 * 12: 기법 선언 노드
 */
