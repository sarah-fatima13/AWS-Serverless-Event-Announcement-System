# AWS-Serverless-Event-Announcement-System

## Project Overview:

This project implements a **serverless event announcement system on AWS** that allows users to subscribe to event notifications, view upcoming events, and create new events using a web interface. The frontend is hosted on **Amazon S3**, while backend processing is handled using **AWS Lambda**, **Amazon SNS**, and **Amazon API Gateway**.

The system is fully event-driven, scalable, cost-effective, and demonstrates real-world serverless application design using AWS cloud services.

## File Summary:

* **index.html** – Frontend website for viewing, creating events, and subscribing.
* **styles.css** – Website styling.
* **events.json** – Stores event data.
* **subscribeToSNSFunction.py** – Lambda function for email subscription.
* **createEventFunction.py** – Lambda function for event creation and notification.
* **architecture-diagram/** – AWS architecture diagram.
* **event-announcement-working-images/** – Screenshots of working project.
* **README.md** – Project documentation.


## Architectural Diagram:




## Project Steps (Working):


### 1. Design Serverless Architecture

A serverless architecture was designed using Amazon S3 for frontend hosting, AWS Lambda for backend logic, SNS for notifications, and API Gateway for API communication.


### 2. Create S3 Bucket & Upload Website Files

An S3 bucket was created and the frontend files (index.html, styles.css, events.json) were uploaded.


### 3. Enable Static Website Hosting

Static website hosting was enabled to provide public access to the website.


### 4. Configure Bucket Policy for Public Access

A bucket policy was applied to allow public read access to website files.


### 5. Create SNS Topic

An SNS topic named **EventAnnouncements** was created to manage subscriptions and send notifications.

### 6. Create Subscription Lambda – subscribeToSNSFunction

A Lambda function was created to subscribe user email addresses to the SNS topic.


### 7. Create Event Lambda – createEventFunction

A Lambda function was created to store new events in S3 and notify subscribers.



### 8. Setup API Gateway Endpoints

Two API endpoints were created:

* **POST /subscribe**
* **POST /create-event**



### 9. Integrate API with Frontend

API Gateway endpoints were integrated into the frontend for seamless user interaction.


### 10. End-to-End Testing

The entire workflow was tested successfully:

* Email subscription
* Event creation
* SNS notifications
* Event display update

## AWS Services Used:

* Amazon S3
* AWS Lambda
* Amazon SNS
* Amazon API Gateway
* AWS IAM

## Note:

All AWS resources used for this project were deleted after completion to avoid unintended charges, as the project was implemented using the AWS Free Tier.

