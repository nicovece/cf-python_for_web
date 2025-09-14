# Python for Web Developers Learning Journal

## Exercise 2.6: User Authentication in Django

### Reflection Questions

---

**In your own words, write down the importance of incorporating authentication into an application. You can take an example application to explain your answer.**

Authentication is important because it makes sure that only the right people can access certain parts of an application. For example, in a banking app, you don’t want just anyone to see or move your money. By requiring a username and password (or other login methods), the app confirms your identity and protects your personal information. Without authentication, anyone could access private data or perform actions they shouldn’t, which would make the app unsafe.

---

**In your own words, explain the steps you should take to create a login for your Django web application.**

Steps to create a login in Django:

1. Set up templates – Tell Django where to look for your login template.
2. Create the view – Add a function or class that checks the user’s username and password.
3. Make the template – Build an HTML page with a form for the user to log in.
4. Register the URL – Connect the login view to a URL (like /login/) in your project’s URL settings.
5. Protect pages – Mark certain pages so that only logged-in users can access them.

---

**Look up the following three Django functions on Django’s official documentation and/or other trusted sources and write a brief description of each.**

`authenticate()`

- Purpose: To check whether given credentials (like a username & password) correspond to a real user in your Django application.
- What it returns: If credentials are valid, it returns a User object; otherwise, it returns None.
- How it works: Django goes through its configured “authentication backends” until one backend accepts the credentials. If none do, authentication fails.

`redirect()`

- Purpose: To send the user’s browser to a different URL instead of returning a normal page.
- What it does: It makes Django return a special HTTP response that tells the browser “go here instead.” This is useful after forms, login, logout, or whenever you want to change what page the user sees next.

  Details:

  - You can give it a URL string (absolute or relative), or a named view (so Django will look up the correct URL).
  - By default the redirect is temporary (HTTP status 302). You can make it permanent (status 301).

`include()`

- Purpose: To help organize URLs: it allows you to “pull in” another set of URL patterns from another module (often from an app) into your main URL configuration.
- How it works: Suppose you have a Django app with its own urls.py file; using include() in the project’s (or another app’s) urls.py lets you make URLs under a certain prefix route to those included patterns.
- Benefit: It keeps your URL setup cleaner and more modular (you don’t have all URL patterns in one file). Also useful for namespacing URL names so you don’t get name clashes.
