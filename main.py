from filemanager import Filemanager
from PreProc import PreProc
from model import model
dest = "/home/dan/Videos"
# # clusterlist = []
#
filemanager = Filemanager("/home/dan/Documents", dest)
PreProc = PreProc()
#
#
files = filemanager.getFiles()
contentlist = filemanager.getSummary()
#
# processed_file = PreProc.preprocessing(files)
#
print(files)
print(contentlist)
# print(processed_file)
#
# model = model("/home/dan/Documents")
# clusters = model.filemodel()
# model.save_model()
#
#
#
# filemanager.moveFilesToCluster(clusters)
#
#
# # if files is not None:
#     # print(processed_file)
#
#     # print(processed_file)