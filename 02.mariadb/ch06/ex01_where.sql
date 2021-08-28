SELECT userid, name
from usertbl
where height between 180 and 183;

select name, addr
from usertbl
where addr = '경남' or addr = '전남' or addr = '경북';

SELECT Name, addr
FROM userTbl
WHERE addr in('경남', '전남', '경북');

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
WHERE height >= (
    SELECT height
    FROM userTbl
    WHERE addr = '경남'
);

SELECT Name, height FROM userTbl
WHERE height >= ANY (SELECT height FROM userTbl WHERE addr = '경남');

SELECT Name, height FROM userTbl
WHERE height >= ALL (SELECT height FROM userTbl WHERE addr = '경남');


SELECT Name, height FROM userTbl
WHERE height IN (SELECT height FROM userTbl WHERE addr = '경남');
