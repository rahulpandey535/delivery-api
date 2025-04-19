# Delivery Cost Calculator API

This is a simple Flask-based REST API that calculates the minimum delivery cost for a customer's order based on product availability across three warehouse centers (C1, C2, C3). This project was built as part of a final assessment to practice backend development and API deployment.

## Project Description

There are 3 warehouse centers, each storing a specific set of products (A to I). A customer can place an order for any number of these products, and the system must decide how to fulfill the order using a single delivery vehicle. The vehicle may pick up products from multiple centers and deliver to the customer location (L1), possibly in multiple trips. The goal is to minimize the total delivery cost.

## Technologies Used

- Python 3
- Flask
- Git and GitHub
- Render (for deployment)

## How the API Works

The API exposes a single POST endpoint that takes a JSON object representing the quantity of each product in the order. It calculates and returns the minimum delivery cost required to fulfill the order.

### API Endpoint

POST /calculate-cost

### Example Request Body

```json
{
  "A": 1,
  "B": 1,
  "C": 1,
  "G": 1,
  "H": 1,
  "I": 1
}
Example Response
{
  "minimum_cost": 118
}
Business Logic Overview

Only one delivery vehicle is used per order.
The vehicle can pick up products from more than one center and deliver to L1 multiple times.
Cost is calculated as: 2 * distance to L1 * ₹2/km (round trip per center).
The best combination of routes is chosen to minimize the total cost.
Test Cases (As per the assessment)


Order	Expected Cost
A-1, G-1, H-1, I-3	86
A-1, B-1, C-1, G-1, H-1, I-1	118
A-1, B-1, C-1	78
A-1, B-1, C-1, D-1	168
Running Locally

Clone the repository
Create a virtual environment and activate it
Install dependencies using pip install -r requirements.txt
Run the application using python app.py
Example:
git clone https://github.com/rahulpandey535/delivery-api.git
cd delivery-api
python -m venv venv
source venv/bin/activate   # Or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
The API will start at http://localhost:5000
Deployment

This project is deployed using Render, which offers free web service hosting for Python applications.
About Me

I am a computer science student interested in backend development and API design. This project helped me understand how to structure a Flask application, implement business logic, and deploy an API to a live server.