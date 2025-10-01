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

What went well during this Achievement was that the course felt clear, structured, and engaging. The concepts were explained in a straightforward way, and I didn’t feel lost at any point. Everything we covered felt useful and directly connected to practical applications. I especially enjoyed how the course balanced theory with hands-on practice, which made the learning experience smooth and rewarding. More than anything, I discovered that I really enjoy working with Python—this Achievement actually made me fall in love with the language.

b. **What’s something you’re proud of?**

Something I’m especially proud of is the sense of accomplishment I get when I finish a project. I still remember the first time, over 20 years ago, when I saw a billboard I had designed out in the city, or when I launched my first website in 2005. That same feeling is still with me today—seeing something I’ve built come to life, ready to be used and useful, is incredibly powerful. This course gave me more of those moments, and I’m proud of everything I’ve learned and created along the way.

c. **What was the most challenging aspect of this Achievement?**
I didn’t find any single aspect overwhelmingly challenging during this Achievement. Some concepts required effort to fully understand, but with the clear explanations and mentoring provided, what first looked like a mountain quickly became just a hill to climb. I also experimented with slightly different tools than the ones suggested in the exercises—for example, I deployed on Render.com instead of Heroku—and everything worked out well. To me, that’s part of what it means to be a developer: being able to adapt, explore alternatives, and find your own way when needed. This challenge of independence was also a valuable part of the learning process.

d. **Did this Achievement meet your expectations? Did it give you the confidence to start working with your new Django skills?**

Yes, this Achievement definitely met my expectations. I now understand the architecture of a Django web application—still at a simple level, but it’s a strong foundation to build on. I also gained a sense of how complex Django apps can become, which gave me perspective on where I am in my learning journey.

It has given me the confidence to start working on Django projects, at least with simpler tasks to begin with. In fact, I’ve already taken a first step: after talking with a friend who is a seasoned full-stack developer, he invited me to join a project he’s working on, with an Angular front end and a Django back end. The project is quite complex, and it feels a bit intimidating, but thanks to this course, I can now look at the code and actually understand parts of what’s going on. That alone feels like real progress and motivates me to keep learning.
