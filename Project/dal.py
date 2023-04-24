import crypt, os, spwd

class userdao:
    def _init_(self,user:str,pwd:str) -> None:
        self.user=user
        self.pwd=pwd
    def FindUser(self)->bool:
        if self.user in os.listdir("/home"):
            return True
        else :
            return False
        
    def authenticate(self, usn, pwd) -> bool:
        user=spwd.getspnam(usn)
        if(crypt.crypt(pwd, user.sp_pwdp)) == user.sp_pwdp:
            return True
        return False
    def Check(self)->bool:
        if self.authenticate==True and self.FindUser==True:
            return True
        else:
            return False