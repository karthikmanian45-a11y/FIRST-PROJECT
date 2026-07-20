from flask import Flask,render_template,request,jsonify
from bank import Bank
from main import Account
from current import CurrentAccount
from savings import SavingsAccount
import os

app=Flask(__name__)
B=Bank()

@app.route("/")
def home():
    return "WELCOME TO MY BANK ACCOUNT PROJECT"

@app.route("/deposit",methods=["GET","POST"])
def depo():
    if request.method == "POST":
        req=request.get_json()
        a=B.find_acc(req["acc_no"])
        a.deposit(req["amount"])
        return "Deposited successfully"


@app.route("/withdraw",methods=["GET","POST"])
def withd():
    if request.method=="POST":
        req=request.get_json()
        a=B.find_acc(req["acc_no"])
        a.withdraw(req["amount"])
        return "Withdrawn successfull"

@app.route("/balance",methods=["GET","POST"])
def balance():
    if request.method=="POST":
        req=request.get_json()
        a=B.find_acc(req["acc_no"])
        return str(a.show_balance)

@app.route("/accounts")
def accounts():
        return str(B.show_acc())

@app.route("/add_acc",methods=["GET","POST"])
def ad_acc():
        if request.method=="POST":
             req=request.get_json()
             a=CurrentAccount(req["acc_no"],req["name"])
             B.add_acc(a)
             return "Account added successfully"

@app.route("/remove_acc",methods=["GET","POST"])
def rem_acc():
        if request.method=="POST":
             req=request.get_json()
             B.remove_acc(req["acc_no"])
             return "Account removed successfully"

@app.route("/find_acc",methods=["GET","POST"])
def fin_acc():
        if request.method=="POST":
             req=request.get_json()
             return str(B.find_acc(req["acc_no"]))
        raise ValueError("This account is not in this bank")

@app.route("/interest",methods=["GET","POST"])
def saving():
     if request.method=="POST":
          req=request.get_json()
          a=B.find_acc(req["acc_no"])
          return str(a.calculate_interest())
@app.route("/is_valid_amount",methods=["GET","POST"])
def valid():
     if request.method=="POST":
          req=request.get_json()
          return str(B.is_valid_amount(req["amount"]))
@app.route("/total_accounts")
def acc():
     return str(B.total_accounts())



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))