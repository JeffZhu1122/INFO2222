CREATE TABLE IF NOT EXISTS `app_user`(
   `user_id` INT(10),
   `user_name` VARCHAR(400),
   `user_passwd` VARCHAR(400),
   `user_email` VARCHAR(400),
   `user_phone` VARCHAR(400),
   `submission_date` DATE,
   PRIMARY KEY ( `user_id` )
);

alter table app_user modify user_id integer auto_increment ;  
