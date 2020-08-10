-- creates data base and its data talbe filled
-- creates data base and its data talbe filled
SELECT id,
    name
FROM cities
WHERE state_id = (
        SELECT id
        FROM states
        WHERE name = "California"
    );
