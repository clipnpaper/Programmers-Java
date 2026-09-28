-- USED_GOODS_BOARD와 USED_GOODS_USER 테이블에서 완료된 중고 거래의 총금액이 70만 원 이상인 사람의 
-- 회원 ID, 닉네임, 총거래금액을 조회하는 SQL문을 작성해주세요. 결과는 총거래금액을 기준으로 오름차순 정렬해주세요.
SELECT A.USER_ID, A.NICKNAME, B.TOTAL_SALES
FROM USED_GOODS_USER AS A
inner join (select WRITER_ID, sum(PRICE) as TOTAL_SALES
from USED_GOODS_BOARD
where STATUS = 'DONE'
GROUP by 1
having TOTAL_SALES >= 700000) AS B
on A.USER_ID = B.WRITER_ID
order by 3;