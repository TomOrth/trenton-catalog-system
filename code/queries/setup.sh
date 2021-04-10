# Sets up the database
sudo -u postgres psql -c "ALTER ROLE lion SUPERUSER;"
psql lion -f setup.sql
sudo -u postgres psql -c "ALTER ROLE lion nosuperuser;"