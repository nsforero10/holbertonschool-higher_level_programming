-- Counts the number of equals scores
-- Counts the number of equals scores
SELECT score, COUNT(score) as number FROM second_table
    GROUP BY score
    ORDER BY score DESC;