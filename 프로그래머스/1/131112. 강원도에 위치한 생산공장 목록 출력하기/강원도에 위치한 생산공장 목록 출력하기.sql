-- 코드를 입력하세요
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM food_factory
WHERE LEFT(address, 3) = '강원도'
order by factory_id