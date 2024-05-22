# Remove migration files
Get-ChildItem -Recurse -Filter *.py -Include migrations | Where-Object { $_.Name -ne "__init__.py" } | Remove-Item -Force
Get-ChildItem -Recurse -Filter *.pyc -Include migrations | Remove-Item -Force

# Recreate initial migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser