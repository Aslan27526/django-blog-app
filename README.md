

Clone This Project (Make Sure You Have Git Installed)
```
https://github.com/mustafamuratcoskun/DjangoBlogApp.git
```
Install Dependencies 

```
pip install -r requirements.txt
```
Note: Django  has a rendering issues after 2.0.8. If you encounter with this problem, go to the file which has the problem (it will be shown in error page) and delete "renderer=self.forms.renderer". Or just change Django version to 2.0 (Django==2.0) in requirements.py


Set Database (Make Sure you are in directory same as manage.py)
```
python manage.py makemigrations
python manage.py migrate
```
Create SuperUser 
```
python manage.py createsuperuser
```

After all these steps , you can start testing and developing this project. 

http://aslantinomia.pythonanywhere.com/.
