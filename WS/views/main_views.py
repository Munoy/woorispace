from typing import Any

from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.utils import redirect
import json
import math

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return redirect(url_for('main.estimate'))

@bp.route('/estimate')
def estimate():
    return render_template('main.html')

@bp.route('/cal', methods=['POST'])
def cal():
    train_tes = []
    value = dict(request.form)
    param = json.dumps(value)
    print("param = " + param)
    params = json.loads(param)

    print("use = " + params['use'])     #용도
    print("area = " + params['area'])   #면적
    print("type = " + params['type'])   #종별
    print("cor = " + params['cor'])     #보정 요율

    ug = 100000000

    use1 = 1564630
    use2 = 1902800
    use3 = 1639088
    use4 = 1651588
    use5 = 1567446
    use6 = 699500
    use7 = 867125
    use8 = 1680755
    use9 = 1641879



    if params['use'] == "아파트":
        use_cost = use1
        cstrt_cost = use_cost * float(params['area'])
    elif params['use'] == "연립주택":
        use_cost = use2
        cstrt_cost = use_cost * float(params['area'])
    elif params['use'] == "다세대주택":
        use_cost = use3
        cstrt_cost = use_cost * float(params['area'])
    elif params['use'] == "다가구주택":
        use_cost = use4
        cstrt_cost = use_cost * float(params['area'])
    elif params['use'] == "근린생활시설":
        use_cost = use5
        cstrt_cost = use_cost * float(params['area'])
    elif params['use'] == "창고":
        use_cost = use6
        cstrt_cost = use_cost * float(params['area'])
    elif params['use'] == "공장":
        use_cost = use7
        cstrt_cost = use_cost * float(params['area'])
    elif params['use'] == "다중주택":
        use_cost = use8
        cstrt_cost = use_cost * float(params['area'])
    elif params['use'] == "오피스텔":
        use_cost = use9
        cstrt_cost = use_cost * float(params['area'])

    if(cstrt_cost < 50000000): #5000만원 이하
        cstrt_cost_min = 1
        cstrt_cost_max = 50000000
        if(params['type'] == '1'):
            type_rate_min =6.81
            type_rate_max =6.81
        elif(params['type'] == '2'):
            type_rate_min =8.51
            type_rate_max =8.51
        elif(params['type'] == '3'):
            type_rate_min =10.22
            type_rate_max =10.22
        elif(params['type'] == '4'):
            type_rate_min =7.61
            type_rate_max =7.61
        elif(params['type'] == '5'):
            type_rate_min =9.51
            type_rate_max =9.51
        elif(params['type'] == '6'):
            type_rate_min =11.41
            type_rate_max =11.41
        elif(params['type'] == '7'):
            type_rate_min =8.36
            type_rate_max =8.36
        elif(params['type'] == '8'):
            type_rate_min =10.46
            type_rate_max =10.46
        elif(params['type'] == '9'):
            type_rate_min =12.55
            type_rate_max =12.55
    elif(cstrt_cost < ug):  # 1억원 ======================
        cstrt_cost_min = 50000000
        cstrt_cost_max = ug
        if (params['type'] == '1'):
            type_rate_min =6.81
            type_rate_max =6.25
        elif (params['type'] == '2'):
            type_rate_min =8.51
            type_rate_max =7.82
        elif (params['type'] == '3'):
            type_rate_min =10.22
            type_rate_max =9.38
        elif (params['type'] == '4'):
            type_rate_min =7.61
            type_rate_max =6.95
        elif (params['type'] == '5'):
            type_rate_min =9.51
            type_rate_max =8.69
        elif (params['type'] == '6'):
            type_rate_min =11.41
            type_rate_max =10.43
        elif (params['type'] == '7'):
            type_rate_min =8.36
            type_rate_max =7.65
        elif (params['type'] == '8'):
            type_rate_min =10.46
            type_rate_max =9.56
        elif (params['type'] == '9'):
            type_rate_min =12.55
            type_rate_max =11.48
    elif (cstrt_cost < ug * 2): # 2억원 ======================
        cstrt_cost_min =ug
        cstrt_cost_max =ug * 2
        if (params['type'] == '1'):
            type_rate_min =6.25
            type_rate_max =5.44
        elif (params['type'] == '2'):
            type_rate_min =7.82
            type_rate_max =6.8
        elif (params['type'] == '3'):
            type_rate_min =9.38
            type_rate_max =8.16
        elif (params['type'] == '4'):
            type_rate_min =6.95
            type_rate_max =6.05
        elif (params['type'] == '5'):
            type_rate_min =8.69
            type_rate_max =7.57
        elif (params['type'] == '6'):
            type_rate_min =10.43
            type_rate_max =9.08
        elif (params['type'] == '7'):
            type_rate_min =7.65
            type_rate_max =6.66
        elif (params['type'] == '8'):
            type_rate_min =9.56
            type_rate_max =8.33
        elif (params['type'] == '9'):
            type_rate_min =11.48
            type_rate_max =9.99
    elif (cstrt_cost < ug * 3): # 3억원 ======================
        cstrt_cost_min =ug * 2
        cstrt_cost_max =ug * 3
        if (params['type'] == '1'):
            type_rate_min =5.44
            type_rate_max =4.72
        elif (params['type'] == '2'):
            type_rate_min =6.8
            type_rate_max =5.9
        elif (params['type'] == '3'):
            type_rate_min =8.16
            type_rate_max =7.08
        elif (params['type'] == '4'):
            type_rate_min =6.05
            type_rate_max =5.26
        elif (params['type'] == '5'):
            type_rate_min =7.57
            type_rate_max =6.57
        elif (params['type'] == '6'):
            type_rate_min =9.08
            type_rate_max =7.88
        elif (params['type'] == '7'):
            type_rate_min =6.66
            type_rate_max =5.78
        elif (params['type'] == '8'):
            type_rate_min =8.33
            type_rate_max =7.23
        elif (params['type'] == '9'):
            type_rate_min =9.99
            type_rate_max =8.68
    elif (cstrt_cost < ug * 5): # 5억원 ======================
        cstrt_cost_min =ug * 3
        cstrt_cost_max =ug * 5
        if (params['type'] == '1'):
            type_rate_min =4.72
            type_rate_max =4.3
        elif (params['type'] == '2'):
            type_rate_min =5.9
            type_rate_max =5.38
        elif (params['type'] == '3'):
            type_rate_min =7.08
            type_rate_max =6.46
        elif (params['type'] == '4'):
            type_rate_min =5.26
            type_rate_max =4.79
        elif (params['type'] == '5'):
            type_rate_min =6.57
            type_rate_max =5.98
        elif (params['type'] == '6'):
            type_rate_min =7.88
            type_rate_max =7.18
        elif (params['type'] == '7'):
            type_rate_min =5.78
            type_rate_max =5.26
        elif (params['type'] == '8'):
            type_rate_min =7.23
            type_rate_max =6.58
        elif (params['type'] == '9'):
            type_rate_min =8.68
            type_rate_max =7.9
    elif (cstrt_cost < ug * 10): # 10억원 ======================
        cstrt_cost_min =ug * 5
        cstrt_cost_max =ug * 10
        if (params['type'] == '1'):
            type_rate_min =4.3
            type_rate_max =3.83
        elif (params['type'] == '2'):
            type_rate_min =5.38
            type_rate_max =4.79
        elif (params['type'] == '3'):
            type_rate_min =6.46
            type_rate_max =5.75
        elif (params['type'] == '4'):
            type_rate_min =4.79
            type_rate_max =4.26
        elif (params['type'] == '5'):
            type_rate_min =5.98
            type_rate_max =5.32
        elif (params['type'] == '6'):
            type_rate_min =7.18
            type_rate_max =6.39
        elif (params['type'] == '7'):
            type_rate_min =5.26
            type_rate_max =4.68
        elif (params['type'] == '8'):
            type_rate_min =6.58
            type_rate_max =5.86
        elif (params['type'] == '9'):
            type_rate_min =7.9
            type_rate_max =7.03
    elif (cstrt_cost < ug * 20): # 20억원 ======================
        cstrt_cost_min =ug * 10
        cstrt_cost_max =ug * 20
        if (params['type'] == '1'):
            type_rate_min =3.83
            type_rate_max =3.4
        elif (params['type'] == '2'):
            type_rate_min =4.79
            type_rate_max =4.24
        elif (params['type'] == '3'):
            type_rate_min =5.75
            type_rate_max =5.09
        elif (params['type'] == '4'):
            type_rate_min =4.26
            type_rate_max =3.77
        elif (params['type'] == '5'):
            type_rate_min =5.32
            type_rate_max =4.72
        elif (params['type'] == '6'):
            type_rate_min =6.39
            type_rate_max =5.66
        elif (params['type'] == '7'):
            type_rate_min =4.68
            type_rate_max =4.15
        elif (params['type'] == '8'):
            type_rate_min =5.86
            type_rate_max =5.19
        elif (params['type'] == '9'):
            type_rate_min =7.03
            type_rate_max =6.22
    elif (cstrt_cost < ug * 30): # 30억원 ======================
        cstrt_cost_min =ug * 20
        cstrt_cost_max =ug * 30
        if (params['type'] == '1'):
            type_rate_min =3.4
            type_rate_max =3.23
        elif (params['type'] == '2'):
            type_rate_min =4.24
            type_rate_max =4.03
        elif (params['type'] == '3'):
            type_rate_min =5.09
            type_rate_max =4.84
        elif (params['type'] == '4'):
            type_rate_min =3.77
            type_rate_max =3.58
        elif (params['type'] == '5'):
            type_rate_min =4.72
            type_rate_max =4.48
        elif (params['type'] == '6'):
            type_rate_min =5.66
            type_rate_max =5.38
        elif (params['type'] == '7'):
            type_rate_min =4.15
            type_rate_max =3.94
        elif (params['type'] == '8'):
            type_rate_min =5.19
            type_rate_max =4.93
        elif (params['type'] == '9'):
            type_rate_min =6.22
            type_rate_max =5.91
    elif (cstrt_cost < ug * 50): # 50억원 ======================
        cstrt_cost_min =ug * 30
        cstrt_cost_max =ug * 50
        if (params['type'] == '1'):
            type_rate_min =3.23
            type_rate_max =3.12
        elif (params['type'] == '2'):
            type_rate_min =4.03
            type_rate_max =3.9
        elif (params['type'] == '3'):
            type_rate_min =4.84
            type_rate_max =4.68
        elif (params['type'] == '4'):
            type_rate_min =3.58
            type_rate_max =3.46
        elif (params['type'] == '5'):
            type_rate_min =4.48
            type_rate_max =4.33
        elif (params['type'] == '6'):
            type_rate_min =5.38
            type_rate_max =5.2
        elif (params['type'] == '7'):
            type_rate_min =3.94
            type_rate_max =3.81
        elif (params['type'] == '8'):
            type_rate_min =4.93
            type_rate_max =4.76
        elif (params['type'] == '9'):
            type_rate_min =5.91
            type_rate_max =5.72
    elif (cstrt_cost < ug * 100): # 100억원 ======================
        cstrt_cost_min =ug * 50
        cstrt_cost_max =ug * 100
        if (params['type'] == '1'):
            type_rate_min =3.12
            type_rate_max =3.04
        elif (params['type'] == '2'):
            type_rate_min =3.9
            type_rate_max =3.8
        elif (params['type'] == '3'):
            type_rate_min =4.68
            type_rate_max =4.56
        elif (params['type'] == '4'):
            type_rate_min =3.46
            type_rate_max =3.38
        elif (params['type'] == '5'):
            type_rate_min =4.33
            type_rate_max =4.22
        elif (params['type'] == '6'):
            type_rate_min =5.2
            type_rate_max =5.07
        elif (params['type'] == '7'):
            type_rate_min =3.81
            type_rate_max =3.72
        elif (params['type'] == '8'):
            type_rate_min =4.76
            type_rate_max =4.65
        elif (params['type'] == '9'):
            type_rate_min =5.72
            type_rate_max =5.58
    elif (cstrt_cost < ug * 200): # 200억원 ======================
        cstrt_cost_min =ug * 100
        cstrt_cost_max =ug * 200
        if (params['type'] == '1'):
            type_rate_min =3.04
            type_rate_max =2.96
        elif (params['type'] == '2'):
            type_rate_min =3.8
            type_rate_max =3.69
        elif (params['type'] == '3'):
            type_rate_min =4.56
            type_rate_max =4.43
        elif (params['type'] == '4'):
            type_rate_min =3.38
            type_rate_max =3.28
        elif (params['type'] == '5'):
            type_rate_min =4.22
            type_rate_max =4.1
        elif (params['type'] == '6'):
            type_rate_min =5.07
            type_rate_max =4.92
        elif (params['type'] == '7'):
            type_rate_min =3.72
            type_rate_max =3.61
        elif (params['type'] == '8'):
            type_rate_min =4.65
            type_rate_max =4.51
        elif (params['type'] == '9'):
            type_rate_min =5.58
            type_rate_max =5.42
    elif (cstrt_cost < ug * 300): # 300억원 ======================
        cstrt_cost_min =ug * 200
        cstrt_cost_max =ug * 300
        if (params['type'] == '1'):
            type_rate_min =2.96
            type_rate_max =2.91
        elif (params['type'] == '2'):
            type_rate_min =3.69
            type_rate_max =3.63
        elif (params['type'] == '3'):
            type_rate_min =4.43
            type_rate_max =4.36
        elif (params['type'] == '4'):
            type_rate_min =3.28
            type_rate_max =3.23
        elif (params['type'] == '5'):
            type_rate_min =4.1
            type_rate_max =4.03
        elif (params['type'] == '6'):
            type_rate_min =4.92
            type_rate_max =4.84
        elif (params['type'] == '7'):
            type_rate_min =3.61
            type_rate_max =3.55
        elif (params['type'] == '8'):
            type_rate_min =4.51
            type_rate_max =4.44
        elif (params['type'] == '9'):
            type_rate_min =5.42
            type_rate_max =5.32
    elif (cstrt_cost < ug * 500): # 500억원 ======================
        cstrt_cost_min =ug * 300
        cstrt_cost_max =ug * 500
        if (params['type'] == '1'):
            type_rate_min =2.91
            type_rate_max =2.87
        elif (params['type'] == '2'):
            type_rate_min =3.63
            type_rate_max =3.58
        elif (params['type'] == '3'):
            type_rate_min =4.36
            type_rate_max =4.3
        elif (params['type'] == '4'):
            type_rate_min =3.23
            type_rate_max =3.18
        elif (params['type'] == '5'):
            type_rate_min =4.03
            type_rate_max =3.98
        elif (params['type'] == '6'):
            type_rate_min =4.84
            type_rate_max =4.77
        elif (params['type'] == '7'):
            type_rate_min =3.55
            type_rate_max =3.5
        elif (params['type'] == '8'):
            type_rate_min =4.44
            type_rate_max =4.38
        elif (params['type'] == '9'):
            type_rate_min =5.32
            type_rate_max =5.25
    elif (cstrt_cost < ug * 1000): # 1000억원 ======================
        cstrt_cost_min =ug * 500
        cstrt_cost_max =ug * 1000
        if (params['type'] == '1'):
            type_rate_min =2.87
            type_rate_max =2.8
        elif (params['type'] == '2'):
            type_rate_min =3.58
            type_rate_max =3.5
        elif (params['type'] == '3'):
            type_rate_min =4.3
            type_rate_max =4.21
        elif (params['type'] == '4'):
            type_rate_min =3.18
            type_rate_max =3.12
        elif (params['type'] == '5'):
            type_rate_min =3.98
            type_rate_max =3.9
        elif (params['type'] == '6'):
            type_rate_min =4.77
            type_rate_max =4.68
        elif (params['type'] == '7'):
            type_rate_min =3.5
            type_rate_max =3.43
        elif (params['type'] == '8'):
            type_rate_min =4.38
            type_rate_max =4.29
        elif (params['type'] == '9'):
            type_rate_min =5.25
            type_rate_max =5.14
    elif (cstrt_cost < ug * 2000):  # 2000억원 ======================
        cstrt_cost_min =ug * 1000
        cstrt_cost_max =ug * 2000
        if (params['type'] == '1'):
            type_rate_min =2.8
            type_rate_max =2.76
        elif (params['type'] == '2'):
            type_rate_min =3.5
            type_rate_max =3.45
        elif (params['type'] == '3'):
            type_rate_min =4.21
            type_rate_max =4.14
        elif (params['type'] == '4'):
            type_rate_min =3.12
            type_rate_max =3.07
        elif (params['type'] == '5'):
            type_rate_min =3.9
            type_rate_max =3.84
        elif (params['type'] == '6'):
            type_rate_min =4.68
            type_rate_max =4.6
        elif (params['type'] == '7'):
            type_rate_min =3.43
            type_rate_max =3.38
        elif (params['type'] == '8'):
            type_rate_min =4.29
            type_rate_max =4.22
        elif (params['type'] == '9'):
            type_rate_min =5.14
            type_rate_max =5.06
    elif (cstrt_cost < ug * 3000):  # 3000억원 ======================
        cstrt_cost_min =ug * 2000
        cstrt_cost_max =ug * 3000
        if (params['type'] == '1'):
            type_rate_min =2.76
            type_rate_max =2.73
        elif (params['type'] == '2'):
            type_rate_min =3.45
            type_rate_max =3.42
        elif (params['type'] == '3'):
            type_rate_min =4.14
            type_rate_max =4.1
        elif (params['type'] == '4'):
            type_rate_min =3.07
            type_rate_max =3.03
        elif (params['type'] == '5'):
            type_rate_min =3.84
            type_rate_max =3.79
        elif (params['type'] == '6'):
            type_rate_min =4.6
            type_rate_max =4.55
        elif (params['type'] == '7'):
            type_rate_min =3.38
            type_rate_max =3.34
        elif (params['type'] == '8'):
            type_rate_min =4.22
            type_rate_max =4.17
        elif (params['type'] == '9'):
            type_rate_min =5.06
            type_rate_max =5.01
    elif (cstrt_cost < ug * 5000):  # 5000억원 ======================
        cstrt_cost_min =ug * 3000
        cstrt_cost_max =ug * 5000
        if (params['type'] == '1'):
            type_rate_min =2.73
            type_rate_max =2.69
        elif (params['type'] == '2'):
            type_rate_min =3.42
            type_rate_max =3.36
        elif (params['type'] == '3'):
            type_rate_min =4.1
            type_rate_max =4.03
        elif (params['type'] == '4'):
            type_rate_min =3.03
            type_rate_max =2.99
        elif (params['type'] == '5'):
            type_rate_min =3.79
            type_rate_max =3.73
        elif (params['type'] == '6'):
            type_rate_min =4.55
            type_rate_max =4.48
        elif (params['type'] == '7'):
            type_rate_min =3.34
            type_rate_max =3.28
        elif (params['type'] == '8'):
            type_rate_min =4.17
            type_rate_max =4.11
        elif (params['type'] == '9'):
            type_rate_min =5.01
            type_rate_max =4.93
    else:  # 5000억원 이상 ======================
        () # 24


    denominator1 = cstrt_cost_max - cstrt_cost_min
    numerator1 = (cstrt_cost - cstrt_cost_min) * (type_rate_min - type_rate_max)
    rate_result = type_rate_min - (numerator1/denominator1)

    rate_result = round(rate_result, 5)
    cor_result = rate_result * float(params['cor'])
    cor_result = round(cor_result, 5)
    cs_cost = cstrt_cost * (cor_result * 0.01)
    cs_cost = round(cs_cost, 0)
    cs_cost2 = round(cs_cost, -3)
    cstrt_cost = math.trunc(cstrt_cost)
    d = {
        "cstrt_cost_min": cstrt_cost_min,
        "cstrt_cost_max": cstrt_cost_max,
        "type_rate_min": type_rate_min,
        "type_rate_max": type_rate_max,
        "rate_result": rate_result,
        "cor_result": cor_result,
        "cs_cost": cs_cost,
        "cs_cost2": cs_cost2,
        "use_cost": use_cost,
        "cstrt_cost": cstrt_cost
    }
    data = json.dumps(d)
    print(str(data))
    return json.dumps(d)
