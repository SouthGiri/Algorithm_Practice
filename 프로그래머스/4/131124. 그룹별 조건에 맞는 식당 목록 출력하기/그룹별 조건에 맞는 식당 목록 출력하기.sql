WITH review AS (
    SELECT  rv.member_id,
            member_name,
            COUNT(*) 'cnt'
      FROM  rest_review rv JOIN
            member_profile mp ON
            rv.member_id = mp.member_id
     GROUP
        BY  member_id
)
SELECT  member_name,
        review_text,
        LEFT(review_date, 10) 'REVIEW_DATE'
  FROM  review r JOIN
        rest_review rr ON
        r.member_id = rr.member_id
 WHERE  cnt = (SELECT MAX(cnt)
               FROM review)
 ORDER
    BY  review_date,
        review_text
;