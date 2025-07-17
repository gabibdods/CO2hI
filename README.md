# ✈️ Plane Consumption Calculator — Estimating the Environmental Impact of Air Travel

A full-stack web application built with Django, Python, and SQLite that calculates the estimated CO2 emissions of airplane flights based on aircraft type, route distance, cruise speed, and passenger load. This was my first large-scale project, testing the limits of my capabilities. Unfortunately, a lot of the files were corrupted due to faulty storage management, so only are left the lecture notes I take from taking a web development course using python and the django framework.

## 🔍 Problem Statement

Air travel is a major contributor to global carbon emissions. Yet, most people lack awareness of how much CO2 a specific flight produces. This project aims to raise environmental awareness by allowing users to input flight parameters and receive an estimate of the associated CO2 emissions.

## 🎯 Project Goals

- Estimate CO2 emissions for a flight based on:
  - Departure and arrival cities
  - Aircraft type
  - Cruise speed
  - Number of passengers
- Provide a web-based, interactive input/output interface
- Learn full-stack development using Django
- Explore environmental modeling through code

## 🛠️ Technologies Used

- **Backend:** Django (Python), SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Development Environment:** Visual Studio Code
- **Server:** Localhost using Django's development server

## 🔧 Features

- User-friendly input form for flight details
- Backend calculation of CO2 emissions
- SQLite database for data handling
- Dynamic frontend interface with clean UI
- Emphasis on environmental education

## 📈 Design Assumptions

- Constant cruise speed assumed throughout the flight
- Zero acceleration assumed during flight phase
- CO2 emissions estimated from fuel consumption per kilometer per passenger
- Simplified distance calculations without altitude considerations

## 🧩 Challenges Faced

- Finding reliable datasets on aircraft specs (engine type, fuel use, weight)
- Limited mathematical knowledge to model 3D spherical distances and acceleration curves
- Understanding and implementing Django’s MVT architecture for the first time

## 📚 Lessons Learned

### Technical

- Configuring and deploying Django projects
- Handling HTTP requests and form data
- Local server hosting and database integration

### Environmental

- Quantitative insight into aviation’s environmental footprint
- The need for cleaner alternatives to current air travel technologies

### Mathematical

- Basic understanding of line integrals and spherical geometry
- Application of mass and acceleration to estimate fuel consumption