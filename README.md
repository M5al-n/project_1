Plant Care Tracker
Introduction
This is a Python program developed through Streamlit, used for managing the plants owned by the user. Plant data is provided in CSV form, whereas an external Plant API is used for fetching data related to watering and sunlight.

Problem and Solution
People owning plants may have problems keeping track of watering schedules, care tips, and data related to the plants they own. This program enables the user to consolidate all the data and provides care tips from an external API.

Main Pages
Dashboard
Shows the total number of plants, care tasks, growth logs, and saved plants.

Add New Plant
Used for adding a new plant and retrieving the watering and sunlight information from an API.

Record Care
Used to log the tasks such as watering, fertilization, repotting, and pruning.

Due for Care
Lists out plants that need watering.

Search Plants
Enables the user to search for their plants by name or location.

View All Plants
Displays all saved plants.

Track Growth
Tracks the height and measurement date of plants.

Seasonal Care
Helps users remember the seasonal care needs.

Plant Photos
Uploads pictures of the plants.


Schedule Adjustment
Depends upon seasonal variations to adjust the watering schedule accordingly.

Plant Doctor
Suggests guidance according to symptoms of the problem.
Plant Care Assistant
Provides general information about caring for plants.

Technologies
Python
Streamlit
Pandas
CSV
Plant API
Requests
Deployment Problem
After deployment of the program to Streamlit Cloud, some texts became hard to see due to different themes locally and on the cloud service.
