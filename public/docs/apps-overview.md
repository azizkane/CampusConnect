# Backend Breakdown

## Overview

The backend of CampusConnect is designed to handle various functionalities through a modular approach, with each app responsible for a specific domain.

### Apps and Their Responsibilities

## Core App
- **Accounts**: Manages user authentication, authorization, and profile management. Handles different user roles such as Super Admin, School Admin, Managers, and Students.

- **Schools**: Manages school-specific data, including school profiles, associated users, and school-wide settings.

- **Students**: Handles student-specific data and interactions, including enrollment, progress tracking, and participation in projects and events.

- **Billing**: Handles subscription plans and payments, allowing the Super Admin to assign and manage pricing plans based on student numbers.

## Features App
- **Calendar**:
  - **Projects**: Provides tools for project creation, task management, role assignment, and progress tracking for student projects.
  - **Events**: Manages the planning and organization of seminars, workshops, and study sessions, including invitations and resource sharing.
  - **CalendarSettings**:
  - **SharedCalendar**: 

- **Libraries**: Manages educational resources, allowing schools to maintain private libraries or share resources with other institutions.

- **Forums**: Facilitates group discussions, Q&A, and community interactions, with moderation features to ensure constructive communication.

## Utils App
- **Mailjet**: Manages email communications and notifications.

## System App
- **Audit**: Handles auditing and logging of system activities for security and compliance purposes.
- **Authentication**: Manages system-level authentication mechanisms and integrations.

## Database Integration

- **PostgreSQL**:
  - Manages core relational data for the following apps:
    - Accounts
    - Schools
    - Students
    - Billing
    - System Apps

- **MongoDB**:
  - Handles flexible, unstructured data for the following apps:
    - Libraries
    - Events
    - Projects
    - Forums
    - Calendar.app
