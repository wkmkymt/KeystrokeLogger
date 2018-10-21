heroku pg:psql -c "\copy (SELECT * FROM keystroke) TO dbs/dump.csv WITH CSV HEADER"
