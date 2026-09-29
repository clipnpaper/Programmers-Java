-- 코드를 작성해주세요
select 
count(*) as fish_count, max(ifnull(length,10)) as max_length, fish_type
from fish_info group by 3 having avg(ifnull(length,10)) >= 33
order by 3;