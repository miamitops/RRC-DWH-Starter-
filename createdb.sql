BEGIN;
CREATE TABLE `t_dwh_report_format` (`i_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `s_name` varchar(254) NOT NULL, `s_desc` varchar(254) NOT NULL);
CREATE TABLE `t_dwh_reports` (`reportId_id` integer NOT NULL PRIMARY KEY, `raw_data` varchar(254) NULL);
CREATE TABLE `t_dwh_report_view` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY);
CREATE TABLE `t_report_types` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `s_name` varchar(254) NOT NULL, `s_desc` varchar(254) NOT NULL);
ALTER TABLE `t_dwh_reports` ADD CONSTRAINT `t_dwh_reports_reportId_id_3a08efaa_fk_report_builder_report_id` FOREIGN KEY (`reportId_id`) REFERENCES `report_builder_report` (`id`);

COMMIT;
