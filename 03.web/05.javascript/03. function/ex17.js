// 키워드 인수 - 비구조화 할당
function show({name}) {
  console.log(name);
};

let member = {
  mid: 'Y0001',
  name: '정시온',
  address: 'shion_jung@example.com'
};

show(member);
