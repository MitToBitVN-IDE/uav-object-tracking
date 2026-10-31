<p align="center">
  <h1 align="center">🛸 UAV Object Tracking Pipeline</h1>
  <p align="center">
    <b>Nghiên cứu & Xây dựng Thuật toán Theo dõi Đối tượng dựa trên Xử lý Ảnh cho Máy bay Không người lái (UAV)</b>
    <br />
    <i>Học viện Hàng không Việt Nam — Khoa Kỹ thuật Hàng không (Lớp 26AE202)</i>
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/YOLOv8-Real--Time_Detection-00FFFF?style=for-the-badge&logo=opencv&logoColor=black" />
  <img src="https://img.shields.io/badge/ByteTRACK-Multi--Object_Tracking-00599C?style=for-the-badge" />
  <img src="https://img.shields.io/badge/OpenCV-Computer_Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/badge/PyTorch-Deep_Learning-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />
</p>

---

## 📌 Tổng Quan Đề Tài (Overview)

Đề tài tập trung xây dựng quy trình khép kín (**pipeline**) xử lý thị giác máy tính cho UAV nhằm giải quyết các thách thức đặc thù của video ghi từ camera trên không:
- 🎯 **Đối tượng kích thước nhỏ** và khoảng cách xa.
- 💨 **Rung lắc camera** do động cơ và môi trường gió trên cao.
- 🙈 **Che khuất tạm thời (Occlusion)** và đối tượng thay đổi góc nhìn liên tục.

Hệ thống kết hợp mô hình phát hiện đối tượng thời gian thực **YOLOv8**, thuật toán gán danh tính **ByteTRACK** cùng module **Bù trừ chuyển động toàn cục (Global Motion Compensation - GMC)**.

---

## 📸 Kết Quả Thực Nghiệm & Demo (Experimental Results)

| Phát hiện & Gán ID Bàn Phím | Theo dõi Điện Thoại & Khung Xương Tay | Theo dõi Cử Chỉ Bàn Tay (MediaPipe) |
| :---: | :---: | :---: |
| ![Keyboard Tracking](https://via.placeholder.com/400x300.png?text=Demo+Keyboard+FPS+16) | ![Phone Tracking](https://via.placeholder.com/400x300.png?text=Demo+Phone+Hand+FPS+15) | ![Hand Tracking](https://via.placeholder.com/400x300.png?text=Demo+Hand+Gesture+FPS+22) |
| **FPS: 16** *(YOLOv8 + ByteTRACK)* | **FPS: 15** *(Multi-modal Detection)* | **FPS: 22** *(Gesture Landmarking)* |

> *(Ghi chú: Thay thế các link ảnh/GIF minh họa ở trên bằng đường dẫn tới hình ảnh/GIF thực tế trong thư mục `assets/` của bạn).*

---

## 🏗️ Kiến Trúc Hệ Thống (System Architecture)
