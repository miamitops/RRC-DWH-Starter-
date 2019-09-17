BEGIN;
CREATE TABLE `accounts_organizations` (`i_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(255) NOT NULL UNIQUE);
CREATE TABLE `accounts_profile2` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `mugshot` varchar(100) NOT NULL, `privacy` varchar(15) NOT NULL, `country` varchar(255) NULL, `city` varchar(255) NULL, `duty_station` varchar(255) NOT NULL, `department` varchar(255) NOT NULL, `fk_org` integer NOT NULL, `user_id` integer NOT NULL UNIQUE);
ALTER TABLE `accounts_profile2` ADD CONSTRAINT `accounts_profile2_fk_org_3be15d2a_fk_accounts_organizations_i_id` FOREIGN KEY (`fk_org`) REFERENCES `accounts_organizations` (`i_id`);
ALTER TABLE `accounts_profile2` ADD CONSTRAINT `accounts_profile2_user_id_2d07d642_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

COMMIT;
