-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN, 'N') as FREEZER_YN
FROM food_warehouse
WHERE LEFT(address, 3) = '경기도'
ORDER BY warehouse_id