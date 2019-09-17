BEGIN;
CREATE TABLE `t_dwh_import_files` (`i_file_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `s_progress_instance` varchar(254) NOT NULL, `d_generated` datetime(6) NOT NULL, `d_imported` datetime(6) NOT NULL, `importstatus` varchar(5) NOT NULL, `fk_country_id` varchar(4) NOT NULL);
CREATE TABLE `t_dwh_import_logs` (`report_ptr_id` integer NOT NULL UNIQUE, `log_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `log_level` varchar(5) NOT NULL, `log_message` varchar(1200) NOT NULL, `file_id` integer NOT NULL);
CREATE TABLE `t_dwh_import_types` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `s_name` varchar(254) NOT NULL, `s_desc` varchar(254) NOT NULL);
ALTER TABLE `t_dwh_import_files` ADD CONSTRAINT `t_dwh_import__fk_country_id_18a5b074_fk_conf_countries_countryID` FOREIGN KEY (`fk_country_id`) REFERENCES `conf_countries` (`countryID`);
ALTER TABLE `t_dwh_import_logs` ADD CONSTRAINT `t_dwh_import__report_ptr_id_61fbac9e_fk_report_builder_report_id` FOREIGN KEY (`report_ptr_id`) REFERENCES `report_builder_report` (`id`);
ALTER TABLE `t_dwh_import_logs` ADD CONSTRAINT `t_dwh_import_lo_file_id_6f4c411b_fk_t_dwh_import_files_i_file_id` FOREIGN KEY (`file_id`) REFERENCES `t_dwh_import_files` (`i_file_id`);

COMMIT;
