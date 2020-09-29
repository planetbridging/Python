import random
import string

#Created by Shannon Setter 29-09-2020

random_names = ['darcie','molly','kye','bob','shannon','mark','emmie','john','helena','jasmine','phoebe','ash','jack']
random_work_typs = ['partime','fulltime','casual']
random_degrees = ['Acting','Animation','Arts','IT','Business','Commerce','Dental','Crimonology','Design']
random_address = ['QLD109176','QLD109204','QLD109291','QLD109369','QLD134854','QLD135938','QLD136346','QLD136676','QLD137415','QLD137533']
random_gender = ['male','female']
everyones_bd = "2020-09-01"

def get_random_string(uchars = 3, lchars = 3, dchars = 2, schars = 2):
    # Generates a 10 characters long random string
    # with 3 upper case, 3 lowe case, 2 digits and 2 special characters
 
    str_uchars, str_lchars, str_dchars, str_schars = '', '', '', ''
 
    for i in range(uchars):
        str_uchars += random.SystemRandom().choice(string.ascii_uppercase)
 
    for i in range(lchars):
        str_uchars += random.SystemRandom().choice(string.ascii_lowercase)
 
    for i in range(dchars):
        str_uchars += random.SystemRandom().choice(string.digits)
 
    for i in range(schars):
        str_uchars += random.SystemRandom().choice(string.punctuation)
 
    random_str = str_uchars + str_lchars + str_dchars + str_schars
    random_str = ''.join(random.sample(random_str, len(random_str)))
    return random_str
    
def get_random_name():
    n = random.randint(0,len(random_names)-1)
    return random_names[n]
    
def get_random_work_type():
    n = random.randint(0,len(random_work_typs)-1)
    return random_work_typs[n]
    
def get_random_course_name():
    n = str(random.randint(1000,9999)) + "ICT"
    return n
 
def get_random_phone():
    n = random.randint(1000000000,9999999999)
    return n
    
def get_random_address():
    n = random.randint(0,len(random_address)-1)
    return random_address[n]
    
def get_random_gender():
    n = random.randint(0,len(random_gender)-1)
    return random_gender[n]

    
    
def generator_random_perons():
    r_person_id = get_random_string(23, 23, 4, 0)
    r_address = get_random_address()
    r_first = get_random_name()
    r_middle = get_random_name()
    r_laste = get_random_name()
    r_p_home = str(get_random_phone())
    r_p_mob = str(get_random_phone())
    r_p_emer = str(get_random_phone())
    r_u_n = str(random.randint(0,30))
    r_s_n = str(random.randint(0,30))
    r_g = get_random_gender()
    start_statement = "INSERT INTO tbl_person_details (id_person,id_address,first_name,middle_name,last_name,gender,DOB,home_phone,mobile_phone,emergency_phone,street_number,unit_number,address_prefix,notes)"
    end_statement = "VALUES ('" + r_person_id + "','"+ r_address + "','"+ r_first + "','"+ r_middle + "','"+ r_laste + "','"  + r_g +"','"+ everyones_bd + "','"+ r_p_home + "','"+ r_p_mob + "','"+ r_p_emer + "','"+ r_s_n + "','"+ r_u_n + "','','');"
    print(start_statement + end_statement)
    return r_person_id
    
def generator_random_staffs(id_staff,id_person,id_reports_to):
    r_w_t = get_random_work_type()
    r_h_r = str(random.randint(20,100))

    start_statement = "INSERT INTO tbl_staff (id_staff,id_person,position,work_type,hourly_rate,reports_to,duty)"
    end_statement = "VALUES ('" + id_staff + "','"+ id_person + "','random','"+ r_w_t + "','"+ r_h_r + "','+"+id_reports_to+"+','random');"
    print(start_statement + end_statement)
    #return r_staff_id

print('/*----------Welcome to Remarkable University Created by Shannon Setter----------*/')
print('')

print('/*----------Random person data----------*/')
print('')
for x in range(10):
    generator_random_perons()
    
    
print('/*----------Random staff data----------*/')
print('')
random_staff_ids = []
for x in range(10):
    r_person_id = generator_random_perons()
    r_reports_to = ""
    r_staff_id = get_random_string(23, 23, 4, 0)
    if len(random_staff_ids) >= 1:
        r_reports_to = random_staff_ids[0][0]
        #print("REPORTS: " + r_reports_to)
    
    random_staff_ids.append([r_person_id,r_staff_id])
    generator_random_staffs(r_staff_id,r_person_id,r_reports_to)
    #print(random_staff_ids)
        
print('/*----------Random degrees data----------*/')
print('')

random_degree_ids = []
rd = 0
for b in random_degrees:
    r_degree_id = get_random_string(23, 23, 4, 0)
    r_d = "Bachelor of " + b
    start_statement = "INSERT INTO tbl_degrees (id_degree,id_staff,name,entry_req,full_time_duration,part_time_duration,credit_points,domestic_fee,international_fee,campus)"
    end_statement = "VALUES ('" + r_degree_id + "','"+ random_staff_ids[rd][1] + "','"+r_d+"','not much','long time','long time with breaks',240,30000,50000,'nathan');"
    print(start_statement + end_statement)
    random_degree_ids.append([r_degree_id,random_staff_ids[rd][1]])
    rd+=1
    
print('/*----------Random courses data----------*/')
print('')

random_course_ids = []
rc = 0
for b in random_degrees:
    r_course_id = get_random_string(23, 23, 4, 0)
    r_c = get_random_course_name()
    start_statement = "INSERT INTO tbl_courses (id_course,id_degree,id_staff,name,entry_req,full_time_duration,part_time_duration,credit_points,domestic_fee,international_fee,campus)"
    end_statement = "VALUES ('" + r_course_id + "','"+ random_degree_ids[rc][0] + "','"+random_degree_ids[rc][1]+"','"+r_c+"','not much','long time','long time with breaks',240,3000,5000,'nathan');"
    print(start_statement + end_statement)
    random_course_ids.append(r_course_id)
    rc+=1
    
print('/*----------Random student data----------*/')
print('')

rc = 0
for b in random_degrees:
    print("/*---student " + str(rc) + " start---*/")
    r_enroll_id = get_random_string(23, 23, 4, 0)
    r_student_id = get_random_string(23, 23, 4, 0)
    r_person_id = generator_random_perons()
    r_student_enroll_id = get_random_string(23, 23, 4, 0)
    print("INSERT INTO tbl_student (id_student,id_person) VALUES ('"+r_student_id+"','"+r_person_id+"');")
    print("INSERT INTO tbl_degree_enrolled (id_enroll,id_student,id_degree,start_date,est_finish_date) VALUES ('"+r_enroll_id+"','"+r_student_id+"','"+random_degree_ids[rc][0]+"','"+everyones_bd+"','"+everyones_bd+"');")
    print("INSERT INTO tbl_student_enrolled (id_student_enrolled,id_student,id_course,current_grade,enrolled_status,credit_points,domestic_fee,international_fee,campus) VALUES ('"+r_student_enroll_id+"','"+r_student_id+"','"+random_course_ids[rc]+"',4,'registered',10,3000,5000,'nathan');")
    print("/*---student " + str(rc) + " end---*/")
    print('')
    rc+= 1






    
#print('Your Random String-1:', get_random_string(23, 23, 4, 0))
#print(get_random_name())
#print(get_random_course_name())
