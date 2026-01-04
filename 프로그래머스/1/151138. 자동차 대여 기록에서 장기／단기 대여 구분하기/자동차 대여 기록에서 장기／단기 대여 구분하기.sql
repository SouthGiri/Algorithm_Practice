-- 코드를 입력하세요
SELECT HISTORY_ID, CAR_ID,
    LEFT(start_date, 10) as START_DATE,
    LEFT(end_date, 10) as END_DATE,
    IF(DATEDIFF(end_date, start_date)+1 >= 30, '장기 대여', '단기 대여') as RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE LEFT(start_date, 7) = '2022-09'
ORDER BY history_id DESC