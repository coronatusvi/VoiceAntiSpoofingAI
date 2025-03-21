Đúng vậy, để đảm bảo tính khoa học và nhất quán, bạn nên sử dụng một chương trình tự động để tạo và ghi metadata (các tệp giao thức) cho bộ dữ liệu. Dưới đây là cách bạn có thể làm điều này:

---

### **1. Xây dựng chương trình tự động tạo metadata**
Bạn có thể viết một script Python để tự động duyệt qua các tệp âm thanh trong thư mục `train`, `dev`, và `eval`, sau đó tạo các tệp giao thức (`cm_protocols`) tương ứng.

#### **Ví dụ mã Python:**
```python
import os
import random

# Đường dẫn đến các thư mục dữ liệu
base_dir = "LA"
train_dir = os.path.join(base_dir, "ASVspoof2025_LA_train")
dev_dir = os.path.join(base_dir, "ASVspoof2025_LA_dev")
eval_dir = os.path.join(base_dir, "ASVspoof2025_LA_eval")
protocol_dir = os.path.join(base_dir, "ASVspoof2025_LA_cm_protocols")

# Đảm bảo thư mục giao thức tồn tại
os.makedirs(protocol_dir, exist_ok=True)

# Hệ thống giả mạo và nhãn
spoof_systems = {
    "A01": "TTS neural waveform model",
    "A05": "VC vocoder",
    "A15": "TTS_VC neural waveform"
}
bonafide_label = "bonafide"

# Hàm tạo metadata
def create_protocol(directory, output_file, spoof_systems, bonafide_label):
    protocol_lines = []
    speaker_id_counter = 1

    for file_name in sorted(os.listdir(directory)):
        if file_name.endswith(".flac"):
            # Tạo SPEAKER_ID
            speaker_id = f"LA_{speaker_id_counter:04d}"
            audio_file_name = os.path.splitext(file_name)[0]

            # Xác định loại âm thanh (bonafide hoặc spoof)
            if "bonafide" in file_name:
                system_id = "-"
                key = bonafide_label
            else:
                # Lấy mã hệ thống từ tên file (ví dụ: A01, A05, A15)
                system_id = next((s for s in spoof_systems if s in file_name), None)
                key = "spoof"

            # Ghi dòng giao thức
            if system_id:
                protocol_lines.append(f"{speaker_id} {audio_file_name} - {system_id} {key}")
                speaker_id_counter += 1

    # Ghi vào tệp giao thức
    with open(output_file, "w") as f:
        f.write("\n".join(protocol_lines))
    print(f"Protocol file created: {output_file}")

# Tạo các tệp giao thức
create_protocol(train_dir, os.path.join(protocol_dir, "ASVspoof2025.LA.cm.train.trn.txt"), spoof_systems, bonafide_label)
create_protocol(dev_dir, os.path.join(protocol_dir, "ASVspoof2025.LA.cm.dev.trl.txt"), spoof_systems, bonafide_label)
create_protocol(eval_dir, os.path.join(protocol_dir, "ASVspoof2025.LA.cm.eval.trl.txt"), spoof_systems, bonafide_label)
```

---

### **2. Cách hoạt động của chương trình**
- **Duyệt qua các tệp âm thanh**: Chương trình sẽ duyệt qua các tệp `.flac` trong các thư mục `train`, `dev`, và `eval`.
- **Xác định loại âm thanh**:
  - Nếu tên tệp chứa từ khóa `bonafide`, nó sẽ được gắn nhãn là `bonafide`.
  - Nếu tên tệp chứa mã hệ thống (ví dụ: `A01`, `A05`, `A15`), nó sẽ được gắn nhãn là `spoof` với mã hệ thống tương ứng.
- **Tạo SPEAKER_ID**: SPEAKER_ID được tạo tự động theo thứ tự tăng dần (ví dụ: `LA_0001`, `LA_0002`).
- **Ghi vào tệp giao thức**: Các dòng giao thức được ghi vào tệp `.txt` trong thư mục `cm_protocols`.

---

### **3. Kết quả**
Sau khi chạy chương trình, bạn sẽ có các tệp giao thức trong thư mục `LA/ASVspoof2025_LA_cm_protocols` với nội dung tương tự như sau:

#### **ASVspoof2025.LA.cm.train.trn.txt**
```plaintext
LA_0001 LA_T_0001 - bonafide
LA_0002 LA_T_0002 - A01 spoof
LA_0003 LA_T_0003 - A05 spoof
LA_0004 LA_T_0004 - A15 spoof
```

#### **ASVspoof2025.LA.cm.dev.trl.txt**
```plaintext
LA_0005 LA_D_0001 - bonafide
LA_0006 LA_D_0002 - A01 spoof
LA_0007 LA_D_0003 - A05 spoof
LA_0008 LA_D_0004 - A15 spoof
```

#### **ASVspoof2025.LA.cm.eval.trl.txt**
```plaintext
LA_0009 LA_E_0001 - bonafide
LA_0010 LA_E_0002 - A01 spoof
LA_0011 LA_E_0003 - A05 spoof
LA_0012 LA_E_0004 - A15 spoof
```

---

### **4. Lợi ích của chương trình tự động**
- **Tính nhất quán**: Đảm bảo rằng tất cả các tệp giao thức được tạo theo cùng một định dạng.
- **Tiết kiệm thời gian**: Không cần tạo thủ công các tệp giao thức.
- **Dễ dàng mở rộng**: Có thể dễ dàng thêm các hệ thống giả mạo mới (ví dụ: A02, A03) bằng cách cập nhật danh sách `spoof_systems`.

---

### **5. Kiểm tra và xác minh**
- Đảm bảo rằng tất cả các tệp âm thanh được liệt kê trong tệp giao thức đều tồn tại trong thư mục tương ứng.
- Kiểm tra định dạng của các tệp giao thức để đảm bảo chúng tuân thủ đúng cấu trúc.

---

Với chương trình trên, bạn có thể tự động tạo metadata cho bộ dữ liệu một cách khoa học và hiệu quả.