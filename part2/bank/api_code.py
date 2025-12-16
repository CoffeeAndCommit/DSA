from fastapi import FastAPI, HTTPException

app = FastAPI()
bank = Bank()

@app.post("/account/create")
def create_account(acc_no: int, name: str, pin: str, acc_type: str):
    if acc_type == "savings":
        acc = SavingsAccount(acc_no, name, pin)
    else:
        acc = CurrentAccount(acc_no, name, pin)

    bank.create_account(acc)
    return {"message": "Account created"}


@app.post("/account/deposit")
def deposit(acc_no: int, pin: str, amount: float):
    acc = bank.get_account(acc_no)
    if not acc or not acc.authenticate(pin):
        raise HTTPException(status_code=401, detail="Unauthorized")

    acc.deposit(amount)
    return {"balance": acc.balance}


@app.post("/account/withdraw")
def withdraw(acc_no: int, pin: str, amount: float):
    acc = bank.get_account(acc_no)
    if not acc or not acc.authenticate(pin):
        raise HTTPException(status_code=401, detail="Unauthorized")

    acc.withdraw(amount)
    return {"balance": acc.balance}


@app.get("/account/transactions")
def transactions(acc_no: int, pin: str):
    acc = bank.get_account(acc_no)
    if not acc or not acc.authenticate(pin):
        raise HTTPException(status_code=401, detail="Unauthorized")

    return acc.transactions
