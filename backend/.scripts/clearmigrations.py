import os

def clean_migrations():
    # List of apps to clean migrations
    apps = ['core', 'features', 'system']
    
    # Root directory where the apps are located
    root_dir = '.'
    
    for app in apps:
        migrations_path = os.path.join(root_dir, app, 'migrations')
        if os.path.exists(migrations_path):
            for filename in os.listdir(migrations_path):
                # Keep __init__.py, remove all other Python files
                if filename.endswith('.py') and filename != '__init__.py':
                    file_path = os.path.join(migrations_path, filename)
                    os.remove(file_path)
                    print(f'Deleted: {file_path}')

if __name__ == '__main__':
    clean_migrations()
