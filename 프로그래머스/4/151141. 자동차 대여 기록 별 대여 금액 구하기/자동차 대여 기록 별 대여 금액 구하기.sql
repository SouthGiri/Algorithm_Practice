WITH truck_table AS (
    SELECT  car_id,
            daily_fee
      FROM  car_rental_company_car
     WHERE  car_type = '트럭'
), discount_plan AS (
    SELECT  LEFT(duration_type, INSTR(duration_type, '일') - 1) AS 'day',
            100 - discount_rate AS 'weight'
      FROM  CAR_RENTAL_COMPANY_DISCOUNT_PLAN
     WHERE  car_type = '트럭'
)
SELECT  history_id,
        CAST(
            CASE 
                WHEN DATEDIFF(end_date, start_date)+1 >= 90
                    THEN daily_fee * (SELECT weight FROM discount_plan WHERE day = 90) / 100
                WHEN DATEDIFF(end_date, start_date)+1 >= 30
                    THEN daily_fee * (SELECT weight FROM discount_plan WHERE day = 30) / 100
                WHEN DATEDIFF(end_date, start_date)+1 >= 7
                    THEN daily_fee * (SELECT weight FROM discount_plan WHERE day = 7) / 100
                ELSE daily_fee
            END AS UNSIGNED
        ) * (DATEDIFF(end_date, start_date)+1) AS FEE
  FROM  truck_table t JOIN
        CAR_RENTAL_COMPANY_RENTAL_HISTORY r ON
        t.car_id = r.car_id
 ORDER
    BY  FEE DESC,
        history_id DESC
;