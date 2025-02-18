class DatabaseRouter:
    mongodb_apps = ['features']
    postgres_apps = ['admin', 'auth', 'authtoken', 'contenttypes', 'core', 'sessions', 'system', 'token_blacklist']

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.mongodb_apps:
            return 'mongodb'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.mongodb_apps:
            return 'mongodb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in self.mongodb_apps or obj2._meta.app_label in self.mongodb_apps:
            return True
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.mongodb_apps:
            return db == 'mongodb'
        return db == 'default'
