-- 코드를 입력하세요
SELECT 
a.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY, ifnull(sum(b.PRICE * s.SALES), 0) as TOTAL_SALES
from BOOK as b
    inner join AUTHOR as a
    on b.AUTHOR_ID = a.AUTHOR_ID
    left join BOOK_SALES as s
    on b.BOOK_ID = s.BOOK_ID
where s.SALES_DATE between '2022-01-01' and '2022-01-31'
group by 1, 3
order by 1, 3 desc;
    