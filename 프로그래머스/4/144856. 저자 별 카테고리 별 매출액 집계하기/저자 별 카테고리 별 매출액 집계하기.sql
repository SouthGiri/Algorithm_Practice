SELECT  a.author_id,
        a.author_name,
        category,
        SUM(_sum * price)
  FROM  (SELECT book_id, SUM(sales) AS '_sum'
         FROM book_sales
         WHERE LEFT(sales_date, 7) = '2022-01'
         GROUP BY book_id) AS s JOIN
         book AS b ON
         s.book_id = b.book_id JOIN
         author as a ON
         b.author_id = a.author_id
 GROUP
    BY  author_id,
        category
 ORDER
    BY  author_id,
        category DESC
;