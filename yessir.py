import requests
import threading
import random



#INPUT THE PHISHING PAGE URL IN HERE
url2 = ('')


#usernames and passwords that it will use at random

user1 = ['xl706','wolflord123','valtryek1221']
u1 = random.choice(user1)
pass1 = ['aubm444','app126']
p1 = random.choice(pass1)

user2 = ['talorswi0','swirlcfan','sero43']
u2 = random.choice(user2)
pass2 = ['anthon16','alldav35']
p2 = random.choice(pass2)

user3 = ['rosythedog9','rose1069','ocw26']
u3 = random.choice(user3)
pass3 = ['brooklynn20098','brabra2','ayden0']
p3 = random.choice(pass3)

user4 = ['nena9908','ml361','merkitty18']
u4 = random.choice(user4)
pass4 = ['nommoe','forever322']
p4 = random.choice(pass4)

user5 = ['lexa997','koolbunny360','kkunicorn66']
u5 = random.choice(user5)
pass5 = ['cashday52','butsam81']
p5 = random.choice(pass5)

user6 = ['kkcray4','kenz11023','jazyjazy']
u6 = random.choice(user6)
pass6 = ['coll25','chase908',]
p6 = random.choice(pass6)

user7 = ['jayla50','jamming67','hplover10']
u7 = random.choice(user7)
pass7 = ['elephants23','dare23']
p7 = random.choice(pass7)

user8 = ['hhhj55','gummyworm24','greennoava']
u8 = random.choice(user8)
pass8 = ['hay54','gggamer53','epicmat51']
p8 = random.choice(pass8)

user9 = ['frozentiger107','fortnitepro2349','emma93596']
u9 = random.choice(user9)
pass9 = ['jonathane27','ilovemommy12323','hunterjk']
p9 = random.choice(pass9)

user10 = ['coolblazeboy','calws4paws']
u10 = random.choice(user10)
pass10 = ['lakota7','komo108','karm18']
p10 = random.choice(pass10)

user11 = ['brok9151','aubree8344','asriel80']
u11 = random.choice(user11)
pass11 = ['mglit3','major0915']
p11 = random.choice(pass11)

user12 = ['asqw02','anthony9705']
u12 = random.choice(user12)
pass12 = ['paiboo8','minecraftia25']
p12 = random.choice(pass12)

user13 = ['scarlettcool48','genji30']
u13 = random.choice(user13)
pass13 = ['parrya67','pandagirl177']
p13 = random.choice(pass13)

user14 = ['scarlettcool48','genji30']
u14 = random.choice(user14)
pass14 = ['ramjes90','plp33','paycol25']
p14 = random.choice(pass14)

user15 = ['fashiondiva106','cookiekat613']
u15 = random.choice(user15)
pass15 = ['shelby1100','sether7','samyl91']
p15 = random.choice(pass15)

user16 = ['tzi2011','twilightsparkl53']
u16 = random.choice(user16)
pass16 = ['trevor138','skajes42']
p16 = random.choice(pass16)

user17 = ['teeba200','snowflakemocha','samedraek6','rosewolf907']
u17 = random.choice(user17)
pass17 = ['ajnew66','wilmax96','w25rothwella']
p17 = random.choice(pass17)

user18 = ['princessgrace0','natacha4','mythical2','lieutenant16']
u18 = random.choice(user18)
pass18 = ['kr3647','jasm49','coocoo63','animals82']
p18 = random.choice(pass18)

user19 = ['jils209','issie62','megathree23','oliverf12']
u19 = random.choice(user19)
pass19 = ['gangster42','momdad12','PlayBoy14']
p19 = random.choice(pass19)

user20 = ['nandtv','toasty15','authe27','vuifox1','pancake12doll']
u20 = random.choice(user20)
pass20 = ['sparklingsea9','shepdogg']
p20 = random.choice(pass20)

user21 = ['kai1312','misterfoxwolfy1','ajpwboy1','firefox12']
u21 = random.choice(user21)
pass21 = ['adam7097','tiffany824','summer656']
p21 = random.choice(pass21)









#which data will be spammed, and with that data
data1 = {
    'username' : u1,
    'password' : p1
}
data2 = {
    'username' : u2,
    'password' : p2
}
data3 = {
    'username' : u3,
    'password' : p3
}
data4 = {
    'username' : u4,
    'password' : p4
}
data5 = {
    'username' : u5,
    'password' : p5
}
data6 = {
    'username' : u6,
    'password' : p6
}
data7 = {
    'username' : u7,
    'password' : p7
}
data8 = {
    'username' : u8,
    'password' : p8
}
data9 = {
    'username' : u9,
    'password' : p9
}
data10 = {
    'username' : u10,
    'password' : p10
}
data11 = {
    'username' : u11,
    'password' : p11
}
data12 = {
    'username' : u12,
    'password' : p12
}
data13 = {
    'username' : u13,
    'password' : p13
}
data14 = {
    'username' : u14,
    'password' : p14
}
data15 = {
    'username' : u15,
    'password' : p15
}
data16 = {
    'username' : u16,
    'password' : p16
}
data17 = {
    'username' : u17,
    'password' : p17
}
data18 = {
    'username' : u18,
    'password' : p18
}
data19 = {
    'username' : u19,
    'password' : p19
}
data20 = {
    'username' : u20,
    'password' : p20
}
data21 = {
    'username' : u21,
    'password' : p21
}







#sending and printing the response
def do_request():
    while True:
        response1 = requests.post(url2, data=data1).text
        print(data1)
        response2= requests.post(url2, data=data2).text
        print(data2)
        response3= requests.post(url2, data=data3).text
        print(data3)
        response4= requests.post(url2, data=data4).text
        print(data4)
        response5= requests.post(url2, data=data5).text
        print(data5)
        response6= requests.post(url2, data=data6).text
        print(data6)
        response7= requests.post(url2, data=data7).text
        print(data7)
        response8= requests.post(url2, data=data8).text
        print(data8)
        response9= requests.post(url2, data=data9).text
        print(data9)
        response10= requests.post(url2, data=data10).text
        print(data10)
        response11= requests.post(url2, data=data11).text
        print(data11)
        response12= requests.post(url2, data=data12).text
        print(data12)
        response13= requests.post(url2, data=data13).text
        print(data13)
        response14= requests.post(url2, data=data14).text
        print(data14)
        response15= requests.post(url2, data=data15).text
        print(data15)
        response16= requests.post(url2, data=data16).text
        print(data16)
        response17= requests.post(url2, data=data17).text
        print(data17)
        response18= requests.post(url2, data=data18).text
        print(data18)
        response19= requests.post(url2, data=data19).text
        print(data19)
        response20= requests.post(url2, data=data20).text
        print(data20)
        response21= requests.post(url2, data=data21).text
        print(data21)

threads = []

for i in range(2):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(2):
    threads[i].start()

for i in range(2):
    threads[i].join()
