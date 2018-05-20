from user_info import User 
from privileges import Admin, Privileges 

julie = Admin('Haoyu', 'Zhu', 'julie', 'julie@example.com', 'tianjin')
julie.privileges.show_privileges()
