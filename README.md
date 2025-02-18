# CampusConnect


## Overview
**CampusConnect** is a comprehensive project management application designed for students in colleges, high schools, and educational institutes. It aims to facilitate organization and collaboration within clubs, classes, and student groups, while integrating essential aspects of school life.

## Features

### 1. **University Calendar**
   - **Important Dates**: Integration of key dates such as homework deadlines, exams, school holidays, and other academic events.
   - **School Life Events**: Display of events organized by the school life department, such as open days, conferences, workshops, etc.
   - **Custom Event Categories**: Create and manage custom event categories for better organization.
   - **Notifications**: Alerts for important dates and events. 

### 2. **Project Planning Tool**
   - **Project Creation**: Students can create and manage individual or group projects.
   - **Tasks and Subtasks**: Breakdown of projects into tasks and subtasks with specific deadlines.
   - **Role Assignment**: Assignment of roles and responsibilities within work groups.
   - **Progress Tracking**: Dashboards to track the progress of projects and tasks.
   - **Resource Allocation**: Manage and track project resources and budgets.
   - **Timeline Visualization**: Gantt charts and timeline views for project planning.

### 3. **Seminar and Study Session Planning**
   - **Event Creation**: Students can plan seminars, workshops, study sessions, and other educational events.
   - **Invitations and Participation**: Sending invitations to group members and tracking participation confirmations.
   - **Shared Resources**: Sharing of documents, presentations, and other resources necessary for the events.
   <!-- - **Room Booking**: Integrated room reservation system for events. ---------- PERSPECTIVE --------- -->

### 4. **Forums Section**
   - **Group Discussions**: Spaces for discussion for clubs, classes, and student groups.
   - **Q&A**: Platform for asking questions, sharing ideas, and getting answers from the community.
   - **Moderation**: Moderation features to ensure respectful and constructive discussions.
   - **Topic Categories**: Organized discussion topics with tags and categories.
   <!-- - **Reputation System**: User reputation points based on contributions. --------PERSPECTIVE---------- -->

### 5. **Library**
   - **Educational Resources**: Access to a library of educational resources, including articles, videos, e-books, and other useful documents.
   - **Student Contributions**: Ability for students to contribute by adding their own resources and sharing relevant documents.
   - **Resource Categories**: Organized content by subjects, topics, and types.
   <!-- - **Advanced Search**: Search tools to quickly find necessary resources. -->

## Goals of CampusConnect

- **Organization and Planning**: Help students better organize their time and plan their projects and events.
- **Collaboration**: Facilitate collaboration between students, teachers, and school life members.
- **Engagement**: Encourage engagement and active participation in clubs, classes, and student groups.
- **Resource Access**: Provide easy access to a variety of educational resources and support.

## Architecture

### Backend (Django)
- **Business Logic and Data Management**: Handles the business logic and data management.
- **RESTful API**: Exposes a RESTful API via Django Rest Framework.
- **Database Interaction**: CampusConnect utilizes multiple databases to optimize performance and scalability. (PostgreSQL, MongoDB)
- **Authentication and Authorization**: Manages authentication and authorization.
<!-- - **Caching Layer**: Redis for performance optimization. ---------- PERSPECTIVE ----------- -->
<!-- - **Task Queue**: Celery for background task processing. ---------- PERSPECTIVE ----------- -->

### Database Configuration
- **PostgreSQL**: Manages core relational data for modules such as **accounts**, **schools**, **students**, and **billing**.
- **MongoDB**: Handles flexible, unstructured data for modules like **libraries**, **forums** and **calendar**.
For more details, see [our detailed documentation on database integration](public/docs/apps-overview.md)

### Frontend (Next.js + React)
- **Interactive User Interface**: Creates the interactive user interface using Next.js and React.
- **Backend Communication**: Communicates with the backend via HTTP requests (using axios).
<!-- - **Client-Side State Management**: Manages the application state on the client side using Redux. ---- PERSPECTIVE ----------- -->
- **Navigation**: Allows navigation between different views.
- **Shadcn**: Utilizes Shadcn UI for a consistent and responsive design.
- **Progressive Web App**: Support for offline functionality and mobile-first design. 


### Data Flow
1. **User Interaction**: The user interacts with the React interface.
2. **API Requests**: React sends requests to the Django API.
3. **Request Processing**: Django processes the requests and interacts with the database.
4. **Data Return**: Django returns the data to the frontend.
5. **UI Update**: React updates the user interface.
6. **Real-time Updates**: WebSocket integration for live updates.

## License

This project is licensed under the APACHE License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please contact me.

| Auteur  | Date       | email|
|---------|---------------|--------|
| Aziz Kane  | 09/10/2023  |[aziukane@gmail.com](mailto:aziukane@gmail.com)|

---

This `README.md` file provides a clear and structured overview of the CampusConnect application, its features, benefits, architecture, and how to get started.
