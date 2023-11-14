-- write a script that creates a table called first table in the current database
-- add <id> and <name> columns to the table
-- if the table first_table already exists, you script should not fail
CREATE TABLE IF NOT EXISTS first_table(id INT, name VARCHAR(256));
