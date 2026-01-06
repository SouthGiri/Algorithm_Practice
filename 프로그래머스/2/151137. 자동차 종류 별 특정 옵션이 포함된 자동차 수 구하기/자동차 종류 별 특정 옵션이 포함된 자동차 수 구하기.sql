-- 코드를 입력하세요
SELECT car_type, count(car_id) as CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE options LIKE '%시트%'
GROUP BY car_type
ORDER BY car_type