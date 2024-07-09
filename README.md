# RentSage

RentSage is a web scraping web application that analyzes rent prices in user-selected locations. It considers various factors such as proximity to college campuses, affordability, safety and security, amenities and facilities, and potential roommates. This tool aims to provide valuable insights for individuals searching for rental properties in different cities.

## Features

- **Web Scraping:** Automatically fetches rental price data from Craigslist based on user-selected city.
- **Data Analysis:** Analyzes rent prices along with proximity to the nearest college campus, safety statistics, amenities, and more.
- **Interactive Interface:** Provides a user-friendly interface to explore analyzed data and make informed decisions.

## Technologies Used

- **Python:** Backend scripting and web scraping using `requests` and `BeautifulSoup`.
- **Flask:** Web framework for building the backend server.
- **React:** Frontend framework for building an interactive user interface.
- **HTML/CSS:** Styling and structuring the frontend components.
- **Git:** Version control and collaboration via GitHub.

## Setup

To run RentSage locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rentsage.git
   cd rentsage

2. Install dependencies for both frontend and backend:
    # For backend (Flask)
    cd backend
    pip install -r requirements.txt

    # For frontend (React)
    cd ../frontend
    npm install

3. Start the backend server (Flask) and frontend development server (React):
    # In one terminal/tab, start the Flask backend
    cd ../backend
    python app.py

    # In another terminal/tab, start the React frontend
    cd ../frontend
    npm start

4. Open your web browser and navigate to http://localhost:3000 to view the RentSage application.

Contributing
Contributions to RentSage are welcome! If you'd like to contribute, please fork the repository, create a new branch, commit your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License - see the LICENSE file for details.


Replace placeholders like `your-username`, `your-email`, and adjust any specific paths or details according to your project setup. This README provides a basic structure to help users understand what the project does, how to set it up locally, how to contribute, and where to find more information.




