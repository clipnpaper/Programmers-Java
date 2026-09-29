# -- 코드를 작성해주세요
# with ITEM_NEW as (
#     select o.ITEM_ID, e.PARENT_ITEM_ID , o.ITEM_NAME, o.RARITY, o.PRICE
#     from ITEM_INFO as o
#         inner join ITEM_TREE as e
#         on o.ITEM_INFO = e.ITEM_TREE
# )
# select 

# from ITEM_NEW as p
#     left join ITEM_NEW as c
#     on p.ITEM_ID = c.PARENT_ITEM_ID
select ITEM_ID, ITEM_NAME, RARITY from ITEM_INFO
where ITEM_ID not in (select distinct PARENT_ITEM_ID from ITEM_TREE where PARENT_ITEM_ID IS NOT NULL)
order by 1 desc;