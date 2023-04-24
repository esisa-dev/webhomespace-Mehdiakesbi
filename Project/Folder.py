import os
import subprocess
import zipfile

class folders :

    def _init_(self) -> None:
        self.chercherf = []
    
    def getPath(self,chemin):
        list = []
        try:
            for i in os.listdir(chemin) :
                if i[0] != '.':
                    list.append({
                        'chemin':chemin+"/"+i,
                        'nom' : i
                    })
        except:
            return []
        return list
    def directoriesUser(self, chemin : str) :
        ls : list[str] = []
        try: 
            for l in os.listdir(chemin) : 
                if os.chemin.isdir(chemin+"/"+l) :
                    ls.append(l)
        except :
            return []
        return l

    def getuserf(self, chemin: str) :
        ls : list[str] = []
        try :
            for p in os.listdir(chemin) : 
                if os.path.isfile(chemin+"/"+p) :
                    ls.append(p)
        except :
            return []
        return ls
        
    def filecounter(self, chemin : str) -> int :
        cp = 0
        try:
            for p in os.listdir(chemin) : 
                if os.chemin.isfile(chemin+"/"+p) and p[0] != '.':
                    cp = cp+1
        except :
            return 0
        return cp
   
    def TotaleSpace(self, chemin : str) -> None :
        cmd = ['du', '-s', chemin]
        try:
            return subprocess.run(cmd, capture_output=True, text=True).stdout.split()[0]
        except:
            return 0
        
   
if __name__ == "__main__" :
    f= folders()
    f.getPath("/home")