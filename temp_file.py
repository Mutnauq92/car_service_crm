"""
import zoneinfo

def create_continent_city_dict():
    # Initialize the dictionary
    continent_dict = {}

    # Get the set of available timezones
    timezones = zoneinfo.available_timezones()

    for tz in timezones:
        # Split the timezone into continent and city
        parts = tz.split('/')
        if len(parts) == 2:
            continent, city = parts
            
            # If the continent is not already a key in the dictionary, add it
            if continent not in continent_dict:
                continent_dict[continent] = []
            
            # Add the city to the list of cities for the given continent
            continent_dict[continent].append(city)
    
    return continent_dict

# Example usage
continent_dict = create_continent_city_dict()

def choose_continent(continent):
    return continent_dict[continent]
    

cont = "africa".capitalize()
print(choose_continent(cont))
"""

rm -f db.sqlite3  # Deletes the SQLite database file
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete  # Deletes all migration files except __init__.py
find . -path "*/migrations/*.pyc"  -delete  # Deletes all compiled Python files for migrations

python manage.py makemigrations crm
python manage.py migrate
    
    