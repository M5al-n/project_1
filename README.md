# Plant Care Tracker

 Introduction

This is a Python application built using Streamlit for managing the plants belonging to the user. The plant data is stored in CSV format, while plant API is used to retrieve information about watering and sunlight.

Problem and Solution

Users who own plants tend to forget the water schedule, care tips and plant information. This tool helps users by organizing all the data together and providing care tips from an external API.

Main Pages

* Dashboard: Lists total plants, care activities, growth activities, and saved plants.

* Add New Plant: Adds new plant and gets water and sun details from the API.

* Record Care: Cares for watering, fertilizing, re-potting, and trimming of plants.

* Due for Care: Displays plants which require watering.

* Search Plants: Allows search of plants by name or place.

* View All Plants: Displays all the saved plants.

* Track Growth: Tracks height and date of plants.

* Seasonal Care: Reminds users about seasonal care requirements.

* Plant Photos: Uploads photos of plants.

* Adjust Schedule: Modifies watering schedule according to the season.

* Plant Doctor: Gives suggestions about probable issues based on symptoms.

* Plant Care Assistant: Gives basic answers regarding plant care.s.

Technologies

* Python

* Streamlit

* Pandas

* CSV

* Plant API

* Requests
 Deployment Issue

There was an issue in that once the program was deployed onto Streamlit cloud, there were texts that looked lighter because of the difference in themes.

Solution

CSS was employed in changing the text color into dark text color while retaining the light-green design.

