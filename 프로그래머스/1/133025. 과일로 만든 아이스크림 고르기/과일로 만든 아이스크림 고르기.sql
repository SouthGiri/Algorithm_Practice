-- 코드를 입력하세요
SELECT fh.FLAVOR
FROM first_half as fh, icecream_info as ii
WHERE fh.flavor = ii.flavor
    and total_order > 3000 
    and ingredient_type = 'fruit_based'
ORDER BY total_order DESC