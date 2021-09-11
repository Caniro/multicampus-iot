-- INSERT : 데이터 삽입
use sampledb;
CREATE TABLE testTbl1 (id int, userName char(3), age int);
INSERT INTO testTbl1 VALUES (1, '홍길동', 25);
INSERT INTO testTbl1(id, userName) VALUES (2, '설현');
INSERT INTO testTbl1(userName, age, id) VALUES ('초아', 26, 3);
select * from testTbl1;

-- AUTO_INCREMENT : 자동 증가. INSERT할 때는 NULL 입력
CREATE TABLE testTbl2
(
    id int AUTO_INCREMENT PRIMARY KEY,
    userName char(3),
    age int
);
INSERT INTO testTbl2 VALUES (NULL, '지민', 25);
INSERT INTO testTbl2 VALUES (NULL, '유나', 22);
INSERT INTO testTbl2 VALUES (NULL, '유경', 21);
SELECT * FROM testTbl2;

-- last_insert_id() : AUTO_INCREMENT 속성에서 마지막으로 입력된 값
select last_insert_id();

-- AUTO_INCREMENT 시작 값 변경
ALTER TABLE testTbl2 AUTO_INCREMENT=100;
INSERT INTO testTbl2 VALUES (NULL, '찬미', 23);
SELECT * FROM testTbl2;

-- @@auto_increment_increment : 증가값에 해당하는 서버 변수. 이 값만큼씩 증가함
CREATE TABLE testTbl3
(
    id int AUTO_INCREMENT PRIMARY KEY,
    userName char(3),
    age int
);
ALTER TABLE testTbl3 AUTO_INCREMENT=1000;
SET @@auto_increment_increment=3;
INSERT INTO testTbl3 VALUES (NULL, '나연', 20);
INSERT INTO testTbl3 VALUES (NULL, '정연', 18);
INSERT INTO testTbl3 VALUES (NULL, '모모', 19);
SELECT * FROM testTbl3;

-- 여러 데이터를 한번에 입력 가능
INSERT INTO testTbl3
    VALUES (NULL, '나연', 20), (NULL, '정연', 18), (NULL, '모모', 19);
SELECT * FROM testTbl3;

-- 서브쿼리를 통해 데이터를 한번에 입력할 수 있다.
CREATE TABLE testTbl4
(
    id int,
    Fname varchar(50),
    Lname varchar(50)
);
INSERT INTO testTbl4
    SELECT emp_no, first_name, last_name
    FROM employees.employees;
select * from testTbl4;

-- 위에서 했던 create table ... 서브쿼리 구문으로도 구현 가능
CREATE TABLE testTbl5
    (SELECT emp_no, first_name, last_name FROM employees.employees);

-- IGNORE : 앞에서 오류가 발생해도 계속 진행
drop table if exists memberTbl;
create table memberTbl (select userID, name, addr from userTbl LIMIT 3);
alter table memberTbl
    add constraint pk_memberTbl primary key (userID);
insert into memberTbl values('BBK', '비비코', '미국'); -- 이거 포함 3줄을 한번에 실행해보면 에러나서 적용안됨
insert into memberTbl values('SJH', '서장훈', '서울');
insert into memberTbl values('HJY', '현주엽', '경기');
select * from memberTbl;
insert ignore into memberTbl values('BBK', '비비코', '미국'); -- 여기서 에러나는데 아래는 정상 진행됨
insert ignore into memberTbl values('SJH', '서장훈', '서울');
insert ignore into memberTbl values('HJY', '현주엽', '경기');
select * from memberTbl;

-- ON DUPLICATE KEY : 기본 키가 중복될 경우 수행할 작업 지정
insert into memberTbl values('BBK', '비비코', '미국')
    on duplicate key update name='비비코', addr='미국';
select * from memberTbl;
