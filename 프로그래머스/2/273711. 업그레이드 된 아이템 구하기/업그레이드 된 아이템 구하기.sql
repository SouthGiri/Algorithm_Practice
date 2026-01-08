# 부모가 null 이 아니고, 부모의 id 로 가서 rarity 가 rare 인 경우
SELECT
        II.ITEM_ID
      , II.ITEM_NAME
      , II.RARITY
FROM
    ITEM_TREE AS IT
    JOIN ITEM_INFO AS II
    ON II.ITEM_ID = IT.ITEM_ID
    JOIN ITEM_INFO AS PI
    ON PI.ITEM_ID = IT.PARENT_ITEM_ID
WHERE
    PI.RARITY = 'RARE'
ORDER BY
    II.ITEM_ID DESC
;