source ../../.finishmyprojects/bin/activate

rm ../sql_app.db

touch ../sql_app.db

rm ../alembic/migrations/versions/*

alembic revision --autogenerate -m "regenerate tables"

# SELECT 'INSERT INTO ' || name || ' SELECT * FROM ' || name || ';'
# FROM sqlite_master
# WHERE type = 'table';
