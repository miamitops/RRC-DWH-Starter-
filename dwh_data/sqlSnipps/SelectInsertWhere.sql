/****** Script for SelectTopNRows command from SSMS  ******/
INSERT INTO [dbo].[base_data_ssd_pop] SELECT * FROM [dbo].[base_data_uga]
WHERE [dbo].[base_data_uga].CountryOfOrigin = 'SSD'
