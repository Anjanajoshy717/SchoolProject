https://marthoma-school-backend.onrender.com/api/achievements/            

REQ
{
  "title":"titlee",
  "description": "This field is required.",
  "date": "2026-12-21",
  "phone_number":"2345678987"
}           
RES
{
  "id": 2,
  "title": "title",
  "description": "This field is required.",
  "date": "2026-12-21",
  "images": [],
  "created_at": "2025-08-20T15:15:35.193086Z"
}            

                 --- User Authentication ---


🔹POST /api/register/
{
  "first_name": "Farhana",
  "last_name": "Shareen",
  "email": "hanashnz2712@gmail.com",
  "phone_number": "1234512345",
  "password": "YourStrongPassword@123",
  "confirm_password": "YourStrongPassword@123" 
}
respo{
    "message": "User registered successfully. Please verify OTP sent to your email."
}

🔹POST /api/verify-otp/
{
  "phone_number": "1234512345",
  "otp": "947852"
}
respo{
    "message": "OTP verified successfully. You can now log in."
}

🔹POST /api/auth/login/
{
  "email": "hanashnz2712@gmail.com",
  "password": "YourStrongPassword@123"
}
respo
{
  "access": "your-access-token"
}

                                    -----EVENTS AND ACTIVITIES-----(meenakshi)
API Endpoints  
• GET /api/events/            - List all events (Authenticated) 
• POST /api/events/           - Create new event (Admin/Subadmin)  
• GET /api/events/{id}/       - Event detail (Authenticated)  
• PUT /api/events/{id}/       - Update event (Admin/Subadmin)  
• DELETE /api/events/{id}/    - Delete event (Admin/Subadmin) 


GET /api/events/ 

RES[ 
    { 
        "id": 5, 
        "title": "Annual Sports Day", 
        "description": "Track & Field events for all grades", 
        "image": null, 
        "location": "School Auditorium, Green Valley Public School, Trivandrum", 
        "event_date": "2025-11-29", 
        "registration_link": "https://greenvalleyschool.com/events/register/science-exhibition
2025", 
        "created_at": "2025-07-28T14:33:52.362902Z" 
    }, 
… 
] 


POST   /api/events/ 

Body(form-data) 
                     
title                 Annual Sports Day 
description           Track & Field events for all grades  
image                 Select file 
location              School Auditorium, Green Valley Public School, Trivandrum 
event_date            2025-11-25 
registration_link     https://greenvalleyschool.com/events/register/science-exhibition-2025 
 

RES{ 
    "id": 5, 
    "title": "Annual Sports Day", 
    "description": "Track & Field events for all grades", 
    "image": null, 
    "location": "School Auditorium, Green Valley Public School, Trivandrum", 
    "event_date": "2025-11-25", 
    "registration_link": "https://greenvalleyschool.com/events/register/science-exhibition-2025", 
    "created_at": "2025-07-28T14:33:52.362902Z" 
} 


GET     /api/events/{id}/ 
 
RES{ 
    "id": 5, 
    "title": "Annual Sports Day", 
    "description": "Track & Field events for all grades", 
    "image": null, 
    "location": "School Auditorium, Green Valley Public School, Trivandrum", 
    "event_date": "2025-11-25", 
    "registration_link": "https://greenvalleyschool.com/events/register/science-exhibition-2025", 
    "created_at": "2025-07-28T14:33:52.362902Z" 
} 
PUT      /api/events/{id}/  

Body(form-data) 
REQ

title              Annual Sports Day 
description        Track & Field events for all grades  
image              Select file 
location           School Auditorium, Green Valley Public School, Trivandrum 
event_date         2025-11-28 
registration_link  https://greenvalleyschool.com/events/register/science-exhibition-  2025 

RES{ 
    "id": 5, 
    "title": "Annual Sports Day", 
    "description": "Track & Field events for all grades", 
    "image": null, 
    "location": "School Auditorium, Green Valley Public School, Trivandrum", 
    "event_date": "2025-11-28", 
    "registration_link": "https://greenvalleyschool.com/events/register/science-exhibition2025", 
    "created_at": "2025-07-28T14:33:52.362902Z" 
  } 

PATCH/api/events/{id}/  

REQ
Body(form-data) 

event_date    2025-11-28 

RES{ 
    "id": 5, 
    "title": "Annual Sports Day", 
    "description": "Track & Field events for all grades", 
    "image": null, 
    "location": "School Auditorium, Green Valley Public School, Trivandrum", 
    "event_date": "2025-11-28", 
    "registration_link": "https://greenvalleyschool.com/events/register/science-exhibition2025", 
    "created_at": "2025-07-28T14:33:52.362902Z" 
} 

DELETE /api/events/{id}/ 


User Roles 
• Admin: Full CRUD access 
• Subadmin: Full CRUD access


                            ------- 📘 Teacher ------(shabeeb)

🔹 GET /api/teachers/
Description: Retrieve a list of all teachers.

Query Parameters (Optional):

search: Search by first_name, last_name, email, subject

ordering: Order by first_name, last_name, joining_date
Example: /api/teachers/?ordering=last_name

Response:


[
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "phone": "1234567890",
    "date_of_birth": "1990-01-01",
    "gender": "M",
    "address": "123 Main St",
    "qualification": "MSc",
    "subject": "Mathematics",
    "joining_date": "2025-08-01",
    "profile_picture": "/media/teachers/profile_pics/john.jpg",
    "is_active": true
  },
  ...
]
Permissions:

Public: ✅ Read

Admin: ✅ Read & Write

✅ POST /api/teachers/
Description: Create a new teacher entry (Admin only).

Request Body:

{
    
    "name": "alan",
    "email_id": "alice12@example.com",
    "contact_number": "+919874563210",
    "date_of_birth": "1985-05-10",
    "experience": 0,
    "degree": "mca",
    "college_or_uni": "calicut",
    "yearofpass": "2022",
    "category": "deceased",
    "subject": "Hindi"
    "joining_date":"2009-05-10"
}
Response: 201 Created


  {
    "id": 2,
    "name": "alan",
    "email_id": "alice12@example.com",
    "contact_number": "+919874563210",
    "date_of_birth": "1985-05-10",
    "date_of_death": null,
    "experience": 0,
    "degree": "mca",
    "college_or_uni": "calicut",
    "yearofpass": 2022,
    "category": "deceased",
    "subject": "Hindi",
    "joining_date": "2025-08-19",
    "profile_picture": null
    "joining_date":"2009-05-10"
}

Validations:

Email must be unique.

joining_date is read-only and auto-assigned.

Permissions:

Admin only

🔹 GET /api/teachers/<id>/
Description: Retrieve a specific teacher's details by ID.

Response:


{
  "id": 1,
  "first_name": "John",
  ...
}
Permissions:

Public: ✅ Read

🔹 PUT /api/teachers/<id>/
Description: Update an existing teacher’s record (Admin only).

Request Body: (Full object update)


{
  "first_name": "Updated",
  ...
}
Permissions:

Admin only

🔹 PATCH /api/teachers/<id>/
Description: Partially update a teacher's details (Admin only).

Request Body: (Only fields to update)


{
  "phone": "1112223333"
}
Permissions:

Admin only

🔹 DELETE /api/teachers/<id>/
Description: Delete a teacher (Admin only).

Permissions:

Admin only

🔐 Permissions
SAFE_METHODS (GET, HEAD, OPTIONS): Public access

POST, PUT, PATCH, DELETE: Only accessible to admin (is_staff=True)

                                       ----------Learning(ajil)-----------

                      
 This document describes the REST API endpoints for managing school divisions, classes, subjects,
 sections, and syllabus. All POST, PUT, PATCH, DELETE requests require is
 staff = True (Admin only). GET requests are public (read-only).
 
1. Classes


  ✅ GET     /api/classes/                    – List all classes
  ✅ GET     /api/classes/?division=LP        – Filter by division (LP or HS)
  ✅ GET     /api/classes/{id}/               – Retrieve a class
  ✅ PATCH   /classes/{id}/                   – Update a class (Admin only)
  ✅ DELETE  /api/classes/{id}/               – Delete a class (Admin only)
  ✅ POST    /api/classes/                    – Create a class (Admin only)

  REQ{
      "name": "Class 8",
      "order": 8,
      "division":"HS"
  }
  RES{
      "id": 3,
      "subjects": [],
      "division": "HS",
      "name": "Class 8",
      "order": 8,
      "image": null
  }

2. Subjects
 
  ✅ GET    /api/subjects/                     – List all subjects
  • GET     /api/subjects/?class
  id={class
  id}– List subjects in a class
  ✅ GET   /api/subjects/{id}/                 – Retrieve a subject
  ✅ POST  /api/subjects/                      – Create a subject (Admin only)
  ✅ PUT   /api/subjects/{id}/                 – Edit
  ✅ PATCH /subjects/{id}/                     – Update subject
  ✅ DELETE /api/subjects/{id}/                – Delete subject

  REQ{
        "school_class": 3,
        "name": "Math",
        "description": "Mathematics for Class 3"
      }
  RES{
        "id": 5,
        "school_class": 3,
        "name": "Math",
        "description": "Mathematics for Class 3",
        "image": null,
        "sections": []
      }

3. Sections (Units)

  ✅ GET /api/sections/
  • GET /api/sections/?subject
  ✅ GET /api/sections/{id}/
  id={subject
  ✅ POST /api/sections/ (Admin only)
  id}
  ✅ PUT /api/sections/{id}/, PATCH /sections/{id}/
  ✅ DELETE /api/sections/{id}/
  REQ{
        "subject": 1,
        "title": "Unit 2: Addition",
        "content": "Basic addition operations",
        "order": 2
      }
  RES{
        "id": 1,
        "syllabus": [],
        "title": "Unit 2: Addition",
        "content": "Basic addition operations",
        "order": 2,
        "image": null,
        "subject": 1
      }
 
4. Syllabus (Chapters)

  ✅ GET       /api/syllabus/
  • GET        /api/syllabus/?sectionid={sectionid}
  ✅ GET      /api/syllabus/{id}/
  ✅ POST     /api/syllabus/ (Admin only)
  ✅ PUT      /api/syllabus/{id}/, PATCH /syllabus/{id}/
  ✅ DELETE   /api/syllabus/{id}/
  REQ{
        "section": 11,
        "chapter_title": "Chapter 1: Counting",
        "description": "Counting numbers 1 50",
        "order": 1
    }
  RES{
        "id": 21,
        "section": 11,
        "chapter_title": "Chapter 1: Counting",
        "description": "Counting numbers 1 50",
        "order": 1,
        "image": null
      }


                                         Advertisement(ajil)



Advertisement Endpoints

 
 GET /api/ads/  -List All Advertisements
 
 RES {
    [
      "id": 1,
      "title": "Summer Mega Sale",
      "image": "/media/ads/sale.jpg",
      "description": "Up to 50% off on books and supplies",
      "link": "https://example.com/sale",
      "start_date": "2025-08-01",
      "end_date": "2025-08-15",
      "is_active": true,
      "created_by": 2,
      "created_at": "2025-08-05T10:30:00Z"
      —
 ]
 }


 POST /api/ads/                -Create Advertisement
 
REQ {
      "title": "Summer Mega Sale",
      "description": "Big discounts on supplies",
      "link": "https://example.com/sale",
      "start_date": "2025-08-01",
      "end_date": "2025-08-15",
      1
      "is_active": true,
      "image": "<file upload>"
    }
RES {
      "id": 2,
      "title": "Summer Mega Sale",
      "image": "/media/ads/sale.jpg",
      "description": "Big discounts on supplies",
      "link": "https://example.com/sale",
      "start_date": "2025-08-01",
      "end_date": "2025-08-15",
      "is_active": true,
      "created_by": 1,
      "created_at": "2025-08-05T11:15:30Z"
      —
    } 
GET   /api/ads/{id}/            -Retrieve Advertisement by ID

RES {
      "id": 2,
      "title": "Summer Mega Sale",
      "image": "/media/ads/sale.jpg",
      "description": "Big discounts on supplies",
      "link": "https://example.com/sale",
      "start_date": "2025-08-01",
      "end_date": "2025-08-15",
      "is_active": true,
      "created_by": 1,
      "created_at": "2025-08-05T11:15:30Z"
      —
    }
 
PUT /api/ads/{id}/               -Update Advertisement


REQ{
 
    "title": "Updated Mega Sale",
    "description": "Now 70% off!",
    "is_active": false
    Response Example:
    "id": 2,
    "title": "Updated Mega Sale",
    "image": "/media/ads/sale.jpg",
    "description": "Now 70% off!",
    "link": "https://example.com/sale",
    "start_date": "2025-08-01",
    "end_date": "2025-08-15",
    "is_active": false,
    "created_by": 1,
    "created_at": "2025-08-05T11:15:30Z"
    —
 }
 
 DELETE /api/ads/{id}/             -Delete Advertisement


 2 Error Responses
 • 401 Unauthorized– Missing or invalid token
 • 403 Forbidden– User not admin when modifying data
 • 400 Bad Request– Invalid or missing fields in request
 • 404 Not Found– Advertisement does not exist


                                               Enquire -(eben)
                         
 POST /api/enquiry/  
 
REQ{
    "name": "Eben Lal",
    "email": "eben@example.com",
    "phone_number": "9876543210",
    "message": "I would like to know more about your services."
}

 

RES{
    "message": "Enquiry submitted successfully."
}


terminal response : 

Subject: New Enquiry from Eben Lal
From: noreply@example.com
To: admin@example.com
Date: Wed, 06 Aug 2025 11:47:15 -0000
Message-ID: <175448083561.394944.605756573236375208@msi-Modern-14-C12MO>


            Name: Eben Lal
            Email: eben@example.com
            Phone Number: 9876543210
            Message: I would like to know more about your services.


            
                                                 review(anwin)


GET  /api/school-reviews/

POST  /api/school-reviews/   -Add new review

{
  "school": 1  "rating": 5,
  "comment": "Amazing school with great teachers!"
}


                                                 NEWS SECTION (nandhidha)



GET   /api/news/       - List All News 

RES [ 
   { 
    "id": 1, 
    "title": "Example News", 
    "content": "This is the news content.", 
    "image": "http://127.0.0.1:8000/media/news/image.jpg", 
    "published_at": "2025-08-06T10:45:00Z" 
    }, 
... 
    ] 


POST   /api/news/   - Create News(admin/subadmin only)   
Content-Type: multipart/form-data 

Key                  Value                   Type

title                My first news title     Text
content              This is the content.    Text
image                (upload image file)     File 
 
RES{ 
    "id": 3, 
    "title": "My first news title", 
    "content": "This is the content.", 
    "image": "http://127.0.0.1:8000/media/news/image.jpg", 
    "published_at": "2025-08-06T11:00:00Z" 
} 
 
GET    /api/news/<id>/   -Retrieve Single News

 
RES{ 
    "id": 3, 
    "title": "My first news title", 
    "content": "This is the content.", 
    "image": "http://127.0.0.1:8000/media/news/image.jpg", 
    "published_at": "2025-08-06T11:00:00Z" 
} 

PUT/PATCH   /api/news/<id>/    - Update News 

Body (form-data): 
Key              Value                     Type

title            Updated news title        Text 
content          Updated content           Text
image            (upload new image)        File (optional) 
 
RES{ 
"id": 3, 
"title": "Updated news title", 
"content": "Updated content", 
"image": "http://127.0.0.1:8000/media/news/newimage.jpg", 
"published_at": "2025-08-06T11:00:00Z" 
} 


DELETE   /api/news/<id>/      -Delete News 

                                ---------SPORTS(meenakshi)--------

Features 
• Add/Edit/Delete/View school events. 
• Only Admin and Subadmin can modify events 
• RESTful API design, Postman testable 
 
API Endpoints  
• GET /api/sports/  
• POST /api/sports/  
• GET /api/sports/{id}/  
• PUT /api/sports/{id}/  
• DELETE /api/sports/{id}/  
 
• GET /api/sports-images/  
• POST /api/ sports-images /  
• GET /api/ sports-images /{id}/  
• PUT /api/ sports-images /{id}/  
• DELETE /api/ sports-images /{id}/  
 
• GET /api/ sports-winners/  
• POST /api/ sports-winners/  
• GET /api/ sports-winners/{id}/  
• PUT /api/ sports-winners/{id}/  
• DELETE /api/ sports-winners/{id}/  
 

✅GET /api/sports/  
RES[ 
   { 
        "id": 8, 
        "title": "School Level Volleyball", 
        "description": "A competitive volleyball tournament...", 
        "created_at": "2025-08-06T10:46:12.780921Z", 
        "images": [], 
        "winners": [ 
            { 
                "id": 1, 
                "event": 8, 
                "name": "Rahul K", 
                "photo": "http://127.0.0.1:8000/media/abc", 
                "student_class": "10A", 
                "position": "1st" 
            } 
        ]
          }
… 
  ] 
✅POST  /api/sports/  
 
REQ{ 
    "title": "Annual Sports Day", 
    "description": "A day full of fun and competition!" 
  } 
 
RES{ 
    "id": 19, 
    "title": "Annual Sports Day", 
    "description": "A day full of fun and competition!", 
    "created_at": "2025-08-06T14:16:42.458515Z", 
    "images": [], 
    "winners": [] 
  } 
✅GET /api/events/{id}/ 

RES{ 
    "id": 19, 
    "title": "Annual Sports Day", 
    "description": "A day full of fun and competition!", 
    "created_at": "2025-08-06T14:16:42.458515Z", 
    "images": [], 
    "winners": [] 
} 
✅PUT(PATCH)    /api/sports/{id}/  
 
REQ{ 
  "title": "Sports Day Celebration", 
  "description": "A day full of fun and competition!!" 
} 

RES{ 
    "id": 20, 
    "title": "Sports Day Celebration", 
    "description": "A day full of fun and competition!!", 
    "created_at": "2025-08-06T14:26:26.517071Z", 
    "images": [], 
    "winners": [] 
} 
✅DELETE /api/sports/{id}/   


✅GET /api/sports-images/  

RES[ 
    { 
        "id": 1, 
        "event": 17, 
        "image": "http://127.0.0.1:8000/media/sports_images/WhatsApp_Image_2025-0805_at_9.13.02_PM.jpeg" 
    }, 
    { 
        "id": 2, 
        "event": 17, 
        "image": "http://127.0.0.1:8000/media/sports_images/WhatsApp_Image_2025-0805_at_9_qD1mxCx.13.02_PM.jpeg" 
    }, 
] 


POST /api/sports-images/ 

Body(form-data) 

REQ{ 
    "event": 1, 
    "image": "http://127.0.0.1:8000/media/sport_images/winner1.jpg" 
   } 
RES { 
    "id": 5, 
    "event": 1, 
    "image": "http://127.0.0.1:8000/media/sport_images/winner1.jpg" 
    } 

GET     /api/sports-images/{id}/ 

RES { 
"id": 6, 
"event": 21, 
"image": "http://127.0.0.1:8000/media/sports_images/WhatsApp_Image_2025-08
05_at_9_G9ThkTB.13.03_PM.jpeg" 
} 

PUT(PATCH)      /api/ sports-images /{id}/  

Body(form-data) 
REQ{ 
"event": event_id(21), 
"image": http://127.0.0.1:8000/media/sports_images/WhatsApp_Image_2025-08
04_at_9.00.43_PM.jpeg 
} 
RES{ 
    "id": 6, 
    "event": 21, 
    "image": "http://127.0.0.1:8000/media/sports_images/WhatsApp_Image_2025-08
04_at_9.00.43_PM.jpeg" 
}

DELETE  /api/sports-images/{id}/  

GET     /api/sports-winners/  

RES [ 
    { 
        "id": 1, 
        "event": 8, 
        "name": "Rahul K", 
        "photo": "http://127.0.0.1:8000/media/abc", 
        "student_class": "10A", 
        "position": "1st" 
    }, 
    { 
        "id": 2, 
        "event": 8, 
        "name": "Vikram S", 
        "photo": "http://127.0.0.1:8000/media/abc", 
        "student_class": "10B", 
        "position": "2nd" 
    }, 
] 
POST      /api/sports-winners/  

Body(form-data) 
REQ{ 
    "event": event_id(21) 
    "name": "Aravind S", 
    "photo": "http://127.0.0.1:8000/media/winner_photos/SamplePhoto_11.jpg", 
    "student_class": "10-A", 
    "position": "1st" 
} 

RES{ 
    "id": 13, 
    "event": 21, 
    "name": "Aravind S", 
    "photo": "http://127.0.0.1:8000/media/winner_photos/SamplePhoto_11.jpg", 
    "student_class": "10-A", 
    "position": "1st" 
} 

GET    /api/sports-winners/{id}/  

RES{ 
    "id": 2, 
    "event": 8, 
    "name": "Vikram S", 
    "photo": "http://127.0.0.1:8000/media/abc", 
    "student_class": "10B", 
    "position": "2nd" 
  } 
 
PUT(PATCH)   /api/sports-winners/{id}/  

Body(form-data) 
REQ{ 
    "event": 21, 
    "name": "Aravind S", 
    "photo": "http://127.0.0.1:8000/media/winner_photos/SamplePhoto_11_SGZUFUW.jpg", 
    "student_class": "10-B", 
    "position": "1st" 
} 
RES{ 
    "id": 2, 
    "event": 21, 
    "name": "Aravind S", 
    "photo": "http://127.0.0.1:8000/media/winner_photos/SamplePhoto_11_SGZUFUW.jpg", 
    "student_class": "10-B", 
    "position": "1st" 
} 

DELETE     /api/sports-winners/{id}/   
 


User Roles 
• Admin: Full CRUD access 
• Subadmin: Full CRUD access 
• Others: Read-only 


                                               WeProvide API (aiswarya)


POST   /api/weprovide/   
Request Body (Form data): 
           name: martin 
            image: upload 
           description: USS and NMMS Scholarships 
Response: 
            { 
           "id": 3, 
            "name": "martin", 
            "image": "http://127.0.0.1:8000/media/we_provide/OIP.jpeg", 
            "description": "USS and NMMS Scholarships" 
            } 

▪ /api/weprovide/id/       -Detail, Update, or Delete 
▪ Methods: GET, PUT, PATCH, DELETE 

▪ /api/facility/             -Facility API 
▪ Methods: GET, POST 
Formdata: 
            name: Helen 
            image: uploaded 
Response: 
                { 
             "id": 2, 
              "name": "Helen", 
               "image": "http://127.0.0.1:8000/media/facility_images/OIP_2.jpeg" 
              } 

▪ /api/facility/id/      -Detail, Update, or Delete 
▪ Methods: GET, PUT, PATCH, DELETE 

                           ABOUTUS(jayakrishnan)


 1.Information submission
 Endpoint: /api/about-us/post/ 
Method: POST
 Body (form-data):
 Key                    Type           Value

 title                  Text           About Us 
 description            Text          104 years is a long period for a school.
 image                  File          classroom.jpg
 
RES {

      "status": "success",
      "message": "Information added",
      "data": {
      "id": 3,
      "title": "About Us",
      "image": "/media/AboutUs%20Images/classroom_j3EGbjD.jpg",
      "description": "Marthoma High School, established in 1921, has
      completed 104 years in the year 2025. 104 years is a long period for a
      school."
   }
   }
 

GET /api/about-us/view/   -Retrieve Information

RES {
      "status": "success",
      "message": "Fetched About Us",
      "data": {
      "id": 3,
      "title": "About Us",
      "image": "/media/AboutUs%20Images/classroom_j3EGbjD.jpg",
      "description": "Marthoma High School, established in 1921, has
      completed 104 years in the year 2025. 104 years is a long period for a
      school."
 }
 }
 
 PUT /api/about-us/view/    -UpdateInformation

 Body (form-data):

 Key                Type          Value

 title              Text           About Us
 description        Text           Marthoma High School, established in 1921,
 image              File           classroom.jpg

 RES {
      
    "status": "success",
    "message": "About Us info updated successfully!",
    "data": {
    "id": 3,
    "title": "About Us",
    "image": "/media/AboutUs%20Images/classroom_QIbJWRg.jpg",
    "description": "Marthoma High School, established in 1921,"
 }
 }
 

DELETE /api/about-us/view/   -Delete About Us


RES {

 "status": "success",
 "message": "About Us all info deleted!"
 }

                        ----------career(prajin)------------


✅	GET / api/jobs/?search=React Developer     -Search jobs
✅ Delete /api/jobs/1/                        - delete job
✅ POST   /api/jobs/                          - create jobs

REQ {
      "title": "React Developer",
      "description": "Looking for a React developer with 2+ years experience.",
      "location": "Remote",
      "salary": "50000",
      "deadline": "2025-09-01",
      "experience": "2+ years",
      "requirements": "Proficient in React, JavaScript, and REST APIs",
      "last_date": "2025-08-31"
    }
RES {
      "id": 2,
      "title": "React Developer",
      "location": "Remote",
      "experience": "2+ years",
      "requirements": "Proficient in React, JavaScript, and REST APIs",
      "posted_at": "2025-08-08T05:31:24.377158Z",
      "last_date": "2025-08-31",
      "is_active": true
    }
 
✅Patch /api/jobs/1/          -Update jobs

REQ {
      "title": "python Developer"
    }
RES {
    "id": 1,
    "title": "python Developer",
    "location": "Remote",
    "experience": "2+ years",
    "requirements": "Proficient in React, JavaScript, and REST APIs",
    "posted_at": "2025-08-14T21:14:31.187594Z",
    "last_date": "2025-08-31",
    "is_active": true
  }


✅ GET   /api/jobs/           -List jobs
RES:[
      {
          "id": 2,
          "title": "React Developer",
          "location": "Remote",
          "experience": "2+ years",
          "requirements": "Proficient in React, JavaScript, and REST APIs",
          "posted_at": "2025-08-08T05:31:24.377158Z",
          "last_date": "2025-08-31",
          "is_active": true
      }
    ]


•	Patch /api/jobs/1/   - Apply jobs
REQ

    Key	                 Value	             Type

    job	                 1	                 Text
    full_name	           John Doe	           Text
    email	               john@example.com    Text
    phone_number	       9876543210	         Text
    years_of_experience	 2	                 Text
    qualification	       B.Tech	             Text
    current_location	   Kochi	             Text
    resume	             choose PDF file	   File

RES{
    "id": 1,
    "job": 1,
    "full_name": "John Doe",
    "email": "john@example.com",
    "phone_number": "9876543210",
    "years_of_experience": "2",
    "qualification": "B.Tech",
    "current_location": "Kochi",
    "resume": "/media/resumes/resume.pdf",
    "applied_at": "2025-08-07T10:30:12Z"
  }


 


