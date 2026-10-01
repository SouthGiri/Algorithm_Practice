SELECT  ID,
        FISH_NAME,
        LENGTH
  FROM  (
        SELECT  ID,
                FISH_TYPE,
                LENGTH,
                MAX(LENGTH) OVER (PARTITION BY FISH_TYPE) AS MAX_LEN
          FROM  FISH_INFO
        ) FI 
        JOIN FISH_NAME_INFO FNI
        ON FI.FISH_TYPE = FNI.FISH_TYPE
 WHERE  FI.LENGTH = FI.MAX_LEN
 ORDER
    BY  ID
;