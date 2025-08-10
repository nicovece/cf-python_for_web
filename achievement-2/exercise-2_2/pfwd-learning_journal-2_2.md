# Python for Web Developers Learning Journal

## Exercise 2.2: Django Project Set Up

### Reflection Questions

---

**Suppose you’re in an interview. The interviewer gives you their company’s website as an example, asking you to convert the website and its different parts into Django terms. How would you proceed? For this question, you can think about your dream company and look at their website for reference.**

For a newspaper-style website in Django, I would break the site into separate apps based on functionality:

- **accounts** – Handles user registration, login/logout, profiles, and permissions (e.g., readers vs. editors).
- **articles** – Manages article creation, editing, publishing, categories, and tags.
- **comments** – Allows users to comment on articles, with moderation tools.
- **subscriptions** – Handles paid plans, free trials, and subscriber content access.
- **homepage** – Displays featured news, trending articles, and search functionality.

This way, each app focuses on one responsibility, making the project easier to maintain and scale.

---

**In your own words, describe the steps you would take to deploy a basic Django application locally on your system.**

First, I create a virtual environment and activate it, so dependencies stay isolated. Then I install Django and start a new project with django-admin startproject. Inside the project, I create my first app and add it to INSTALLED_APPS. After that, I run migrations to set up the database, create a superuser for the admin panel, and finally start the development server with runserver. At that point, the site is live locally at 127.0.0.1:8000.

**Steps to deploy a basic Django application locally:**

1. **Create a virtual environment** to isolate project dependencies:
   `python3 -m venv env`
   `source env/bin/activate`

2. **Install Django** in the virtual environment:
   `pip3 install django`

3. **Create a new Django project**:
   `django-admin startproject project_name`
   `cd project_name`

4. **Create your first app** (e.g., `news`, `blog`, `accounts`):
   `python3 manage.py startapp app_name`

   Then add the app to the `INSTALLED_APPS` list in `settings.py`.

5. **Apply initial database migrations** to set up default tables:
   `python3 manage.py migrate`

6. **Create a superuser** to access the Django admin interface:
   `python3 manage.py createsuperuser`

7. **Start the development server** to run the project locally:
   `python3 manage.py runserver`

At this point, the Django project is running locally and can be accessed in the browser at `http://127.0.0.1:8000/` and `http://127.0.0.1:8000/admin`.

---

**Do some research about the Django admin site and write down how you’d use it during your web application development.**

The Django admin site is like a built-in control panel for my app’s data. I use it to quickly add, edit, and delete records, test my models, assign user roles, and fill in test data — all without coding a separate front end. It’s great for checking that the backend works before building the actual UI.

Key ways I can use it:

- View, add, edit, and delete records in the database without writing SQL queries.
- Test and manage models I create, making sure relationships and fields work correctly.
- Assign permissions and roles to users (e.g., editors, moderators, admins).
- Quickly populate test data for development.
- Monitor changes in content and check that CRUD operations work as expected.
