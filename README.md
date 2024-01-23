# Beauty city

This is a website of the beauty shops chain "City of Beauty", consisting of several salons. Each of them provides their own services and masters.

You can sign up for a service by selecting master, suitable shop, as well as date and time. The service can be paid for immediately on the site or, after its fulfillment, directly in the shop.

## How to install

Clone the project repository:
```bash
git clone https://github.com/michaelmatasyants/beauty_city.git
```

Rename `.env.example` to `.env` and add all the environment variables described in the file.

Run:<br>
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
