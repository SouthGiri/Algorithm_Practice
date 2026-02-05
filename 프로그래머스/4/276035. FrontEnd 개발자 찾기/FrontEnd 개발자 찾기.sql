WITH front AS (
    SELECT  *
      FROM  skillcodes
     WHERE  LEFT(category, 5) = 'Front'
)
SELECT  DISTINCT id,
        email,
        first_name,
        last_name
  FROM  developers d JOIN
        front f ON
        (d.skill_code & f.code) > 0
 ORDER
    BY  id
;