// 불특정 속성 취득

let logo = document.getElementById('logo');
let attrs = logo.attributes;

console.log(attrs['alt']);

console.log(attrs);
for (let i = 0; i < attrs.length; ++i) {
  let attr = attrs[i]; // 인덱스로도 추출 가능
  console.log(attr.name + ':' + attr.value);
}
