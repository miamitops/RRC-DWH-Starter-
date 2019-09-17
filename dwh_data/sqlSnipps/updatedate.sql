UPDATE base_data_ssd_pop 
SET moddob = CONVERT(DATETIME, lTRIM(DateOfBirth))

SELECT LEFT(ARRIVALDATE,3) FROM base_data_ssd_pop
DELETE FROM [dbo].[base_data_uga]
WHERE FamilyName = 'FamilyName'