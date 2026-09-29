-- 코드를 작성해주세요

select sum(score) as SCORE, e.EMP_NO, 
EMP_NAME, POSITION, EMAIL from HR_GRADE as g
inner join HR_EMPLOYEES as e
on g.EMP_NO = e.EMP_NO
group by 2, 3, 4, 5
order by 1 desc
limit 1;

