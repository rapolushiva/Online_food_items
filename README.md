# Online_food_items
Online food items project is used to buy or sell food items in online. Insert the food items data into mysql database.then search item name in the searchbar  it will  navigate to desire food item url it will appear.


Main changes in the above Food_Items_DB  are:
1)Mysql Port number 3307 to 3306  in settings.py
2)In your local host create Database name as food_item_db 
3)The below commands are run in your terminal or commandprompt after download this Food_Items_DB
      -->cd Food_Items_DB (change the directory main project and makemigration command as follows) 
      -->python manage.py makemigrations(Afther the makemigrations migrate using next command) 
      -->python manage.py migrate (After migrate different tables are created in the Database) 
      -->python manage.py createsuperuser (it is used log into admin page) 
      -->Python manage.py runserver (after login data enter into two diffeterent tables are one is category table and another             one is Products table)
4)Enter the required urls show the web pages based on entered urls
