SELECT
    ii.item_id,
    item_name
FROM
    item_info as ii JOIN
    item_tree as it ON
    ii.item_id = it.item_id
WHERE
    parent_item_id IS NULL
ORDER BY
    item_id