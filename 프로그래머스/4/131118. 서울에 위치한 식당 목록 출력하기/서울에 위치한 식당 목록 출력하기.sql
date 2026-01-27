SELECT  i.rest_id,
        rest_name,
        food_type,
        favorites,
        address,
        ROUND(AVG(review_score), 2) AS SCORE
  FROM  (
        SELECT  *
          FROM  rest_info
         WHERE  address LIKE '서울%'
        ) AS i JOIN
        rest_review AS r ON
        i.rest_id = r.rest_id
 GROUP
    BY  rest_id
 ORDER
    BY  score DESC,
        favorites DESC
;