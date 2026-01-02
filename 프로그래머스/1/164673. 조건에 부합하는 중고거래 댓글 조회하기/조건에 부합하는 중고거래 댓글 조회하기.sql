-- 코드를 입력하세요
SELECT TITLE, b.BOARD_ID, r.REPLY_ID, 
    r.WRITER_ID, r.CONTENTS, DATE_FORMAT(r.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
FROM USED_GOODS_BOARD as b, USED_GOODS_REPLY as r
WHERE DATE_FORMAT(b.CREATED_DATE, '%Y%m') = '202210'
    and b.board_id = r.board_id
ORDER BY r.created_date, title