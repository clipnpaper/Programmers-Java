-- 코드를 입력하세요
WITH RECURSIVE A AS 
(SELECT 0 AS hour UNION ALL SELECT hour + 1 FROM A WHERE hour < 23) 
SELECT 
A.hour as HOUR, ifnull(count(ANIMAL_ID),0) as COUNT
FROM A
    left join ANIMAL_OUTS as B
    ON A.hour = HOUR(B.DATETIME)
group by 1
order by 1;