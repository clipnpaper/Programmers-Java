-- 코드를 입력하세요
SELECT MCDP_CD as '진료과코드', COUNT(*) AS '5월예약건수' from APPOINTMENT 
where APNT_YMD BETWEEN '2022-05-01' AND '2022-05-31'
group by 1
order by 2, 1;