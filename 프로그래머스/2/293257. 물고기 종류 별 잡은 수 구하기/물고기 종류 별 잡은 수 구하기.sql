-- 코드를 작성해주세요
select 
count(*) as fish_count, fish_name
from fish_info as a
    inner join fish_name_info as b
    on a.fish_type = b.fish_type
group by 2
order by 1 desc;

