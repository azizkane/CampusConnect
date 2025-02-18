## CampusConnect Models Structure

**CampusConnect** is a platform designed for educational institutions to facilitate management, organization, and collaboration among administrators, teachers, and students.


## System App (PostgreSQL)

### Security & Authentication Models
- **AuthToken**
  - Attributes: `user` (ForeignKey), `token`, `expiry_date`, `is_valid`, `timestamps`
  - Filters: `by_user`, `by_validity`, `by_expiry`

- **LoginAttempt**
  - Attributes: `user` (ForeignKey), `ip_address`, `success`, `timestamp`
  - Filters: `by_user`, `by_success`, `by_date_range`

- **PermissionGroup**
  - Attributes: `name`, `description`, `permissions`, `is_active`, `timestamps`
  - Filters: `by_name`, `by_permissions`, `by_active_status`

### Audit Models
- **Log**
  - Attributes:
    - `user` (ForeignKey)
    - `action` (ENUM: Create, Update, Delete, Login, Logout)
    - `entity_type`
    - `entity_id`
    - `changes` (JSON)
    - `ip_address`
    - `timestamp`
  - Filters: `by_user`, `by_action`, `by_date_range`, `by_entity_type`

## Core App (PostgreSQL)

### Accounts Models
- **User**
  - Attributes: 
    - `email` (unique)
    - `password` (hashed)
    - `first_name`
    - `last_name`
    - `phone_number`
    - `role` (ENUM: SuperAdmin, Admin, Manager, Student, Parent, Teacher)
    - `is_active`
    - `last_login`
    - `address`
    - `date_of_birth`
    - `timestamps`
  - Security:
    - Password hashing with bcrypt
    - JWT session management
    - Password reset functionality
  - Filters: `by_role`, `by_active_status`, `by_school`

- **UserProfile**
  - Attributes: `user` (OneToOne), `avatar`, `bio`, `preferences`, `timestamps`
  - Filters: `by_user`

### Billing Models
- **Plan**
  - Attributes:
    - `name`
    - `price_per_max_student`
    - `billing_cycle` (ENUM: Monthly, Quarterly, Yearly)
    - `features` (JSON)
    - `is_active`
    - `timestamps`
  - Filters: `by_active_status`, `by_billing_cycle`

- **Subscription**
  - Attributes:
    - `school` (ForeignKey)
    - `plan` (ForeignKey)
    - `start_date`
    - `end_date`
    - `student_count`
    - `total_amount`
    - `payment_status`(ENUM: Active, Pending, Expired, Cancelled)
    - `timestamps`
  - Filters: `by_school`, `by_status`, `by_date_range`, `by_payment_status`

### School Models
- **School**
  - Attributes:
    - `name`
    - `address`
    - `contact_info`
    - `admin` (ForeignKey to User)
    - `created_by` (ForeignKey to User, SuperAdmin)
    - `is_active`
    - `subscription` (ForeignKey to Subscription)
    - `logo`
    - `settings` (JSON)
    - `timestamps`
  - Filters: `by_admin`, `by_active_status`, `by_creator`, `by_subscription_status`

- **Department**
  - Attributes:
    - `name`
    - `school` (ForeignKey)
    - `head` (ForeignKey to User)
    - `description`
    - `is_active`
    - `timestamps`
  - Filters: `by_school`, `by_head`, `by_active_status`

- **Manager**
  - Attributes: 
    - `user` (OneToOne)
    - `school` (ForeignKey)
    - `department` (ForeignKey)
    - `permissions` (JSON: calendar, library, forum, projects)
    - `is_active`
    - `timestamps`
  - Filters: `by_school`, `by_department`, `by_permissions`, `by_active_status`

- **Class**
  - Attributes:
    - `name`
    - `department` (ForeignKey)
    - `supervisor` (ForeignKey to User)
    - `students` (ManyToMany)
    - `is_active`
    - `timestamps`
  - Filters: `by_department`, `by_supervisor`, `by_active_status`

### Students Models
- **Student**
  - Attributes:
    - `user` (OneToOne)
    - `student_id` (unique)
    - `department` (ForeignKey)
    - `current_class`
    - `enrollment_date`
    - `team_role` (ENUM: Leader, Member)
    - `status` (ENUM: Active, Graduated, Suspended)
    - `father_full_name`
    - `mother_full_name`
    - `father_email`
    - `mother_email`
    - `timestamps`
  - Filters: `by_department`, `by_class`, `by_team_role`, `by_status`

- **Team**
  - Attributes:
    - `name`
    - `description`
    - `department` (ForeignKey)
    - `leader` (ForeignKey to Student)
    - `members` (ManyToMany to Student)
    - `type` (ENUM: Project, StudyGroup, Club, EventCommittee, WorkshopGroup, SeminarTeam)
    - `is_active`
    - `max_members`
    - `timestamps`
  - Filters: `by_department`, `by_leader`, `by_member`, `by_active_status`, `by_type`

## Features App (MongoDB)

### Calendar Models
#### Main Models
  - **CalendarSettings**
      - Attributes:
        - `user` (OneToOneField to User)
        - `default_view` (ENUM: Day, Week, Month)
        - `timezone`
        - `notifications_enabled`
        - `created_at`
        - `updated_at`
      - Filters: `by_user`, `by_default_view`, `by_timezone`, `by_notifications_status`

  - **SharedCalendar**
    - Attributes:
      - `name`
      - `description`
      - `owner` (ForeignKey to User)
      - `members` (ManyToMany to User)
      - `is_active`
      - `timestamps`
      - Filters: `by_owner`, `by_member`, `by_active_status`

  - **Category** <!-- PERSPECTIVE -->
    - Attributes:
      - `name`
      - `description`
      - `color_code`
      - `is_active`
      - `timestamps`
    - Filters: `by_name`, `by_active_status`

#### Event Models
  - **Event**
    - Attributes:
      - `title`
      - `description`
      - `school` (ForeignKey)
      - `department` (ForeignKey, optional)
      - `organizer` (ForeignKey to User)
      - `type` (ENUM: Class, Exam, Meeting, Activity, Project, Holiday)
      - `category` (ENUM: Seminar, Workshop, StudySession, ClubActivity, ClassProject, ResearchProject, Presentation, Conference, OpenDay, GroupWork, IndividualWork, Competition, Exhibition, FieldTrip, CaseStudy, Thesis, Internship, Mentorship, PeerTutoring, SkillsWorkshop, TechnicalProject, CreativeProject, CommunityService, StartupProject, Innovation, Hackathon, DebateCompetition, AcademicContest)
      - `start_datetime`
      - `end_datetime`
      - `place`
      - `target_classes` (ManyToMany to Class)
      - `is_recurring`
      - `recurrence_pattern` (JSON, optional)
      - `reminder_settings` (JSON)
      - `timestamps`
    - Filters: `by_school`, `by_department`, `by_type`, `by_date_range`, `by_organizer`, `by_category`

#### Project Models
  - **Project**
    - Attributes:
      - `title`
      - `description`
      - `team` (ForeignKey)
      - `supervisor` (ForeignKey to User)
      - `category` (ENUM: Seminar, Workshop, StudySession, ClubActivity, ClassProject, ResearchProject, Presentation, Conference, OpenDay, GroupWork, IndividualWork, Competition, Exhibition, FieldTrip, CaseStudy, Thesis, Internship, Mentorship, PeerTutoring, SkillsWorkshop, TechnicalProject, CreativeProject, CommunityService, StartupProject, Innovation, Hackathon, DebateCompetition, AcademicContest)
      - `start_date`
      - `end_date`
      - `status` (ENUM: Planning, Active, OnHold, Completed, Archived)
      - `priority` (ENUM: Low, Medium, High)
      - `progress` (Integer)
      - `place`
      - `is_to_validate`
      - `validation_author`
      - `validation_date`
      - `timestamps`
    - Filters: `by_team`, `by_supervisor`, `by_status`, `by_priority`, `by_date_range`, `by_category`

  - **Task**
    - Attributes:
      - `title`
      - `description`
      - `project` (ForeignKey)
      - `assigned_to` (ForeignKey to User)
      - `due_date`
      - `status` (ENUM: Pending, InProgress, Completed)
      - `timestamps`
    - Filters: `by_project`, `by_assigned_user`, `by_status`, `by_due_date`, `by_date_range`    
    
### Forum Models
- **Forum**
  - Attributes:
    - `title`
    - `description`
    - `school` (ForeignKey)
    - `department` (ForeignKey, optional)
    - `moderator` (ForeignKey to User)
    - `status` (ENUM: Active, Archived, Hidden, ReadOnly)
    - `is_active`
    - `timestamps`
  - Filters: `by_school`, `by_department`, `by_moderator`, `by_active_status`, `by_status`

- **Topic**
  - Attributes:
    - `title`
    - `description`
    - `forum` (ForeignKey)
    - `created_by` (ForeignKey to User)
    - `is_pinned`
    - `is_locked`
    - `view_count`
    - `timestamps`
  - Filters: `by_forum`, `by_created_by`, `by_pinned_status`

- **Post**
  - Attributes:
    - `content`
    - `topic` (ForeignKey)
    - `author` (ForeignKey to User)
    - `parent_post` (ForeignKey to self, optional)
    <!-- - `is_edited`-- PERSPECTIVE -->
    - `timestamps`
  - Filters: `by_topic`, `by_author`, `by_date_range`

- **Comment**
  - Attributes:
    - `content`
    - `post` (ForeignKey to Post)
    - `author` (ForeignKey to User)
    - `parent_comment` (ForeignKey to self, optional)
    <!-- - `is_edited` -- PERSPECTIVE -->
    - `timestamps`
  - Filters: `by_post`, `by_author`, `by_date_range`  

### Library Models
- **LibraryCategory**
  - Attributes:
    - `name`
    - `description`
    - `manager` (ForeignKey to User)
    - `school` (ForeignKey)
    - `access_level` (ENUM: Public, Department, Private)
    - `target`
    - `is_active`
    - `timestamps`
  - Filters: `by_school`, `by_department`, `by_access_level`, `by_target`, `by_active_status`

- **Library**
  - Attributes:
    - `name`
    - `description`
    - `target`
    - `library_category` (ForeignKey)
    - `department` (ForeignKey, optional)
    - `access_level` (ENUM: Public, Department, Private)
    - `is_active`
    - `timestamps`
  - Filters: `by_school`, `by_department`, `by_access_level`, `by_target`, `by_active_status`, `by_library_category`

- **Document**
  - Attributes:
    - `title`
    - `description`
    - `library` (ForeignKey)
    - `file_path`
    - `file_size`
    - `file_type`
    - `uploaded_by` (ForeignKey to User)
    - `access_level` (ENUM: Public, Department, Private)
    - `download_count`
    - `timestamps`
  - Filters: `by_library`, `by_access_level`, `by_uploaded_by`, `by_file_type`

## Technical Implementation

### Security

- JWT-based authentication with refresh tokens
  - Uses JSON Web Tokens for secure user authentication
  - Includes refresh token mechanism to maintain user sessions
  - Provides stateless authentication solution

- Role-based access control (RBAC)
  - Controls user access based on assigned roles
  - Defines permissions for different user types
  - Ensures users can only access authorized resources

- Password hashing with bcrypt
  - Securely hashes user passwords before storage
  - Uses salt rounds for additional security
  - Prevents password exposure in case of data breaches

- CORS policies
  - Controls which domains can access the API
  - Prevents unauthorized cross-origin requests
  - Defines allowed HTTP methods and headers

- Input validation and sanitization
  - Validates all user inputs before processing
  - Removes potentially malicious content
  - Ensures data integrity and security

- XSS protection
  - Prevents cross-site scripting attacks
  - Sanitizes user-generated content
  - Escapes special characters in output

- SQL injection prevention
  - Uses parameterized queries
  - Validates and escapes database inputs
  - Prevents malicious SQL code execution

- Session management
  - Tracks and manages user sessions
  - Implements session timeout
  - Handles concurrent sessions
<!-- 
- Two-factor authentication (optional) ----- PERSPECTIVES
  - Adds extra layer of security
  - Uses time-based one-time passwords
  - Supports multiple 2FA methods 

- Rate limiting
  - Limits number of requests from single IP/user
  - Prevents brute force attacks
  - Controls API usage and server load
  -->

### Architecture
- RESTful API design
- API versioning
- Microservices architecture 
- Structured logging
<!-- - Database indexing and optimization-- PERSPECTIVE -->
<!-- - Redis caching-- PERSPECTIVE -->
<!-- - Background tasks with Celery -- PERSPECTIVE -->
<!-- - WebSocket support for real-time features -- PERSPECTIVE -->

<!-- 
### Monitoring- ----- PERSPECTIVES 
- Error tracking with Sentry 
- Performance monitoring 
- API usage analytics 
- System health checks 
- Automated backups 
- Load balancing 
- Scalability management -->

## Getting Started

1. System Setup
   - Configure database (PostgreSQL and MongoDB)
   - Set up environment variables
   - Install dependencies
   <!-- - Configure Redis and Celery - PERSPECTIVE -->

2. Initial Configuration
   - SuperAdmin account creation
   - Configure basic settings
   - Set up email service
   <!-- - Configure storage service- PERSPECTIVES -->
   <!-- - Set up monitoring tools- PERSPECTIVES -->

3. School Setup
   - Define plans 
   - Client contact SuperAdmin for access
   - SuperAdmin creates school, admin account and assigns subscription plan
   - Admin gets full access to platform features
   - Admin configures departments, settings and school-specific configurations

4. User Management
   - Admin adds managers
   - Admin or managers add students
   - Create teams
   - Configure permissions
   - Set up user roles

5. Content Setup
   - Configure library categories and structure
   - Set up forums and moderation
   - Create initial calendar events
   - Configure project templates
   - Set up document management

For support:
Contact Me 👉 Aziz Kane - [aziukane@gmail.com](mailto:aziukane@gmail.com)