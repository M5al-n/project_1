# Plant Care Tracker

## Introduction

This is a Python application built using Streamlit for managing the user's plants. The plant data is stored in CSV format, while a Plant API is used to retrieve information about watering and sunlight.

## Problem and Solution

Users who own plants may forget watering schedules, care tips, and plant information. This tool helps users by organizing all the data together and providing care information from an external API.

## Main Pages

### Dashboard
Lists total plants, care activities, growth records, and saved plants.

### Add New Plant
Adds a new plant and gets watering and sunlight details from the API.

### Record Care
Records watering, fertilizing, repotting, and pruning activities.

### Due for Care
Displays plants that require watering.

### Search Plants
Allows users to search for plants by name or location.

### View All Plants
Displays all saved plants.

### Track Growth
Tracks the height and measurement date of plants.

### Seasonal Care
Reminds users about seasonal care requirements.

### Plant Photos
Uploads photos of plants.

### Adjust Schedule
Modifies the watering schedule according to the season.

### Plant Doctor
Gives suggestions about possible issues based on symptoms.

### Plant Care Assistant
Gives basic answers regarding plant care.

## Technologies

### Python
### Streamlit
### Pandas
### CSV
### Plant API
### Requests

## Deployment Issue

After the program was deployed on Streamlit Cloud, some text appeared too light because of differences between the local and deployed themes.

Solution


CSS was employed in changing the text color into dark text color while retaining the light-green design.

Plant Care Tracker Application: https://plant-care212.streamlit.app/

Project Introduction Video:
