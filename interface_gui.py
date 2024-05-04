import keyboard # type: ignore
import os
from time import sleep


class Monitor():
    def __init__(self,symbol="EURUSD",list_text=[]):
        self.list_text = ["Start", "Setting","Log Terminal"] or list_text
        self.selected_index_row = 0  # เพิ่มตัวแปรเพื่อเก็บ index ที่ถูกเลือก
        self.selected_index_col = False
        self.choose = ""
        self.symbol = symbol
        self.exit = ''
        
        self.main()
    def show(self):      
        os.system('cls')
      
        print(f'''Indibot interface \n\n press up or down "Slice select choice"\n press right "Enter into programe Press ESC to exit()"\n \n Current = {self.symbol} \n''')
       
        for i, item in enumerate(self.list_text): 
            if i == self.selected_index_row:
                print(f">__{item}")  # แสดงตัวเลือกที่ถูกเลือกด้วยเครื่องหมาย >
                self.choose = item
            else:
                print(f"  {item}") 
                
                          
        if self.selected_index_col:
                 match self.choose:
                  
                    case "Setting":
                        if self.selected_index_col :
                            self.symbol = input("\nsymbol : ")
                        
                                # print("Do you want to save [Y/n]")
                            
                                    
                            self.selected_index_col = False
                                   
                      
                            
                    case default:
                        print("tesr")  
                        
                        
                     
    def main(self):
        
            def Enter():
                
                self.selected_index_col = True
             
            try:
                self.show()
                keyboard.on_press(self.key_press)
                keyboard.add_hotkey('down', lambda:self.choose_type(1) )
                keyboard.add_hotkey('up', lambda:self.choose_type(-1))
                keyboard.add_hotkey('right', lambda: Enter())
                       
                keyboard.wait('esc')
            except EOFError as e:
               
                print(e)

    def choose_type(self,type):
            
                
        self.selected_index_col = False
             
        self.selected_index_row = (self.selected_index_row + type) % len(self.list_text)  # เปลี่ยน index ที่ถูกเลือกเป็นตัวถัดไป
   

    def key_press(self,even):
      
        self.show()    
        
        
class MoveKey(Monitor):
    def __init__(self):
        super().__init__()        
    
# def key_press(event):
#     pass
#     # print(event.name)

# keyboard.on_press(key_press)

try:
    gui = Monitor()  # สร้างอ็อบเจ็กต์ gui นอกลูป while เพื่อประสิทธิภาพ
except EOFError as e:
  
    print(e)

finally:
    os.system('cls')
   