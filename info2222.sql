CREATE TABLE IF NOT EXISTS `app_user`(
   `user_id` INT(10),
   `user_name` VARCHAR(400),
   `user_passwd` VARCHAR(400),
   `salt` VARCHAR(100),
   `user_email` VARCHAR(400),
   `is_super` INT DEFAULT 0,
   `uploaded` INT DEFAULT 0,
   `submission_date` DATE,
   PRIMARY KEY ( `user_id` )
);

alter table app_user modify user_id integer auto_increment ;
