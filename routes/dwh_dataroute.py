class DWHRouter(object):
    '''
    A router for the dwh Data Model'''
    def db_for_read(self, model, **hints):
        '''read DWH data from the dwh_data database'''
        if model._meta.app_label == 'dwh_data':
            return 'dwh_data'
        return None
    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model._meta.app_label == 'dwh_data':
            return 'dwh_data'
        return None
    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the dwh_data app is involved.
        """
        if obj1._meta.app_label == 'dwh_data' or \
            obj2._meta.app_label == 'dwh_data':
            return True
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'dwh_data'
        database.
        """
        if app_label == 'dwh_data':
            return db == 'dwh_data'
        return None