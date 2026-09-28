-- 코드를 입력하세요
select
b.INGREDIENT_TYPE, sum(a.TOTAL_ORDER) as TOTAL_ORDER
from FIRST_HALF as a
    inner join ICECREAM_INFO as b
    on a.FLAVOR = b.FLAVOR
group by 1
order by 2;
