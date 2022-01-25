from rest_framework import permissions


class IsStuffOrReadOnly(permissions.IsAdminUser):#bu arkadaşın admin yetkisi var mı yok mu(admin mi kullanııcı mı)(IsAdminUserdan inherit ediyoruz)
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:#user staf değilse sadece safe methodlara izin verecek(sadece get ile çekebilecek)
            return True#eğer kullanıcı sadece get methodubu kullandıysa her türlü bilgiyi görmesine izin ver ama get dısında (post,delete,update m)methodlaını çağıdıysa sadece is_staff olan kullanıcıya ixin ver
        else:#eğer safe method değil (post,delete,petch,post(create,update,delete) gibi birşeyse)
            return bool(request.user and request.user.is_staff)#ama get dısında (post,delete,update m)methodlaını çağıdıysa sadece is_staff olan kullanıcıya ixin ver
            
            
        
        