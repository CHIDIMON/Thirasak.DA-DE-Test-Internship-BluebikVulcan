# Assessment Bluebik Vulcan (Data Analyst & Data Engineer)


Repository นี้รวบรวมคำตอบสำหรับแบบทดสอบตำแหน่ง **Data Analyst** และ **Data Engineer** โดยแบ่งแยกโฟลเดอร์ตามโจทย์ที่ได้รับมอบหมายครับ## โครงสร้างไฟล์ (Repository Structure)```text

```

├── requirements.txt            # รายชื่อ Library ที่ต้องติดตั้ง (Pandas)

├── DA_Total_Price/             # [ส่วนของ Data Analyst]

│   ├── solution.sql            # *** ไฟล์คำตอบหลัก (SQL Query)

│   ├── database.sql            # (Test Data) ข้อมูลจำลองสำหรับทดสอบ

│   └── mock_data_test.py       # (Test Script) ไฟล์สำหรับรันตรวจสอบผลลัพธ์ SQL

└── DE_Data_Transformation/     # [ส่วนของ Data Engineer]

    └── main.py                 # *** ไฟล์คำตอบหลัก (Python Pandas Logic)
```
SETUP
```
git clone https://github.com/CHIDIMON/Thirasak.DA-DE-Test-Internship-BluebikVulcan.git
cd Thirasak.DA-DE-Test-Internship-BluebikVulcan
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python ./DE_Data_Transformation/main.py
python DA_Total_Price/mock_data_test.py
```
