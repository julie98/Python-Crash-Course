# from privileges import User, Privileges, Admin
import privileges

julie = privileges.Admin('Haoyu', 'Zhu', 'julie', 'julie@example.com', 'tianjin')
julie.privileges.show_privileges()
