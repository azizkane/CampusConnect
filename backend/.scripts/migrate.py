import os
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()

def run_migrations():
    # Core apps on PostgreSQL
    core_apps = {
        'accounts': {
            'db': 'accounts',
            'app': 'core.accounts'
        },
        'schools': {
            'db': 'schools',
            'app': 'core.schools'
        },
        'students': {
            'db': 'students',
            'app': 'core.students'
        }
    }

    # Service apps on PostgreSQL
    service_apps = {
        'billing': {
            'db': 'billing',
            'app': 'service.billing'
        },
        'mailjet': {
            'db': 'default',
            'app': 'service.mailjet'
        }
    }

    # Feature apps on MongoDB
    feature_apps = [
        'feature.libraries',
        'feature.forums',
        'feature.calendar.events',
        'feature.calendar.projects',
        'feature.calendar.calendar'
    ]

    print("\n=== Starting Core Apps Migrations (PostgreSQL) ===")
    for name, config in core_apps.items():
        print(f"\nMigrating {config['app']} on {config['db']} database")
        call_command('migrate', config['app'], database=config['db'])

    print("\n=== Starting Service Apps Migrations (PostgreSQL) ===")
    for name, config in service_apps.items():
        print(f"\nMigrating {config['app']} on {config['db']} database")
        call_command('migrate', config['app'], database=config['db'])

    print("\n=== Starting Feature Apps Migrations (MongoDB) ===")
    for app in feature_apps:
        print(f"\nMigrating {app} on mongodb database")
        call_command('migrate', app, database='mongodb')

if __name__ == '__main__':
    run_migrations()
