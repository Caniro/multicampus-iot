// 정적 메서드

class Area {
  static getTriangleArea(base, height) {
    return base * height / 2;
  }
}

console.log(Area.getTriangleArea(10, 5));
