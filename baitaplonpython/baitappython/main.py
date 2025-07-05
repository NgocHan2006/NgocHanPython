import json
import random


def luu_du_lieu_vao_file():
    with open("vocab_data.json", "w", encoding="utf-8") as f:
        json.dump(vocab_data, f, ensure_ascii=False, indent=4)

def them_tu_vung():
    chu_de = input("Nhập chủ đề: ")
    tu = input("Nhập từ vựng: ")
    nghia = input("Nhập nghĩa: ")
    tu_moi = {"từ": tu, "nghĩa": nghia, "điểm": 0, "lịch sử": []}
    if chu_de not in vocab_data:
        vocab_data[chu_de] = []
    vocab_data[chu_de].append(tu_moi)
    luu_du_lieu_vao_file()
    print("Đã thêm từ.")

def them_chu_de():
    chu_de = input("Nhập tên chủ đề mới: ")
    if chu_de in vocab_data:
        print("Chủ đề đã tồn tại.")
    else:
        vocab_data[chu_de] = []
        luu_du_lieu_vao_file()
        print("Đã thêm chủ đề.")

def xem_tu_theo_chu_de():
    for chu_de in vocab_data:
        print(f"\n== {chu_de} ==")
    for item in vocab_data[chu_de]:
        print(f"{item['từ']} - {item['nghĩa']} (Điểm: {item['điểm']})")

def hien_thi_tat_ca_tu():
    print("== Tất cả từ vựng ==")
    for chu_de, ds in vocab_data.items():
        for item in ds:
            print(f"{item['từ']} ({chu_de}) - {item['nghĩa']} | Điểm: {item['điểm']}")

def tim_kiem_tu():
    tu_khoa = input("Nhập từ cần tìm: ")
    for chu_de, ds in vocab_data.items():
        for item in ds:
            if tu_khoa in item["từ"] or tu_khoa in item["nghĩa"]:
                print(f"Tìm thấy trong {chu_de}: {item}")

def sua_thong_tin_tu():
    tu_khoa = input("Nhập từ cần sửa: ")
    for chu_de, ds in vocab_data.items():
        for item in ds:
            if item["từ"] == tu_khoa:
                item["nghĩa"] = input("Nhập nghĩa mới: ")
                luu_du_lieu_vao_file()
                print("Đã cập nhật.")
                return
    print("Không tìm thấy từ.")

def xoa_tu_vung():
    tu_khoa = input("Nhập từ cần xóa: ")
    for chu_de, ds in vocab_data.items():
        for item in ds:
            if item["từ"] == tu_khoa:
                ds.remove(item)
                luu_du_lieu_vao_file()
                print("Đã xóa.")
                return
    print("Không tìm thấy từ.")

def luyen_tap_ngau_nhien():
    all_words = [(cd, item) for cd in vocab_data for item in vocab_data[cd]]
    if not all_words:
        print("Không có từ nào để luyện tập.")
        return
    chu_de, tu = random.choice(all_words)
    dap_an = input(f"Nghĩa của từ '{tu['từ']}' là gì? ")
    if dap_an.strip().lower() == tu["nghĩa"].lower():
        print("Đúng rồi!")
        tu["điểm"] += 1
        tu["lịch sử"].append(True)
    else:
        print(f"Sai. Đáp án đúng là: {tu['nghĩa']}")
        tu["lịch sử"].append(False)
    luu_du_lieu_vao_file()

def cap_nhat_diem():
    tu_khoa = input("Nhập từ cần cập nhật điểm: ")
    for ds in vocab_data.values():
        for item in ds:
            if item["từ"] == tu_khoa:
                diem = int(input("Nhập điểm mới: "))
                item["điểm"] = diem
                luu_du_lieu_vao_file()
                print("Đã cập nhật điểm.")
                return
    print("Không tìm thấy từ.")

def hien_thi_lich_su_on_luyen():
    tu_khoa = input("Nhập từ cần xem lịch sử: ")
    for ds in vocab_data.values():
        for item in ds:
            if item["từ"] == tu_khoa:
                print("Lịch sử luyện tập:", item["lịch sử"])
                return
    print("Không tìm thấy từ.")

def thong_ke_diem_on():
    print("== Thống kê theo điểm ==")
    thong_ke = {}
    for ds in vocab_data.values():
        for item in ds:
            d = item["điểm"]
            thong_ke[d] = thong_ke.get(d, 0) + 1
    for d, sl in sorted(thong_ke.items()):
        print(f"Điểm {d}: {sl} từ")

def hien_thi_tu_sai_nhieu():
    print("== Các từ sai nhiều nhất ==")
    tu_sai_nhieu = []
    for chu_de, ds in vocab_data.items():
        for item in ds:
            so_sai = item["lịch sử"].count(False)
            tu_sai_nhieu.append((so_sai, item["từ"], chu_de))
    tu_sai_nhieu.sort(reverse=True)
    for so_sai, tu, chu_de in tu_sai_nhieu[:5]:
        print(f"{tu} ({chu_de}) - Sai: {so_sai} lần")

def hien_thi_tu_diem_0():
    print("== Các từ có điểm = 0 ==")
    for chu_de, ds in vocab_data.items():
        for item in ds:
            if item["điểm"] == 0:
                print(f"{item['từ']} - {item['nghĩa']} ({chu_de})")

def hien_thi_diem_cao_nhat():
    max_diem = max(item["điểm"] for ds in vocab_data.values() for item in ds)
    print(f"Các từ có điểm cao nhất ({max_diem}):")
    for chu_de, ds in vocab_data.items():
        for item in ds:
            if item["điểm"] == max_diem:
                print(f"{item['từ']} - {item['nghĩa']} ({chu_de})")

def sap_xep_tu_theo_alphabet():
    print("== Từ sắp xếp theo Alphabet ==")
    all_words = []
    for chu_de, ds in vocab_data.items():
        for item in ds:
            all_words.append((item["từ"], chu_de, item["nghĩa"]))
    for tu, cd, nghia in sorted(all_words):
        print(f"{tu} ({cd}) - {nghia}")

def hien_thi_tu_diem_thap():
    try:
        nguong = int(input("Nhập điểm tối đa (hiển thị các từ có điểm ≤ giá trị này): "))
    except ValueError:
        print("Giá trị không hợp lệ.")
        return
    print(f"== Các từ có điểm ≤ {nguong} ==")
    for chu_de, ds in vocab_data.items():
        for item in ds:
            if item["điểm"] <= nguong:
                print(f"{item['từ']} ({chu_de}) - {item['nghĩa']} | Điểm: {item['điểm']}")

def xuat_du_lieu_ra_file():
    ten_file = input("Nhập tên file muốn xuất (.json): ")
    with open(ten_file, "w", encoding="utf-8") as f:
        json.dump(vocab_data, f, ensure_ascii=False, indent=4)
    print("Dữ liệu đã được ghi vào", ten_file)

def dem_so_tu_trong_chu_de():
    print("== Số từ trong mỗi chủ đề ==")
    for chu_de, ds in vocab_data.items():
        print(f"{chu_de}: {len(ds)} từ")

def dat_lai_diem_tat_ca():
    for ds in vocab_data.values():
        for item in ds:
            item["điểm"] = 0
    luu_du_lieu_vao_file()
    print("Đã đặt lại điểm cho tất cả từ.")

def menu():
    while True:
        print("\n=== MENU QUẢN LÝ TỪ VỰNG ===")
        print("1. Thêm từ vựng")
        print("2. Thêm chủ đề")
        print("3. Xem từ theo chủ đề")
        print("4. Hiển thị tất cả từ")
        print("5. Tìm kiếm từ")
        print("6. Sửa thông tin từ vựng")
        print("7. Xóa từ vựng")
        print("8. Luyện tập từ ngẫu nhiên")
        print("9. Cập nhật điểm ôn luyện")
        print("10. Hiển thị lịch sử ôn luyện")
        print("11. Thống kê theo điểm ôn")
        print("12. Hiển thị từ sai nhiều nhất")
        print("13. Hiển thị từ có điểm = 0")
        print("14. Hiển thị từ điểm cao nhất")
        print("15. Hiển thị từ có điểm thấp hơn giá trị nhập vào")
        print("16. Sắp xếp từ theo alphabet")
        print("17. Xuất dữ liệu ra file khác")
        print("18. Đếm số từ trong từng chủ đề")
        print("19. Đặt lại điểm tất cả từ")
        print("20. Lưu dữ liệu thủ công")
        print("21. Thoát chương trình")

        choice = input("Chọn chức năng (1-21): ")
        if choice == "1":
            them_tu_vung()
        elif choice == "2":
            them_chu_de()
        elif choice == "3":
            xem_tu_theo_chu_de()
        elif choice == "4":
            hien_thi_tat_ca_tu()
        elif choice == "5":
            tim_kiem_tu()
        elif choice == "6":
            sua_thong_tin_tu()
        elif choice == "7":
            xoa_tu_vung()
        elif choice == "8":
            luyen_tap_ngau_nhien()
        elif choice == "9":
            cap_nhat_diem()
        elif choice == "10":
            hien_thi_lich_su_on_luyen()
        elif choice == "11":
            thong_ke_diem_on()
        elif choice == "12":
            hien_thi_tu_sai_nhieu()
        elif choice == "13":
            hien_thi_tu_diem_0()
        elif choice == "14":
            hien_thi_diem_cao_nhat()
        elif choice == "15":
            hien_thi_tu_diem_thap()
        elif choice == "16":
            sap_xep_tu_theo_alphabet()
        elif choice == "17":
            xuat_du_lieu_ra_file()
        elif choice == "18":
            dem_so_tu_trong_chu_de()
        elif choice == "19":
            dat_lai_diem_tat_ca()
        elif choice == "20":
            luu_du_lieu_vao_file()
            print("✅ Đã lưu dữ liệu vào file.")
        elif choice == "21":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.")

with open("vocab_data.json", "r", encoding="utf-8") as f:
    vocab_data = json.load(f)

if __name__ == "__main__":
    menu()
