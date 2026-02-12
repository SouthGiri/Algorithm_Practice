WITH sedan_suv AS (
    SELECT  c.car_id,
            c.daily_fee,
            c.car_type
      FROM  CAR_RENTAL_COMPANY_CAR c
     WHERE  1=1
            AND c.car_type IN ('세단', 'SUV')
            AND NOT EXISTS (
                SELECT 1
                FROM   CAR_RENTAL_COMPANY_RENTAL_HISTORY h
                WHERE  h.car_id = c.car_id
                  AND  h.start_date <= '2022-11-30'
                  AND  h.end_date   >= '2022-11-01'
            )
)
SELECT  car_id,
        ss.car_type,
        FLOOR(daily_fee * weight * 30) FEE
  FROM  sedan_suv ss JOIN
        (SELECT car_type, ((100 - discount_rate) / 100) AS weight
         FROM   CAR_RENTAL_COMPANY_DISCOUNT_PLAN
         WHERE  LEFT(duration_type, 2) = '30') dp ON
        ss.car_type = dp.car_type
 WHERE  FLOOR(daily_fee * weight) * 30 BETWEEN 500000 AND 1999999
 ORDER
    BY  FEE DESC,
        car_type,
        car_id DESC
;