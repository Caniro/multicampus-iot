-- DELETE : 행 단위로 삭제한다.
select * from testTbl4 where Fname='Aamer';
DELETE FROM testTbl4 WHERE Fname='Aamer';
select * from testTbl4 where Fname='Aamer';

-- 조건에 맞는 결과 중 상위의 몇개만 삭제할 수도 있다.
select * from testTbl4 where Fname='Mary';
DELETE FROM testTbl4 WHERE Fname='Mary' LIMIT 5;

-- 대용량의 데이터 삭제
create table bigTbl1 (select * from employees.employees);
create table bigTbl2 (select * from employees.employees);
create table bigTbl3 (select * from employees.employees);
delete from bigTbl1; -- AffectedRows : 300024, 트랜잭션 로그 기록, 느림
drop table bigTbl2; -- AffectedRows : 0, 테이블 자체를 삭제한다. 트랜잭션을 발생시키지 않음
truncate table bigTbl3; -- AffectedRows : 0, 테이블은 남기지만 트랜잭션 로그를 기록하지 않음
select * from bigTbl1;
select * from bigTbl2; -- DROP으로 테이블을 삭제했으므로 에러
select * from bigTbl3;
