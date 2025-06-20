
-- Segmentación de leads con score alto
SELECT * FROM leads
WHERE score >= 70
ORDER BY score DESC;
