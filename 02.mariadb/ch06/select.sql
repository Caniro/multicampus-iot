-- DB 사용 선언
use employees;

-- 내용 전체 가져오기
select * from titles;
select * from employees.titles;

-- 특정 컬럼 가져오기
select first_name from employees;
select first_name, last_name, gender from employees;

-- 전체 데이터베이스 조회
show databases;
use employees;
-- 전체 테이블 이름만 조회
show tables;

-- 전체 테이블 정보 상세 조회
show table status;

-- 테이블 컬럼 정보 조회
desc employees;

-- 컬럼 별칭(alias) 지정
select first_name as 이름, hire_date '회사 입사일' from employees;

-- 샘플 DB 생성
drop database if exists sampledb;
create database sampledb;
use sampledb;
create table userTbl -- 회원 테이블
(
    userID      CHAR(8) NOT NULL PRIMARY KEY,
    name        VARCHAR(10) NOT NULL,
    birthYear   INT NOT NULL,
    addr        CHAR(2) NOT NULL,
    mobile1     CHAR(3),
    mobile2     CHAR(8),
    height      SMALLINT,
    mDate       DATE
);
create table buyTbl -- 구매 테이블
(
    num         INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    userID      CHAR(8) NOT NULL,
    prodName    CHAR(6) NOT NULL,
    groupName   CHAR(4),
    price       INT NOT NULL,
    amount      SMALLINT NOT NULL,
    FOREIGN KEY (userID) REFERENCES userTbl(userID)
);
INSERT INTO userTbl VALUES('LSG', N'이승기', 1987, N'서울', '011', '11111111', 182, '2008-8-8');
INSERT INTO userTbl VALUES('KBS', N'김범수', 1979, N'경남', '011', '22222222', 173, '2012-4-4');
INSERT INTO userTbl VALUES('KKH', N'김경호', 1971, N'전남', '019', '33333333', 177, '2007-7-7');
INSERT INTO userTbl VALUES('JYP', N'조용필', 1950, N'경기', '011', '44444444', 166, '2009-4-4');
INSERT INTO userTbl VALUES('SSK', N'성시경', 1979, N'서울', NULL , NULL , 186, '2013-12-12');
INSERT INTO userTbl VALUES('LJB', N'임재범', 1963, N'서울', '016', '66666666', 182, '2009-9-9');
INSERT INTO userTbl VALUES('YJS', N'윤종신', 1969, N'경남', NULL, NULL , 170, '2005-5-5');
INSERT INTO userTbl VALUES('EJW', N'은지원', 1972, N'경북', '011', '88888888', 174, '2014-3-3');
INSERT INTO userTbl VALUES('JKW', N'조관우', 1965, N'경기', '018', '99999999', 172, '2010-10-10');
INSERT INTO userTbl VALUES('BBK', N'바비킴', 1973, N'서울', '010', '00000000', 176, '2013-5-5');
INSERT INTO buyTbl VALUES(NULL, 'KBS', N'운동화', NULL, 30, 2);
INSERT INTO buyTbl VALUES(NULL, 'KBS', N'노트북', N'전자', 1000, 1);
INSERT INTO buyTbl VALUES(NULL, 'JYP', N'모니터', N'전자', 200, 1);
INSERT INTO buyTbl VALUES(NULL, 'BBK', N'모니터', N'전자', 200, 5);
INSERT INTO buyTbl VALUES(NULL, 'KBS', N'청바지', N'의류', 50, 3);
INSERT INTO buyTbl VALUES(NULL, 'BBK', N'메모리', N'전자', 80, 10);
INSERT INTO buyTbl VALUES(NULL, 'SSK', N'책', N'서적', 15, 5);
INSERT INTO buyTbl VALUES(NULL, 'EJW', N'책', N'서적', 15, 2);
INSERT INTO buyTbl VALUES(NULL, 'EJW', N'청바지', N'의류', 50, 1);
INSERT INTO buyTbl VALUES(NULL, 'BBK', N'운동화', NULL , 30, 2);
INSERT INTO buyTbl VALUES(NULL, 'EJW', N'책', N'서적', 15, 1);
INSERT INTO buyTbl VALUES(NULL, 'BBK', N'운동화', NULL, 30, 2);

-- SELECT : 데이터 조회
select * from userTbl;
select * from buyTbl;

-- WHERE : 조건으로 조회
SELECT userid, name
    from usertbl
    where height >= 180 and height <= 183;

-- BETWEEN ... AND
SELECT userid, name
    from usertbl
    where height between 180 and 183;

-- OR
select name, addr
    from usertbl
    where addr = '경남' or addr = '전남' or addr = '경북';

-- IN
SELECT Name, addr
    FROM userTbl
    WHERE addr in('경남', '전남', '경북');

-- LIKE
SELECT Name, height
    FROM userTbl
    WHERE name LIKE '김%';

SELECT Name, height
    FROM userTbl
    WHERE name LIKE '_종신';

-- 서브 쿼리가 1개의 행만 리턴하면 단일행 서브쿼리라고 한다.
SELECT Name, height
    FROM userTbl
    WHERE height > (
        SELECT height
        FROM userTbl
        WHERE Name = '김경호'
    );

-- 서브 쿼리가 여러 개의 행만 리턴하면 다중행 서브쿼리라고 한다.
SELECT Name, height FROM userTbl
    WHERE height >= ( -- 다중행 서브쿼리를 리턴하므로 에러 발생
        SELECT height
        FROM userTbl
        WHERE addr = '경남'
    );

-- ANY : 서브쿼리 중 한 가지만 만족해도 되는 상황 (합집합같은)
SELECT Name, height FROM userTbl
    WHERE height >= ANY (SELECT height FROM userTbl WHERE addr = '경남');

-- ALL : 서브쿼리를 모두 만족해야 하는 상황 (교집합같은)
SELECT Name, height FROM userTbl
    WHERE height >= ALL (SELECT height FROM userTbl WHERE addr = '경남');

-- IN : 서브쿼리에 속하는 경우
SELECT Name, height FROM userTbl
    WHERE height IN (SELECT height FROM userTbl WHERE addr = '경남');

-- 이건 왜 안되지
-- select * from (
--     select * from userTbl
-- );

-- ORDER BY : 정렬, ASC(오름차순)가 기본값
select name, mDate from usertbl order by mdate;
SELECT Name, height FROM userTbl ORDER BY height DESC, name ASC;
SELECT Name, height FROM userTbl ORDER BY height DESC, name;

-- DISTINCT : 중복 제거
SELECT addr FROM userTbl;
SELECT DISTINCT addr FROM userTbl;
SELECT DISTINCT addr FROM userTbl ORDER BY addr;

-- LIMIT : 출력 개수 제한
select name from userTbl LIMIT 5;
select name from userTbl LIMIT 5, 5; -- OFFSET

-- CREATE TABLE ... SELECT : 테이블 복사. 제약 조건은 복사 안됨
create table buyTbl2 (select * from buyTbl);
select * from buyTbl;
select * from buyTbl2;

create table buyTbl3 (select userID, prodName from buyTbl);
select * from buyTbl3;

-- GROUP BY : 그룹으로 묶는다.
SELECT userID, amount
    FROM buyTbl
    ORDER BY userID; -- 같은 userID도 행이 별도로 출력됨

-- SUM : 합
SELECT userID, SUM(amount)
    FROM buyTbl
    GROUP BY userID; -- userID를 기준으로 그룹화

-- alias 적용
SELECT userID '사용자 ID', SUM(amount) '구매 개수'
    FROM buyTbl
    GROUP BY userID;

-- 연산도 가능
SELECT userID '사용자 ID', SUM(price * amount) '총 구매액'
    FROM buyTbl
    GROUP BY userID;

SELECT SUM(amount) '총 구매 개수'
    FROM buyTbl;

-- AVG : 평균
SELECT AVG(amount) AS '평균 구매 개수'
    FROM buyTbl;

SELECT userID, AVG(amount) AS '평균 구매 개수'
    FROM buyTbl
    GROUP BY userID;

-- MAX : 최대, MIN : 최소
SELECT Name, height
    FROM userTbl
    WHERE height = (SELECT MAX(height) FROM userTbl)
        OR height = (SELECT MIN(height) FROM userTbl);

-- COUNT : 행의 개수
SELECT COUNT(*) FROM userTbl;
SELECT COUNT(*) 전체, COUNT(mobile1) AS '휴대폰이 있는 사용자'
    FROM userTbl;
SELECT COUNT(*) - COUNT(mobile1) 님폰없
    FROM userTbl;

SELECT userID AS '사용자', SUM(price*amount) AS '총구매액'
    FROM buyTbl
    GROUP BY userID;
-- 여기서 총구매액>1000 인 사람만 찾으려면,
SELECT userID AS '사용자', SUM(price*amount) AS '총구매액'
    FROM buyTbl
    WHERE SUM(price*amount) > 1000
    GROUP BY userID; -- 에러 : 집계 함수는 where 절에서 쓸 수 없음

-- HAVING : 집계 함수에 대해 조건을 제한함. 반드시 GROUP BY 다음에 나와야 함
SELECT userID AS '사용자', SUM(price*amount) AS '총구매액'
    FROM buyTbl
    GROUP BY userID
    HAVING SUM(price*amount) > 1000;
SELECT userID AS '사용자', SUM(price*amount) AS '총구매액'
    FROM buyTbl
    GROUP BY userID
    HAVING SUM(price*amount) > 1000
    ORDER BY SUM(price*amount);

-- ROLLUP : 소합계 및 총합을 같이 출력한다.
SELECT num, groupName, SUM(price * amount) AS '비용'
FROM buyTbl
GROUP BY groupName, num
WITH ROLLUP;
SELECT groupName, SUM(price * amount) AS '비용'
FROM buyTbl
GROUP BY groupName
WITH ROLLUP;
