-- Shows higher temperatures that a state has had
-- Shows higher temperatures that a state has had
SELECT state, MAX(value) as max_temp from temperatures 
    ORDER BY state;
    GROUP BY state 
