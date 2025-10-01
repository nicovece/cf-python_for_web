# Python for Web Developers Learning Journal

## Exercise 2.8: Deploying a Django Application

### Reflection Questions

---

**Explain how you can use CSS and JavaScript in your Django web application.**

In a Django web application, CSS and JavaScript are handled as static files, just like images or fonts. Django provides a built-in system for managing these files, either at the project level (for shared styles and scripts across the whole site) or at the app level (for app-specific files). By placing CSS and JS inside the static/ directory, we can reference them in templates using the {% load static %} template tag and then link them with <link> or <script> tags. This works much like in any other web application, but Django’s static file management ensures that the files are correctly served in development and collected in one place for production.

---

**In your own words, explain the steps you’d need to take to deploy your Django web application.**

To deploy my Django application, I prepared everything in advance by setting up environment variables, generating a new SECRET_KEY, adjusting security settings, updating requirements.txt with gunicorn, and creating a render.yaml configuration file. I also tested the app locally with production settings (DEBUG=False) to make sure everything worked as expected.

For deployment, I pushed my code to GitHub and then connected the repository to Render.com. On Render, I created a new Web Service, configured the build and start commands (including running collectstatic and migrations), and set all the necessary environment variables (like SECRET_KEY, DEBUG=False, and ALLOWED_HOSTS).

Once deployed, I verified that the application loaded correctly, that static files and media were served properly, and that HTTPS and security headers were working. I also tested key features such as login/logout, recipe lists, and search.

Overall, the process involved preparing my Django project for production, connecting it to a hosting platform, and then testing everything carefully after deployment to ensure the app was secure and functional.

---

**You’ve now finished Achievement 2 and, with it, the whole course! Take a moment to reflect on your learning:**

a. **What went well during this Achievement?**

b. **What’s something you’re proud of?**

c. **What was the most challenging aspect of this Achievement?**

d. **Did this Achievement meet your expectations? Did it give you the confidence to start working with your new Django skills?**
