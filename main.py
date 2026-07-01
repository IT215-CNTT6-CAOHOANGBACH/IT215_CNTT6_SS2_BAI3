from fastapi import FastAPI

app = FastAPI(
    title='App lấy sinh viên',
    description="Hay quá"
)

students = [
    {"id": 1, "name": "An", "status": "active"},
    {"id": 2, "name": "Binh", "status": "inactive"},
    {"id": 3, "name": "Cuong", "status": "active"},
    {"id": 4, "name": "Dung", "status": "pending"}
]

@app.get("/students/active", tags=['Students'],summary='Danh sách sv lấy dc actice')
def get_all_std():
    if not students:
        return{
            "message": "Không có sinh viên đang học",
            "data": []
        }
    active_std =[]
    for student in students:
        if student.get('status') == "active":
            active_std.append(student)
            
    return{
        "message": "Danh sách sinh viên đang học",
        'data':active_std
    }