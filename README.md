# DjangoProject

This Django project provides a robust system for user signup, login, and profile management. It offers features for user registration, user data retrieval, updating user details, and deleting user accounts. The project utilizes Django's built-in features for model creation, views implementation, URL routing, and template rendering to deliver seamless user interaction and efficient data management. Thorough testing with Postman ensures the reliability and functionality of all CRUD operations.

## Features

1. **Project Setup**: 
   - Created a virtual environment named DjangoAssignment.
   - Initialized a Django project named Login System.
   - Added an application called Loginify.
   
   
2. **Views and URL Configuration**: 
   - Implemented urls.py in the Loginify app for URL routing.
   - Mapped URLs for login, signup, profile management, and other functionalities.
   
3. **Model Definitions**: 
   - Created a model named UserDetail for storing user information.
   - Designed a UserDetailForm module to handle user data input.
   - Built dynamic Django templates for:
		- Home Page
		- Login Page
		- Signup Page
		- Profile Page
   
4. **Admin Panel Configuration**: 
   - Created a superuser for the Django admin interface using shell commands.
   - Performed the following operations via the admin panel and shell:
		- Added dummy records.
		- Updated existing records.
		- Retrieved records for validation.
		- Deleted unnecessary records.
   
5. **CRUD Operations via API**: 
   - Installed required dependencies:
		- django-rest-framework for creating REST APIs.
		- django-rest-framework-simplejwt for JWT authentication.
   - Developed REST APIs for managing user data:
		- POST: Create token
		- POST: Refresh token
		- POST: Verify token
		- GET: Retrieve all user records.
		- GET by Username: Fetch a specific user by their username.
		- POST: Insert a new user record.
		- PUT: Update user details by username.
		- DELETE: Remove a user account by username.