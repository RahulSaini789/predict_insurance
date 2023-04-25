echo " BUILD START"
Python 3.11.3 -m pip install -r requirements.txt
Python 3.11.3 manage.py collectstatic --noinput --clear
echo " BUILD END" 
