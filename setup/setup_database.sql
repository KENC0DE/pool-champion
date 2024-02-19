-- Create production database
CREATE DATABASE IF NOT EXISTS pool_game_prod;

-- Create development database
CREATE DATABASE IF NOT EXISTS pool_game_dev;

-- Create a user and grant privileges for both databases
CREATE USER 'pooladmin'@'localhost' IDENTIFIED BY 'poolgame';
GRANT ALL PRIVILEGES ON your_database_name_prod.* TO 'pooladmin'@'localhost';
GRANT ALL PRIVILEGES ON your_database_name_dev.* TO 'pooladmin'@'localhost';
FLUSH PRIVILEGES;
