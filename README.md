# Movie Recommendation App 🎬

A **Django REST Framework** project that allows users to explore movies, like/unlike them, comment on movies, and get recommendations based on genre and popularity. Only authenticated users can interact with the app.

---

## Features

- **User Authentication**: Register and login using token-based authentication  
- **Movies**: View a list of movies  
- **Likes**: Like or unlike movies  
- **Comments**: Create, update, and delete comments on movies  
- **Recommendations**: Get movies by genre, sorted by number of likes, with nested comments  

---

## Tools & Technologies Used

- **Python 3.13**  
- **Django 4.x**  
- **Django REST Framework**  
- **SQLite** (default database)  
- **Postman** (for API testing)  

---

## What the API Does

1. **User Endpoints**:  
   - Register and login to get an authentication token  
2. **Movie Endpoints**:  
   - List all movies  
   - Like and unlike movies  
3. **Comment Endpoints**:  
   - Add, update, or delete comments on movies  
4. **Recommendation Endpoint**:  
   - Returns movies in a selected genre, sorted by likes, with all comments nested under each movie  

---

This API is fully token-protected, so only authenticated users can like, comment, or access recommendations.

preview:https://gbemi123.pythonanywhere.com/
