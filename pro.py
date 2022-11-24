from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/manager/')
def manager():
    return render_template('manager.html')

@app.route('/us/')
def us():
    return render_template('user.html')
    
@app.route('/user/',methods=['POST'])
def user():
    name= request.form['name']
    tel = request.form['tel']
    num = request.form['num']
    pwd = request.form['pwd']

    if name=="" or tel=="" or num=="" or pwd=="":
        msg='모두 입력해야합니다'
    else:
        file=open('./data/info.txt','a')
        data = "%s( %s )/%s,%s\n" % (name,tel,num,pwd)
        file.write(data)
        file.close()
        file=open('./data/pwd.txt','a')
        pwdData = "%s,%s\n"%(numData,pwdData)
        file.write(pwdData)
        file.close()
        msg='정보가 저장 되었습니다'
    
    return render_template('user.html',msg=msg)

@app.route('/manager/userList',methods=['GET'])
def userInfo():
    name = request.args.get('name')
    tel = request.args.get('tel')
    num = request.args.get('num')
    pwd = request.args.get('pwd')
    dict={}
    try:
        file = open('./data/info.txt','r')
    except:
        return render_template('userList.html',msg='저장된 정보가 없습니다')
    else:
        for aline in file.readlines():
            list = aline.split('/')
            name=list[0]
            info=list[1].strip()
            infolist = info.split(',')
            num=infolist[0]
            pwd=infolist[1]
            dict[num]=pwd
        file.close()
    return render_template('userList.html',name=name,dict=dict)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8080, debug=True) 