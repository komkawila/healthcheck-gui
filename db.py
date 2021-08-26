import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="health_check_db"
)

mycursor = mydb.cursor()

query1 = "INSERT INTO user_tb(user_cardid, user_firstname_th, user_lastname_th, user_firstname_en, \
  user_lastname_en, user_birth, user_gender, user_address, user_address_subdistrict, user_address_district, \
  user_address_province, user_address_zipcode) \
  VALUES ('1560100447183','ภานุวัฒน์','กาวิละ','phanuwat','kawila','25401011',1,'12 ม.9','บ้านร้อง','งาว','ลำปาง','52110')\
  ON DUPLICATE KEY UPDATE user_cardid = '1560100447183';"

query2 = "INSERT INTO result_db(result_cardid, result_datetime, result_systolic, result_diastolic, result_height, \
  result_weight, result_temp, result_pulse) VALUES ('1560100447183','2021-2-25_05:22:19',120,80,170,75,35.6,89);"

mycursor.execute(query1)
mydb.commit()
mycursor.execute(query2)
mydb.commit()
