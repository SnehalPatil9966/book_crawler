
# book_crawler
Web Crawling Pipeline
Overview
This project is a web crawling pipeline designed to extract and process product information from an e-commerce website. Using the Scrapy framework, the crawler fetches data, cleans and standardizes it, and stores it in a MongoDB database for further use.
The target website for this project is Books to Scrape, a publicly accessible e-commerce site for books. The crawler adheres to the website's robots.txt policy to ensure compliance.
Features
1.	Web Crawling: Extract product details such as Product Name, Price, Rating, and Availability Status.
2.	Data Transformation: Clean and standardize the extracted data.
3.	Data Storage: Store the processed data into a MongoDB database.
Setup Instructions
Prerequisites
1.	Python 3.x installed on your system.
2.	MongoDB installed and running locally or accessible remotely.
3.	Dependencies: Install required Python libraries.
Installation
1.	Clone the repository:
2.	git clone <repository_url>
3.	cd <repository_folder>
4.	Set up a Python virtual environment (optional but recommended):
5.	python -m venv venv
6.	source venv/bin/activate  # On Windows: venv\Scripts\activate
7.	Install required libraries:
8.	pip install scrapy pymongo
Running the Spider
1.	Start the MongoDB service:
2.	mongod
3.	Navigate to the project folder and run the Scrapy spider:
4.	scrapy crawl books
5.	The extracted data will be stored in the books_db database under the products collection in MongoDB.
Project Structure
•	spiders/ 
o	Contains the Scrapy spider for crawling the website.
•	pipelines.py 
o	Defines the MongoDB pipeline for storing data.
•	settings.py 
o	Configures Scrapy settings such as pipelines and MongoDB connection.
Data Schema
Data is stored in a MongoDB collection named products with the following schema:
•	product_name (string): Name of the product.
•	price (float): Price of the product.
•	rating (float): Rating of the product (1.0 to 5.0).
•	availability (string): Product availability status ("In Stock" or "Out of Stock").
Git Guidelines
1.	Use meaningful branch names, e.g., feature/<your_name>.
2.	Commit messages should be concise and descriptive: 
o	"Initialize Scrapy project and add spider for web crawling."
o	"Implement data transformation logic."
o	"Add MongoDB integration for data storage."
3.	Create a Pull Request (PR) to the main branch after completing the implementation.
Dependencies
•	Scrapy: Web crawling framework.
•	PyMongo: Python driver for MongoDB.
•	MongoDB: NoSQL database for storing processed data.
References
•	Scrapy Documentation
•	MongoDB Documentation
License
This project is licensed under the MIT License. See the LICENSE file for details.

