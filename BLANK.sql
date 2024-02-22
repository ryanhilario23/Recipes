-- CREATE SCHEMA recipes_schema

-- CREATE TABLE recipes
-- (
--   recipe_id    INT          NOT NULL AUTO_INCREMENT,
--   name         VARCHAR(500) NULL    ,
--   description  VARCHAR(500) NULL    ,
--   instructions VARCHAR(500) NULL    ,
--   date         DATE         NULL    ,
--   cook_time    VARCHAR(25)      NULL    ,
--   PRIMARY KEY (recipe_id)
-- );

-- CREATE TABLE users
-- (
--   user_id    INT          NOT NULL AUTO_INCREMENT,
--   first_name VARCHAR(255) NULL    ,
--   last_name  VARCHAR(255) NULL    ,
--   email      VARCHAR(255) NULL    ,
--   password   VARCHAR(255) NULL    ,
--   PRIMARY KEY (user_id)
-- );

-- CREATE TABLE users_to_recipes
-- (
--   user_id   INT NOT NULL,
--   recipe_id INT NOT NULL
-- );

-- ALTER TABLE users_to_recipes
--   ADD CONSTRAINT FK_users_TO_users_to_recipes
--     FOREIGN KEY (user_id)
--     REFERENCES users (user_id);

-- ALTER TABLE users_to_recipes
--   ADD CONSTRAINT FK_recipes_TO_users_to_recipes
--     FOREIGN KEY (recipe_id)
--     REFERENCES recipes (recipe_id);

SELECT *
FROM recipes;

-- To save
-- """
-- INSERT INTO users ()
-- VALUES (%()s)
-- """

-- To update
-- """ 
-- UPDATE users
-- SET first_name = %(first_name)s,last_name = %(last_name)s, email= %(email)s
-- WHERE id = %(id)s;
-- """

-- To delete
-- """
-- DELETE FROM users
-- WHERE id = %(id)s;
-- """

-- to run a check
-- """
-- SELECT *
-- FROM users
-- WHERE user_id = %(user_id)s
-- """
-- """
-- SELECT *
-- FROM users
-- WHERE email = %(email)s
-- """
-- """
-- SELECT *
-- FROM users
-- WHERE user_id = %(user_id)s
-- """


