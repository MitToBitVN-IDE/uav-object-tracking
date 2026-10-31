UAV Object Tracking Pipeline (YOLOv8 + ByteTRACK + GMC)Đề tài Nghiên cứu Khoa học Sinh viênChủ đề: Xây dựng thuật toán theo dõi đối tượng dựa trên xử lý ảnh cho máy bay không người lái (UAV)Đơn vị: Khoa Kỹ thuật Hàng không – Học viện Hàng không Việt Nam (VAA)Lớp: 26AE202📌 Tổng quan dự án (Overview)Video quay từ máy bay không người lái (UAV) thường đối mặt với các thách thức kỹ thuật phức tạp như:Đối tượng cần theo dõi có kích thước nhỏ (small objects).Camera bị rung lắc liên tục do chuyển động 3D của thiết bị bay.Đối tượng bị che khuất tạm thời (occlusion) hoặc biến dạng góc nhìn.Dự án này xây dựng một pipeline xử lý ảnh khép kín, tích hợp mô hình phát hiện đối tượng thời gian thực YOLOv8, thuật toán gán định danh đa đối tượng ByteTRACK và module bù trừ chuyển động toàn cục GMC (Global Motion Compensation) nhằm duy trì ID đối tượng chính xác và ổn định.🏗️ Kiến trúc hệ thống (System Architecture)[ Input UAV Video Frame ]
           │
           ▼
[ Global Motion Compensation (GMC) ] ── (Khắc phục rung lắc camera)
           │
           ▼
[ Object Detection (YOLOv8) ] ──────── (Phát hiện & Bounding Box)
           │
           ▼
[ Data Association (ByteTRACK) ] ───── (Lọc Kalman + Gán ID)
           │
           ▼
[ Output Frame with ID Tracking ]
🛠️ Công nghệ & Thuật toán sử dụngLanguage: Python 3.8+Computer Vision Frameworks: OpenCV, PyTorch, Ultralytics YOLOv8Tracking Algorithm: ByteTRACK (Tối ưu hóa gán ID cho cả bounding box điểm số thấp)Datasets: VisDrone-MOT, UAVDT (Tập dữ liệu chuẩn mực quốc tế cho UAV)Hardware Integration Target: Raspberry Pi 3 / Jetson Nano + Cam Gimbal 2 trục in 3D🚀 Hướng dẫn cài đặt & Chạy mô phỏng (Getting Started)1. Clone Repositorygit clone https://github.com/MitToBitVN-IDE/uav-object-tracking.git
cd uav-object-tracking
2. Cài đặt môi trườngpip install -r requirements.txt
3. Chạy thuật toán theo dõi trên Video/Webcampython track.py --source video.mp4 --weights yolov8n.pt --tracker bytetrack.yaml
📊 Kết quả thực nghiệm (Experimental Results)Độ ổn định FPS: Đạt trung bình 15 - 22 FPS trên thiết bị thử nghiệm cơ bản.Khả năng duy trì ID: Giảm thiểu hiện tượng nhảy ID (ID switches) khi đối tượng di chuyển qua vùng bị che khuất tạm thời.👥 Thành viên thực hiện (Team Members)Họ và tênVai tròLớpĐơn vịNgô Quang TrưởngChủ nhiệm đề tài (Leader)26AE202Khoa Kỹ thuật Hàng khôngNguyễn Minh HiếuThành viên nghiên cứu26AE202Khoa Kỹ thuật Hàng khôngPhạm Nguyễn Thanh NgọcThành viên nghiên cứu26AE202Khoa Kỹ thuật Hàng khôngPhạm Anh TuấnThành viên nghiên cứu26AE202Khoa Kỹ thuật Hàng khôngLê Thị Hoàng VânThành viên nghiên cứu26AE202Khoa Kỹ thuật Hàng không📜 LicenseDự án được phân phối dưới giấy phép MIT License.
