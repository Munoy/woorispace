from typing import Any

from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect
from openpyxl import load_workbook
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

    load_wb = load_workbook("WS/static/price.xlsx", data_only=True)
    load_ws = load_wb['2022.02.04']

    if (params['type'] == '9'):
        column = 'C'
    elif (params['type'] == '8'):
        column = 'D'
    elif (params['type'] == '7'):
        column = 'E'
    elif (params['type'] == '6'):
        column = 'F'
    elif (params['type'] == '5'):
        column = 'G'
    elif (params['type'] == '4'):
        column = 'H'
    elif (params['type'] == '3'):
        column = 'I'
    elif (params['type'] == '2'):
        column = 'J'
    elif (params['type'] == '1'):
        column = 'K'

    if (cstrt_cost < 50000000):
        min_row = '5'
        max_row = '5'
        cstrt_cost_min = 1
        cstrt_cost_max = 50000000
    elif (cstrt_cost < ug):  # 1억원 ======================
        min_row = '5'
        max_row = '6'
        cstrt_cost_min = 50000000
        cstrt_cost_max = ug
    elif (cstrt_cost < ug * 2):  # 2억원 ======================
        min_row = '6'
        max_row = '7'
        cstrt_cost_min = ug
        cstrt_cost_max = ug * 2
    elif (cstrt_cost < ug * 3):  # 3억원 ======================
        min_row = '7'
        max_row = '8'
        cstrt_cost_min = ug * 2
        cstrt_cost_max = ug * 3
    elif (cstrt_cost < ug * 5):  # 5억원 ======================
        min_row = '8'
        max_row = '9'
        cstrt_cost_min = ug * 3
        cstrt_cost_max = ug * 5
    elif (cstrt_cost < ug * 10):  # 10억원 ======================
        min_row = '9'
        max_row = '10'
        cstrt_cost_min = ug * 5
        cstrt_cost_max = ug * 10
    elif (cstrt_cost < ug * 20):  # 20억원 ======================
        min_row = '10'
        max_row = '11'
        cstrt_cost_min = ug * 10
        cstrt_cost_max = ug * 20
    elif (cstrt_cost < ug * 30):  # 30억원 ======================
        min_row = '11'
        max_row = '12'
        cstrt_cost_min = ug * 20
        cstrt_cost_max = ug * 30
    elif (cstrt_cost < ug * 50):  # 50억원 ======================
        min_row = '12'
        max_row = '13'
        cstrt_cost_min = ug * 30
        cstrt_cost_max = ug * 50
    elif (cstrt_cost < ug * 100):  # 100억원 ======================
        min_row = '13'
        max_row = '14'
        cstrt_cost_min = ug * 50
        cstrt_cost_max = ug * 100
    elif (cstrt_cost < ug * 200):  # 200억원 ======================
        min_row = '14'
        max_row = '15'
        cstrt_cost_min = ug * 100
        cstrt_cost_max = ug * 200
    elif (cstrt_cost < ug * 300):  # 300억원 ======================
        min_row = '15'
        max_row = '16'
        cstrt_cost_min = ug * 200
        cstrt_cost_max = ug * 300
    elif (cstrt_cost < ug * 500):  # 500억원 ======================
        min_row = '16'
        max_row = '17'
        cstrt_cost_min = ug * 300
        cstrt_cost_max = ug * 500
    elif (cstrt_cost < ug * 1000):  # 1000억원 ======================
        min_row = '17'
        max_row = '18'
        cstrt_cost_min = ug * 500
        cstrt_cost_max = ug * 1000
    elif (cstrt_cost < ug * 2000):  # 2000억원 ======================
        min_row = '18'
        max_row = '19'
        cstrt_cost_min = ug * 1000
        cstrt_cost_max = ug * 2000
    elif (cstrt_cost < ug * 3000):  # 3000억원 ======================
        min_row = '19'
        max_row = '20'
        cstrt_cost_min = ug * 2000
        cstrt_cost_max = ug * 3000
    elif (cstrt_cost < ug * 5000):  # 5000억원 ======================
        min_row = '20'
        max_row = '21'
        cstrt_cost_min = ug * 3000
        cstrt_cost_max = ug * 5000
    else:  # 5000억원 이상 ======================
        () # 24

    type_rate_min = load_ws[column + min_row].value
    type_rate_max = load_ws[column + max_row].value

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
