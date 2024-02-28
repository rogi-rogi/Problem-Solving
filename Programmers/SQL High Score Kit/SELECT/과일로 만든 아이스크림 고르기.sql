-- 05(과일로 만든 아이스크림 고르기).sql
-- https://school.programmers.co.kr/learn/courses/30/lessons/133025

SELECT F.FLAVOR
FROM FIRST_HALF AS F, ICECREAM_INFO AS I
WHERE F.FLAVOR = I.FLAVOR AND F.TOTAL_ORDER > 3000 AND I.INGREDIENT_TYPE = 'fruit_based'
ORDER BY F.TOTAL_ORDER DESC
