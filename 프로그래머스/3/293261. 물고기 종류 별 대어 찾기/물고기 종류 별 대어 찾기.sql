
# SELECT  id, length, fish_type, MAX(length) OVER (PARTITION BY fish_type)
#   FROM  fish_info as fi

WITH R AS (
SELECT  id,
        FI.fish_type,
        N.fish_name,
        MAX(length) OVER (PARTITION BY fish_type) AS LENGTH
  FROM  fish_info AS FI JOIN
        fish_name_info AS N ON
        FI.fish_type = N.fish_type
)

SELECT  I.ID,
        FISH_NAME,
        R.LENGTH
  FROM  fish_info as I JOIN
        R ON
        I.id = R.id
        AND I.length = R.length
 ORDER
    BY  id