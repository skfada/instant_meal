-- this schema will create the database if it does not exist
CREATE DATABASE IF NOT EXISTS instant_meal;
USE instant_meal;
-- creating the user and the password
CREATE USER IF NOT EXISTS 'instant_meal'@'localhost';
SET PASSWORD FOR 'instant_meal'@'localhost' = 'instantmeal@2024';
-- granting privilleges to the user on the database
GRANT ALL PRIVILEGES ON instant_meal.* TO 'instant_meal'@'localhost';
GRANT SELECT ON performance_schema.* TO 'instant_meal'@'localhost';
