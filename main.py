# Phần 1:BÁo cáo phân tích:
# 1.Input của bài toán là gì?: danh sách các đối tượng sinh viên, mỗi đối tượng gồm: id, name, class, và stutus.

# 2.Output mong muốn là gì?: Một đối tượng Json chứa message và data (danh sách các sinh viên có status == "active").

# 3.Điều kiện nào dùng để xác định sinh viên đang học?: Dựa vào trường status của sinh viên có giá trị là "active".


# 4.Các bước xử lý API GET /students/active.: 
# GET /students-active 

# Phần 2: Triển khai code:
from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "An", "status": "active"},
    {"id": 2, "name": "Binh", "status": "inactive"},
    {"id": 3, "name": "Cuong", "status": "active"},
    {"id": 4, "name": "Dung", "status": "pending"}
]

@app.get("/students-active")
def get_active_students():
    active_list = [s for s in students if s["status"] == "active"]

    if not active_list:
        return {
            "message": "Không có sinh viên đang học",
            "data": []
        }
    
    return {
        "message": "Danh sách sinh viên đang học",
        "data": active_list
    }