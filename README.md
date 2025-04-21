# Car Price Predictor

This web application predicts the price of a used car based on various attributes such as the car's company, model, year, fuel type, and kilometers driven. The application uses a machine learning model trained on a dataset to predict the price of the car based on the selected parameters.

## Features

- **Dynamic Dropdowns**: Select a car company, model, year, fuel type, and kilometers driven to predict the car's price.
- **Responsive Design**: The interface is responsive and adapts to different screen sizes.
- **User-Friendly Interface**: A clean, simple, and intuitive design for easy car price prediction.
- **Prediction Result**: Displays the predicted price of the car based on the user input.
  
## Technologies Used

- **Flask**: A Python web framework used to build the server-side logic.
- **HTML/CSS**: For structuring and styling the web pages.
- **Bootstrap 5**: A front-end framework used to build a responsive and mobile-first design.
- **JavaScript**: For handling dynamic dropdown changes and form submission.

## Installation

To run this project locally, follow the steps below:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/car-price-predictor.git

2. **Navigate into the Project Directory**

   cd car-price-predictor

3. **Install Dependencies**:
   
   pip install -r requirements.txt

4. **Run the Flask Application**:
   
   python app.py

5. **Open the Application**:
   
   Open your browser and go to http://127.0.0.1:5000/ to use the Car Price Predictor.

Usage
1. Select the Company of the car from the dropdown.

2. Once a company is selected, the Model dropdown will populate with available models from that company.

3. Choose the Year, Fuel Type, and enter the Kilometers Driven.

4. Click the "Predict Price" button to get the predicted price of the car.

5. The predicted price will appear below the form after submission.

------------------------------------------------------------------------------

Project Structure

car-price-predictor/
│
├── app.py                  # Main Python script running the Flask server
├── templates/
│   ├── index.html          # HTML template for the car price predictor form
├── static/
│   ├── styles.css          # Custom CSS for styling the page
│   └── js/
│       └── script.js        # Custom JavaScript for handling form and dropdown behavior
├── requirements.txt        # List of Python dependencies
└── README.md               # Project documentation

Requirements
1. Python 3.6 or higher
2. Flask
3. Bootstrap (via CDN)
4. Other Python dependencies in requirements.txt

Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to fork the project and submit a pull request.

1. Fork the repository
2. Create a new branch (git checkout -b feature/your-feature-name)
3. Make your changes and commit them (git commit -am 'Add new feature')
4. Push to the branch (git push origin feature/your-feature-name)
5. Create a new pull request
