# Sets up the database
sudo -i -u postgres psql -c "ALTER ROLE lion SUPERUSER;"
psql lion -U lion -f setup.sql
sudo -i -u postgres psql -c "ALTER ROLE lion nosuperuser;"
