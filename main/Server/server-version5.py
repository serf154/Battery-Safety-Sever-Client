#!/usr/bin/python3
import sys
sys.path.append("C:\\Users\\SERF1\\Desktop\\Battery-Safety-Sever-Client")
from main.Tools.File import File
from main.Tools.ServerConnection import Connection
import time
import logging

class Server_PC:
    def __init__(self):
        # variable
        self.content = {};
        self.labels = [];
        logging.basicConfig(filename='Server_Error_Record.log', level=logging.WARNING)

        ## section1: file and floder creation
        print("check the connection")
        self.ConnectionObj = Connection();
        print("*****************************************")

        self.receiveContentFromClient();

        print("*****************************************")
        print("initialize the File")
        self.FileObj = File(self.getLabels())

    def run(self):
        while True:
            print('start the loop')
            print("current time is " + time.strftime('%H-%M-%S'))

            self.receiveContentFromClient();
            self.writeToFile();
            print('complete the loop \n')

    def writeToFile(self):
        for key in self.content:
            assert isinstance(key, str)
            if "is" in key and not self.content[key]:
                print(key + ": " + self.content[key])
        self.FileObj.WritetoCVS(self.datas, self.labels)

    def updateLabelsFromContent(self):
        self.labels = []
        for key in self.content:
            self.labels.append(key)
    def updateDatasFromContent(self):
        self.datas = [];
        for key in self.content:
            self.datas.append(self.content[key])

    def receiveContentFromClient(self):
        while(True):
            try:
                self.content = self.ConnectionObj.receiveContent()
                self.updateLabelsFromContent();
                self.updateDatasFromContent();
                break;
            except Exception as e:
                print(e);
                self.ConnectionObj.reconnect()


    def getLabels(self):
        return self.labels;
    def getDatas(self):
        return self.datas;

server_PC = Server_PC();
server_PC.run();




                    
                

