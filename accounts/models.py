from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile


class Organizations(models.Model):
    id = models.AutoField(db_column='i_id', primary_key=True, blank=False, null=False)
    orgName = models.CharField(db_column='name', unique=True, max_length=255)
    def __unicode__(self):
        return unicode(self.orgName)
   
class Profile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True, verbose_name=_('user'), related_name='my_profile')
    organization = models.ForeignKey(Organizations, db_column='fk_org', verbose_name='Organization')
    country = models.CharField(db_column='country', verbose_name='Country',  max_length=255, null=True, blank=False)
    city = models.CharField(db_column='city', verbose_name='City', max_length=255, null=True, blank=False)
    dutyStation = models.CharField(db_column='duty_station', verbose_name='Duty Station', max_length=255)
    department = models.CharField(db_column='department', verbose_name='Department or Unit', max_length=255)
    '''expiry = models.DateTimeField(db_column='contract_expiry', verbose_name='Contract Expiry Date')'''
    
    class Meta:
        db_table = u'accounts_profile2'
        managed = True