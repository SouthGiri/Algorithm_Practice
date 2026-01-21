WITH expensive as (
    SELECT  product_name
            , category
            , price as MAX_PRICE
            , RANK() OVER (PARTITION BY category ORDER BY price DESC) AS 'rank'
      FROM  food_product
     WHERE  category in ('과자', '국', '김치', '식용유')
)

SELECT  category
        , MAX_PRICE
        , product_name
  FROM  expensive as e
 WHERE  e.rank = 1
 ORDER
    BY  max_price DESC
;