-- 코드를 입력하세요
select CATEGORY, max(PRICE) AS MAX_PRICE, PRODUCT_NAME from FOOD_PRODUCT as a
where CATEGORY IN ('과자', '국','김치','식용유')
AND PRICE = (select max(price) from FOOD_PRODUCT as b where a.CATEGORY = b.CATEGORY group by CATEGORY)
group by CATEGORY
ORDER BY 2 DESC;