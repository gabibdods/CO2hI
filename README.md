# CO<sub>2</sub>hI

# Flight Polution Web Calculator

### Description

- A full-stack web application developed using Django and Python that estimates the carbon emissions of commercial flights based on user-specified parameters, including aircraft type, route distance, cruise speed, and passenger load
- Originally designed as an educational project, it reflects an early hands-on attempt at full-stack environmental modeling

---

## NOTICE

- Please read through this `README.md` to better understand the project's source code and setup instructions
- Also, make sure to review the contents of the `License/` directory
- Your attention to these details is appreciated — enjoy exploring the project!

---

## Problem Statement

- Air travel is a significant contributor to global CO<sub>2</sub> emissions, yet the environmental cost of individual flights remains abstract for most travelers
- This project addresses that gap by providing a transparent calculator for flight-related emissions based on engineering assumptions and user input

---

## Project Goals

### Estimate CO<sub>2</sub> emissions for a flight

- Generate carbon emission estimates using cruise speed, distance, passenger count, and aircraft specifications as inputs

### Provide a web-based, interactive input/output interface

- Deliver an intuitive web interface with real-time form submission, interactive outputs, and responsive design

### Learn full-stack development using Django

- Gain hands-on experience building complete web applications using Django’s MVT architecture

### Explore environmental modeling through code

- Develop simplified physics-based models of aircraft emissions and implement them using Django views and logic

---

## Tools, Materials & Resources

### Django Framework with Python

- Core web application built with Django and Python 3, using Django’s templating engine, forms, and model features

### SQLite3 Database

- Lightweight, file-based relational database used to store input and output data without needing external dependencies

### HTML, CSS, JavaScript (VS Code)

- Used for rendering and styling the frontend, allowing dynamic interaction with form submissions and results

---

## Design Decision

### Constant cruise speed assumed after takeoff

- Emissions calculations begin after the plane reaches cruising speed, using brake horsepower and constant velocity assumptions

### CO₂ emissions derived from estimated fuel consumption per kilometer per passenger

- Fuel burn rate is estimated per kilometer, normalized by the number of passengers for greater realism and scalability

### Simplified distance calculations without altitude or 3D trajectory

- Due to limited math background at the time of development, the model excludes three-dimensional calculations and focuses on straight-line distance

---

## Features

### CO<sub>2</sub> Emissions Estimation for Flights

- Calculates emissions based on user inputs: route, speed, aircraft type, and passenger load

### Realistic Engineering-Based Calculations

- Implements simplified physical assumptions (e.g., constant cruise) to estimate carbon output

### Interactive Web Interface

- Intuitive web-based input forms and output views using Django templates and static assets

### Lightweight & Self-Contained

- Easily deployable using Django’s built-in development server and SQLite3

---

## Block Diagram

```plaintext
                                 ┌────────────────────────┐
                                 │    User Web Browser    │
                                 │╔══════════════════════╗│
                                 │║  Inputs Flight Data  ║│
                                 │╚══════════════════════╝│
                                 └──────────┬─────────────┘
                                            ↓
                               ┌────────────▼─────────────┐
                               │       Django Views       │
                               │╔════════════════════════╗│
                               │║ Handles Form Requests  ║│
                               │╚════════════════════════╝│
                               └───────────┬──────────────┘
                                           ↓
                             ┌─────────────▼───────────────┐
                             │     Emission Calculator     │
                             │╔══════════════════════════╗ │
                             │║ Cruise Speed & BHP Model ║ │
                             │║ Fuel Burn Rate Estimates ║ │
                             │╚══════════════════════════╝ │
                             └──────────────┬──────────────┘
                                            ↓
                             ┌──────────────▼───────────────┐
                             │     Environmental Model      │
                             │╔════════════════════════════╗│
                             │║   CO2 = Fuel * Km / Pax    ║│
                             │║ (Excludes altitude model)  ║│
                             │╚════════════════════════════╝│
                             └───────────────┬──────────────┘
                                             ↓
                             ┌───────────────▼───────────────┐
                             │        Django Templates       │
                             │╔════════════════════════════╗ │
                             │║  Renders Results in HTML   ║ │
                             │║     + CSS + JavaScript     ║ │
                             │╚════════════════════════════╝ │
                             └───────────────┬───────────────┘
                                             ↓
                                   ┌─────────▼──────────┐
                                   │  Output Web Page   │
                                   │╔══════════════════╗│
                                   │║  Emission Report ║│
                                   │╚══════════════════╝│
                                   └────────────────────┘

```

---

## Functional Overview

- Users submit flight parameters through the web interface
- Django views process the request and execute the emission model
- Engine performance and environmental assumptions are applied
- Django templates render a CO<sub>2</sub> emissions report in-browser

---

## Challenges & Solutions

### Lack of real-world datasets on aircraft fuel specifications

- Used brake horsepower and basic engineering estimates to simulate cruise-phase fuel burn

### Limited knowledge of spherical geometry and 3D calculus

- Distance calculations were simplified to straight-line estimates to keep the model approachable

### First-time Django MVT project

- Gained experience mapping models, views, and templates while learning Python web development best practices

---

## Lessons Learned

### Technical Field

- Django deployment, local server operation, and form handling using POST requests

### Environmental Field

- Quantitative understanding of flight-related carbon emissions and the need for modeling emissions early in software projects

### Mathematical Field

- Introduction to geometric modeling, fuel consumption estimation, and the basics of physics-based software simulation

---

## Project Structure

```plaintext
root/
├── License/
│   ├── LICENSE.md
│   │
│   └── NOTICE.md
│
├── .gitattributes
│
├── .gitignore
│
├── README.md
│
├── Lecture1-HTML_&_CSS/
│   └── HTML file notes from the CS50 lecture
│
├── Lecture2-Git/
│   └── Lecture notes from the CS50 lecture and more transported to https://github.com/gabibdods/GitTorial
│
├── Lecture3-Python/
│   └── Python file notes from the CS50 lecture
│
├── Lecture4-Django/
│   └── Example miniature Django server from the CS50 lecture
│
├── Lecture5-SQL_Models_&_Migrations/
│   └── Lecture notes combined with Lecture 4 notes
│
├── Lecture6-JavaScript/
│   └── JavaScript file notes from the CS50 lecture
│
├── Lecture7-User_Interfaces/
│   └── HTML file notes from the CS50 lecture
│
├── Lecture8-Testing_&_CI/CD/
│   └── File notes lost due to poor file transcription process
│
└── Lecture9-Scalability_&_Security/
    └── File notes lost due to poor file transcription process

```

---

## Future Enhancements

- Restore lost source code files and reconstruct the web app for deployment
- Implement geographic calculations with proper elevation and curvature
- Add advanced modeling for takeoff/landing phases and fuel type differences
- Build an interactive emissions map or visual dashboard for route comparisons
