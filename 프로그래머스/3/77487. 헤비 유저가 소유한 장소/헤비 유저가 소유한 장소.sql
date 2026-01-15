SELECT  *
  FROM  PLACES AS P1
 WHERE  EXISTS (
        SELECT  1
          FROM  PLACES AS P2
         WHERE  P1.HOST_ID = P2.HOST_ID
         GROUP
            BY  HOST_ID
        HAVING  COUNT(*) >= 2
        )
;