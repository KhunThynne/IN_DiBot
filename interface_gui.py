import keyboard # type: ignore
import os
from time import sleep


class Interface():
    def __init__(self):
        self.text = ["Start", "Setting","Log Terminal", "End"]
        self.selected_index = 0  # เพิ่มตัวแปรเพื่อเก็บ index ที่ถูกเลือก
        self.choose = "Start"
        self.symbol = "EURUSD"
    def list_interface(self):
        os.system("cls")
        print(f''' 
              Indibot interface \n\n press up or down "Slice select choice"\n press Enter "Enter into programe"\n \n {self.symbol}''')
        for i, item in enumerate(self.text):
            if i == self.selected_index:
                print(f"> {item}")  # แสดงตัวเลือกที่ถูกเลือกด้วยเครื่องหมาย >
                self.choose = item
            else:
                print(f"  {item}")

    def choose_type(self,type):
        
        self.selected_index = (self.selected_index + type) % len(self.text)  # เปลี่ยน index ที่ถูกเลือกเป็นตัวถัดไป
    def selected(self):
        # print(self.choose)
        match self.choose:
            case "End":
                quit()
            case "Setting":
                self.symbol = input("symbol :")
                
            case default:
                pass
def key_press(event):
    pass
    # print(event.name)

keyboard.on_press(key_press)

gui = Interface()  # สร้างอ็อบเจ็กต์ gui นอกลูป while เพื่อประสิทธิภาพ
try:
    while True:
        
        gui.list_interface()
        sleep(0.01)

        # เช็คว่ามีการกดคีย์หรือไม่
    
        match keyboard.read_key():
            case "down":
                gui.choose_type(1)
            case "up":
                gui.choose_type(-1)
            case "enter":
                keyboard.write("test")
                gui.selected()
            case default:
                pass
        
except :
    os.system('cls')
    print("stop")

        
