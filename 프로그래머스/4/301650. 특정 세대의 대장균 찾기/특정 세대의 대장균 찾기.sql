WITH fir_gen AS (
    SELECT  id
      FROM  ecoli_data
     WHERE  parent_id IS NULL
), sec_gen AS (
    SELECT  e.id
      FROM  fir_gen f JOIN
            ecoli_data e ON
            f.id = e.parent_id
)
SELECT  e.id
  FROM  sec_gen s JOIN
        ecoli_data e ON
        s.id = e.parent_id
 ORDER
    BY  id
;