
# 🇱🇰 LankaWork — Sri Lanka Service Marketplace  
A full-stack platform built to connect **users** and **skilled workers** such as DJs, carpenters, decorators, electricians, mechanics, and many more.  
The system also includes an **Event Bundle Booking Module** for organizing birthdays, weddings, and parties in one place.

---

## 🚀 Features

### 👤 User Features
- Create job posts  
- Search & filter workers  
- Book workers for normal jobs  
- Create event bundles (DJ + Decorations + Cake Maker etc.)  
- Track job & event status  
- Rate workers  

### 🛠️ Worker Features
- Register / login  
- Create skill profile (ex: DJ, carpenter, painter)  
- Accept / reject user job requests  
- Manage availability calendar  
- Receive event booking requests  

### 🛡️ Admin Features
- Approve/verify workers  
- Manage users and workers  
- Monitor job posts  
- Monitor event bookings  
- Handle reports  

---

## 🎉 Event Bundle Booking Module
Users can plan parties & events from one place.  
Supported services:

- DJ / Music  
- Photography / Videography  
- Cake Maker  
- Catering  
- Decorations / Flowers  
- Lighting / Sound  
- Stage Setup  
- Party Games / Magician  
- Event Coordinator  

Each service sends separate requests to workers, who accept or reject the job.

---

## 🧠 Light AI Module (Free)
Non-paid lightweight AI features:
- Auto-generate job descriptions  
- Event suggestions  
- Smart worker filtering  

*(No paid AI API required.)*

---

## 🏗️ System Architecture

### Backend — **FastAPI**
- REST API  
- JWT Authentication  
- Role-based access (User, Worker, Admin)  
- Modular routers  
- Event workflows  

### Database — **MySQL**
- Users  
- Workers  
- Jobs  
- Bookings  
- Events  
- Event services  
- Event bookings  

### Frontend — **HTML, CSS, JavaScript**
- Responsive UI  
- Worker filter UI  
- Dashboard pages  
- Event planner interface  

---

## 🗄️ Database Structure (Main Tables)

### `users`
| id | name | email | phone | role | password |
|----|------|--------|--------|-------|----------|

### `workers`
| id | user_id | skill_category | price | location | experience |

### `jobs`
| id | user_id | title | description | status |

### `events`
| id | user_id | type | date | location | total_budget | status |

### `event_services`
| id | event_id | category |

### `event_bookings`
| id | event_service_id | worker_id | status |

---

## 📡 API Endpoints (Short Overview)

### **Auth**
```
POST /auth/register
POST /auth/login
```

### **Users**
```
POST /jobs
GET /jobs
GET /workers?category=x&location=x&price_min=x
```

### **Events**
```
POST /events
POST /events/{id}/services
POST /events/{event_service_id}/book/{worker_id}
```

### **Workers**
```
GET /worker/jobs
PUT /worker/job/{id}/status
```

### **Admin**
```
GET /admin/users
GET /admin/workers
PUT /admin/worker/{id}/approve
```

---

## 🧱 Tech Stack
| Layer | Technology |
|-------|------------|
| Backend | Python+FastAPI |
| Frontend | HTML, CSS, JS |
| Database | MySQL |
| Auth | JWT |
| Architecture | REST API, MVC-ish |

---

## 📦 Installation

### **1. Clone Repo**
```
git clone https://github.com/yourusername/lankawork.git
cd lankawork
```

### **2. Backend Setup**
```
pip install -r requirements.txt
uvicorn main:app --reload
```

### **3. Database Setup**
Import MySQL schema file:
```
mysql -u root -p < database.sql
```

### **4. Frontend**
Open `/frontend/index.html` in browser  
or  
serve with any static server.

---

## 📌 Roadmap
- Mobile App (Flutter or React Native)  
- AI Worker Recommendation System  
- Online Payments (Stripe / PayHere / Genie)  
- Worker Verification System (NIC / License)  
- Push Notifications  

---

## 🏆 Author
**Randidu Damsith**  
Full-Stack Developer

---

## ⭐ License
This project is open-source and free to use.

