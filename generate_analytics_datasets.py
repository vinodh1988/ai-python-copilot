import csv, math, random
from datetime import date, datetime, timedelta
from pathlib import Path

N, SEED = 10_000, 20260928
OUT = Path(__file__).parent / "datasets"
R = random.Random(SEED)

def w(items, weights): return R.choices(items, weights=weights, k=1)[0]
def day(a=date(2024,1,1), b=date(2025,12,31)): return (a + timedelta(days=R.randint(0,(b-a).days))).isoformat()
def yn(p): return "Yes" if R.random() < p else "No"
def save(name, rows):
    OUT.mkdir(exist_ok=True)
    with (OUT/name).open("w", newline="", encoding="utf-8") as f:
        x=csv.DictWriter(f, fieldnames=list(rows[0])); x.writeheader(); x.writerows(rows)
    print(f"{name}: {len(rows):,} records")

def sales():
    products={
      "Electronics":[("Wireless Headphones",79),("Smart Watch",149),("Bluetooth Speaker",59)],
      "Home":[("Air Fryer",119),("Desk Lamp",39),("Coffee Maker",89)],
      "Clothing":[("Running Shoes",74),("Winter Jacket",129),("Casual Shirt",42)],
      "Sports":[("Yoga Mat",32),("Dumbbell Set",95),("Fitness Band",55)]}
    rows=[]
    for i in range(1,N+1):
        cat=w(list(products),[32,27,24,17]); product,base=R.choice(products[cat])
        units=w([1,2,3,4,5,6],[40,27,16,9,5,3]); price=round(base*R.uniform(.92,1.1),2)
        discount=w([0,5,10,15,20,25],[25,20,24,16,10,5])
        revenue=round(units*price*(1-discount/100),2); cost=round(units*price*R.uniform(.52,.76),2)
        rows.append({"order_id":f"ORD-{i:06d}","order_date":day(),
          "region":w(["North","South","East","West","Central"],[20,24,21,22,13]),
          "category":cat,"product":product,
          "sales_channel":w(["Online","Retail Store","Marketplace"],[48,34,18]),
          "customer_segment":w(["Consumer","Corporate","Small Business"],[62,18,20]),
          "units_sold":units,"unit_price":price,"discount_pct":discount,"revenue":revenue,
          "cost":cost,"profit":round(revenue-cost,2),
          "payment_method":w(["Card","UPI","Wallet","Bank Transfer","Cash"],[33,30,14,13,10]),
          "returned":yn(.035+(.035 if cat=="Clothing" else 0)+discount/1000)})
    save("01_retail_sales.csv",rows)

def churn():
    rows=[]; ref=date(2025,12,31)
    for i in range(1,N+1):
        tenure=R.randint(1,72); signup=ref-timedelta(days=tenure*30+R.randint(0,29))
        plan=w(["Basic","Standard","Premium"],[45,37,18]); charge=round({"Basic":24,"Standard":49,"Premium":79}[plan]+R.uniform(-4,12),2)
        sat=w([1,2,3,4,5],[7,13,28,34,18]); tickets=min(12,int(R.expovariate(.55)))
        late=min(10,int(R.expovariate(.8))); contract=w(["Monthly","Annual","Two Year"],[52,32,16]); autopay=yn(.61)
        risk=-2+.55*(contract=="Monthly")+.24*tickets+.2*late+.65*(sat<=2)-.018*tenure-.35*(autopay=="Yes")
        p=1/(1+math.exp(-risk))
        rows.append({"customer_id":f"CUS-{i:06d}","signup_date":signup.isoformat(),"age":R.randint(18,78),
          "region":w(["Urban","Suburban","Rural"],[51,31,18]),"plan":plan,"tenure_months":tenure,
          "monthly_charges":charge,"total_charges":round(charge*tenure*R.uniform(.96,1.02),2),
          "support_tickets_last_year":tickets,"avg_monthly_usage_hours":round(max(1,R.gauss(38+6*(plan!="Basic"),14)),1),
          "contract_type":contract,"autopay":autopay,"satisfaction_score":sat,
          "late_payments_last_year":late,"churned":yn(p)})
    save("02_customer_churn.csv",rows)

def supply():
    rows=[]; suppliers=["Apex Components","BlueRiver Goods","Crest Manufacturing","Delta Supply","Evergreen Parts"]
    scores=dict(zip(suppliers,[4.7,4.3,3.8,4.1,3.5]))
    for i in range(1,N+1):
        supplier=w(suppliers,[22,25,18,21,14]); rating=round(max(1,min(5,R.gauss(scores[supplier],.25))),1)
        mode=w(["Road","Rail","Air","Sea"],[48,19,13,20]); planned={"Road":5,"Rail":8,"Air":2,"Sea":18}[mode]+R.randint(0,3)
        tendency=(4.5-rating)*1.8+{"Road":1,"Rail":1.5,"Air":.3,"Sea":2.5}[mode]
        actual=max(1,round(R.gauss(planned+tendency-1.2,2.2))); qty=R.randint(25,1500); dist=R.randint(80,3200)
        stock=min(.65,.03+max(0,actual-planned)*.035+(qty>1200)*.05)
        rows.append({"shipment_id":f"SHP-{i:06d}","order_date":day(),"supplier":supplier,
          "origin_warehouse":R.choice(["WH-North","WH-South","WH-East","WH-West"]),
          "destination_region":R.choice(["North","South","East","West","Central"]),
          "product_category":R.choice(["Raw Material","Electronics","Packaging","Mechanical Parts","Finished Goods"]),
          "quantity":qty,"shipping_mode":mode,"distance_km":dist,"planned_lead_days":planned,"actual_lead_days":actual,
          "freight_cost":round(120+qty*R.uniform(.18,.55)+dist*R.uniform(.08,.32),2),
          "defect_rate_pct":round(max(0,R.gauss((5.2-rating)*1.4,.7)),2),
          "on_time":"Yes" if actual<=planned else "No","stockout":yn(stock),"supplier_rating":rating})
    save("03_supply_chain.csv",rows)

def hr():
    roles={"Engineering":["Software Engineer","Data Analyst","QA Engineer"],
      "Sales":["Sales Executive","Account Manager","Sales Analyst"],
      "Finance":["Financial Analyst","Accountant","Auditor"],
      "Operations":["Operations Analyst","Process Manager","Coordinator"],
      "Human Resources":["HR Specialist","Recruiter","HR Manager"]}
    rows=[]
    for i in range(1,N+1):
        dept=w(list(roles),[31,23,15,21,10]); years=R.randint(0,25); overtime=yn(.31)
        sat=w([1,2,3,4,5],[8,15,29,31,17]); income=max(2200,2800+years*310+R.gauss(0,1100)+(dept=="Engineering")*900)
        absent=max(0,round(R.gauss(5+(sat<=2)*4,3))); promoted=yn(min(.65,.08+years*.018))
        risk=-2.45+.95*(overtime=="Yes")+.75*(sat<=2)+.045*absent+.55*(years<2)-.42*(promoted=="Yes")
        rows.append({"employee_id":f"EMP-{i:06d}","department":dept,"job_role":R.choice(roles[dept]),
          "age":R.randint(max(20,21+years),min(65,40+years)),
          "gender":w(["Female","Male","Non-binary"],[47,51,2]),
          "education_level":w(["High School","Diploma","Bachelor","Master","Doctorate"],[8,15,48,26,3]),
          "years_at_company":years,"monthly_income":round(income,2),"overtime":overtime,
          "remote_work_days_per_week":w([0,1,2,3,4,5],[21,14,31,23,7,4]),
          "training_hours_last_year":R.randint(0,80),"performance_rating":w([1,2,3,4,5],[2,9,48,34,7]),
          "job_satisfaction":sat,"absenteeism_days":absent,"promoted_last_2_years":promoted,
          "attrition":yn(1/(1+math.exp(-risk)))})
    save("04_hr_attrition.csv",rows)

def marketing():
    rows=[]; channels=["Email","Social Media","Search Ads","Display Ads","SMS"]
    base={"Email":.055,"Social Media":.026,"Search Ads":.041,"Display Ads":.012,"SMS":.075}
    cpm={"Email":2.5,"Social Media":8,"Search Ads":14,"Display Ads":6,"SMS":4.5}
    for i in range(1,N+1):
        channel=w(channels,[28,24,22,16,10]); impressions=R.randint(800,50000)
        clicks=min(impressions,round(impressions*max(.003,R.gauss(base[channel],base[channel]*.28))))
        cp=max(.01,R.gauss(.075 if channel in ["Email","SMS"] else .048,.015))
        conversions=min(clicks,round(clicks*cp)); spend=round(impressions/1000*cpm[channel]*R.uniform(.85,1.2),2)
        revenue=round(conversions*R.uniform(35,145),2)
        rows.append({"campaign_record_id":f"CAM-{i:06d}","activity_date":day(),
          "campaign_name":R.choice(["New Year Sale","Summer Savings","Festival Offers","Product Launch","Loyalty Rewards"]),
          "channel":channel,"region":R.choice(["North","South","East","West","Central"]),
          "audience_segment":w(["New Customers","Returning Customers","High Value","Inactive"],[32,36,17,15]),
          "device":w(["Mobile","Desktop","Tablet"],[63,31,6]),"impressions":impressions,"clicks":clicks,
          "conversions":conversions,"spend":spend,"revenue":revenue,
          "ctr_pct":round(clicks/impressions*100,2),
          "conversion_rate_pct":round(conversions/clicks*100,2) if clicks else 0,
          "roas":round(revenue/spend,2) if spend else 0})
    save("05_marketing_campaigns.csv",rows)

def maintenance():
    rows=[]; start=datetime(2025,1,1)
    for i in range(1,N+1):
        mtype=w(["CNC","Compressor","Pump","Conveyor"],[28,21,27,24]); hours=R.randint(50,35000); days=R.randint(0,240)
        temp=R.gauss(68,9)+days*.035; vibration=max(.2,R.gauss(2.7,.8)+days*.008)
        errors=max(0,round(R.gauss(.8+days/90,1.4)))
        risk=-6.4+.075*(temp-65)+.65*(vibration-2.5)+.015*days+.36*errors+.000025*hours
        p=1/(1+math.exp(-risk)); mp=min(.96,p*2.4+.08*(days>120))
        rows.append({"sensor_record_id":f"SNS-{i:06d}","timestamp":(start+timedelta(minutes=30*i)).isoformat(sep=" "),
          "machine_id":f"M-{R.randint(1,250):04d}","machine_type":mtype,"plant":R.choice(["Plant-A","Plant-B","Plant-C","Plant-D"]),
          "temperature_c":round(temp,2),"vibration_mm_s":round(vibration,2),
          "pressure_bar":round(max(1,R.gauss(6.2,1.1)),2),"rotational_speed_rpm":max(300,round(R.gauss(1450,240))),
          "operating_hours":hours,"days_since_maintenance":days,"error_count_24h":errors,
          "energy_consumption_kwh":round(max(5,R.gauss(52,13)+temp*.15),2),
          "maintenance_required":yn(mp),"failure_within_7_days":yn(p)})
    save("06_predictive_maintenance.csv",rows)

if __name__=="__main__":
    sales(); churn(); supply(); hr(); marketing(); maintenance()
