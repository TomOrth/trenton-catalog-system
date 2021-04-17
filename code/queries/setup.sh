# Sets up the database
sudo -u postgres psql -c "ALTER ROLE matthewvansoelen SUPERUSER;"
psql lion -f setup.sql
sudo -u postgres psql -c "ALTER ROLE matthewvansoelen nosuperuser;"