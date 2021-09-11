-- UPDATE : 기존에 입력된 값을 변경한다.
UPDATE testTbl4
    SET Lname = '없음'
    WHERE Fname = 'Kyoichi';
select * from testTbl4 where Fname = 'Kyoichi';

-- 테이블 전체 행의 특정 열을 연산시킬 수도 있다.
select * from buyTbl2;
UPDATE buyTbl2 SET price = price * 1.5;
select * from buyTbl2;
