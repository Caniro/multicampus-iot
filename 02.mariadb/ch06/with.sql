-- WITH : CTE를 표현한다. SQL문을 좀 더 간결하게 표현할 수 있다.
with abc(userID, total)
as
(select userID as '사용자', SUM(price*amount) as '총구매액'
    from buyTbl group by userID)
select * from abc order by total desc;

-- userTbl에서 각 지역별로 키가 가장 큰 사람들을 뽑아서 평균을 내는 쿼리
with cte_userTbl(addr, maxHeight)
as
    (select addr, MAX(height) from userTbl group by addr)
select AVG(maxHeight*1.0) as '각 지역별 최고 키의 평균'from cte_userTbl;
