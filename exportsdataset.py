from datetime import datetime
import os


class ExportsDataset():
    def __init__(self,dataset,symbol,indicator,path_ex = False) -> None:
        global MACD_return,result_Data,data
        self.dataset = dataset
        self.symbol = symbol
        self.indicator = indicator
        self.__initial()
        self.exportfile()
        self.path_ex = {path_ex if type(path_ex) !=bool else ""}
        self.date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    def __initial(self)->None:
        os.makedirs(f"./dataset/{self.symbol}/{self.path_ex}/indicators/{self.indicator['type']}", exist_ok=True)          
    def exportfile(self,path=False) -> None:
        with open(f'dataset/{self.symbol}/Dataset_{self.date_time}.json', 'w') as f:
            f.write(self.dataset.to_json(orient="index"))
        #indicators
       
        with open(f'dataset/{self.symbol}/indicators/{self.indicator['type']}/Dataset_{self.date_time}.json', 'w') as f:
            f.write(self.indicator['values'].to_json(orient="index"))
