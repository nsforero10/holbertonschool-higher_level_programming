-- Shows higher temperatures that a state has had
-- Shows higher temperatures that a state has had
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state;
