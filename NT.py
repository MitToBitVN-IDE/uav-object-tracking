import cv2
import mediapipe as mp
# Import trực tiếp submodule để tránh lỗi trên Python 3.11
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as mp_drawing
import time

try:
    from ultralytics import YOLO
except ModuleNotFoundError:
    YOLO = None


class HandDetector:
    def __init__(self, mode=False, max_hands=2, detection_con=0.5, track_con=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_con = detection_con
        self.track_con = track_con

        # Khởi tạo giải pháp MediaPipe Hands
        self.mp_hands = mp_hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=self.detection_con,
            min_tracking_confidence=self.track_con
        )
        self.mp_draw = mp_drawing

    def find_hands(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)

        if self.results.multi_hand_landmarks:
            for hand_lms in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(
                        img, 
                        hand_lms, 
                        self.mp_hands.HAND_CONNECTIONS,
                        self.mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=4),
                        self.mp_draw.DrawingSpec(color=(0, 0, 255), thickness=2)
                    )
        return img

    def find_positions(self, img, hand_no=0):
        lm_list = []
        if self.results.multi_hand_landmarks:
            if hand_no < len(self.results.multi_hand_landmarks):
                my_hand = self.results.multi_hand_landmarks[hand_no]
                h, w, c = img.shape
                for id, lm in enumerate(my_hand.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lm_list.append([id, cx, cy])
        return lm_list


class DeviceTracker:
    TARGET_CLASSES = ("cell phone", "mouse", "keyboard")

    def __init__(self, model_path="yolo11n.pt", confidence=0.35, image_size=640):
        if YOLO is None:
            raise ModuleNotFoundError(
                "Thiếu thư viện ultralytics. Cài bằng lệnh: "
                "python -m pip install ultralytics"
            )

        self.model = YOLO(model_path)
        self.confidence = confidence
        self.image_size = image_size

        names = self.model.names
        self.class_names = {
            int(class_id): name for class_id, name in names.items()
        } if isinstance(names, dict) else dict(enumerate(names))
        name_to_id = {
            name.lower(): class_id for class_id, name in self.class_names.items()
        }
        missing_classes = [
            name for name in self.TARGET_CLASSES if name not in name_to_id
        ]
        if missing_classes:
            raise ValueError(
                f"Model {model_path!r} không có các lớp cần theo dõi: "
                f"{', '.join(missing_classes)}"
            )
        self.class_ids = [name_to_id[name] for name in self.TARGET_CLASSES]

    def track(self, img):
        results = self.model.track(
            source=img,
            persist=True,
            tracker="bytetrack.yaml",
            classes=self.class_ids,
            conf=self.confidence,
            imgsz=self.image_size,
            verbose=False,
        )
        if not results:
            return img

        result = results[0]
        if result.boxes is None:
            return img

        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            class_id = int(box.cls[0].item())
            confidence = float(box.conf[0].item())
            track_id = int(box.id[0].item()) if box.id is not None else None
            name = self.class_names[class_id]
            label = f"{name} {confidence:.2f}"
            if track_id is not None:
                label += f" ID:{track_id}"

            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 200, 255), 2)
            cv2.putText(
                img,
                label,
                (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 200, 255),
                2,
            )
        return img


def main():
    detector = HandDetector(max_hands=2, detection_con=0.7, track_con=0.5)
    device_tracker = DeviceTracker()
    cap = cv2.VideoCapture(0)
    p_time = 0

    try:
        while True:
            success, img = cap.read()
            if not success:
                print("Không thể truy cập Webcam.")
                break

            img = cv2.flip(img, 1)
            img = detector.find_hands(img, draw=True)
            img = device_tracker.track(img)
            lm_list = detector.find_positions(img, hand_no=0)

            if len(lm_list) != 0:
                x_index, y_index = lm_list[8][1], lm_list[8][2]
                cv2.circle(img, (x_index, y_index), 10, (255, 0, 255), cv2.FILLED)

            c_time = time.time()
            fps = 1 / (c_time - p_time) if (c_time - p_time) > 0 else 0
            p_time = c_time

            cv2.putText(img, f'FPS: {int(fps)}', (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            cv2.imshow("Hand and Device Tracking", img)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 27:
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()