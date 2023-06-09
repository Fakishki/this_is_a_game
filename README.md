# CLI Airport Flight and Passenger Management System

## Overview
The CLI Airport Flight and Passenger Management System is a Command Line Interface (CLI) application for managing flights, airlines, passengers, and lost luggage at the CLI Airport. The application allows users to view flight details, view airline details, view passenger lists, book passengers on flights, rebook passengers, and assist with lost luggage.

## Getting Started

### Requirements

- Python 3.x
- SQLAlchemy

### Installation

1. Clone the repository or download the source code
2. Install the required Python packages: SQLAlchemy and ipdb (if not already installed)
3. Run "pipenv install"
4. Navigate to the /app folder
5. Run "pipenv shell"
6. Run "python seed.py" to install all the database seed data... wait for the intallation to finish
7. Run "python cli.py" to start the application

## Usage

The application provides a user-friendly command-line interface for managing the airport system. The main menu provides the following options:

1. Flights view today's scheduled flights and their details.
2. Airlines - view all airlines operating at CLI and their scheduled flights.
3. Passengers - view all passengers, booked passengers, and passengers awaiting flights.  You can even book and rebook passengers onto different flights.
4. Luggage Lost & Found - manage lost luggage by listing all luggage ordered by bag tag or passenger name.
5. Exit Application - exit the application.

## Application Structure
The application is organized into the following files:

### cli.py:
The main application file containing the command-line interface.

### helpers.py:
A set of helper functions for various tasks such as printing, displaying flights, airlines, passengers, and luggage.

### models.py:
Contains the SQLAlchemy ORM models for the Airline, Flight, Passenger, and Bag entities.

### seed.py
Contains data seeding for the database.

Other files, such as alembic.ini, are related to database versioning and migrations.

## Support
If you need help or find any issues with the application, please open a new issue on the project's GitHub page or reach out to the project maintainer.onfiguration.

## Copyright
This application was created by and is owned by Walter Pfingsten of Seattle, WA (2023)# this_is_a_game_for_jason
