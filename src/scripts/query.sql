SELECT * from webhooklog;

UPDATE webhooklog set status=null;

SELECT distinct(caseId),min(created_at) as created_at,
	FROM webhooklog
	AND (julianday('now') - created_at) >90000
	GROUP BY caseId
	ORDER BY created_at;
			
SELECT julianday('now') - created_at from webhooklog;


SELECT distinct(caseId),min(created_at) as created_at, 
	(julianday('now') - created_at) as time_diff
	FROM webhooklog
	AND (julianday('now') - created_at) >= 9000
	GROUP BY caseId
	ORDER BY created_at;