class InMemoryDB:
    def __init__(self):
        self.main_dataStore = {}  # The main data store for committed data
        self.temp_store = None  #temp
        self.transactionStatus= False  # sees/track transaction is active

    def begin_transaction(self):
        if self.transactionStatus:
            raise Exception("Transaction already in progress.")
        self.temp_store = {}
        self.transactionStatus = True

    def put(self, key, value):
        if not self.transactionStatus:
            raise Exception("No transaction in progress.")
        self.temp_store[key] = value

    def get(self, key):
        # only return values from the main_dataStore 
        if self.transactionStatus:
            return self.main_dataStore.get(key)
        return self.main_dataStore.get(key)

    def commit(self):
        if not self.transactionStatus:
            raise Exception("No transaction to commit.")
        self.main_dataStore.update(self.temp_store)
        self.temp_store = None
        self.transactionStatus = False

    def rollback(self):
        if not self.transactionStatus:
            raise Exception("No transaction to rollback.")
        self.temp_store = None
        self.transactionStatus = False

# Testing 
if __name__ == "__main__":
    db = InMemoryDB()
   
    print(db.get("A"))  
    try:
        db.put("A", 5)
    except Exception as e:
        print(e)  

   
    db.begin_transaction()

    db.put("A", 5)
    print(db.get("A"))  

   
    db.put("A", 6)
    db.commit()

    
    print(db.get("A")) 
  
    db.begin_transaction()
    db.put("B", 10)
    db.rollback()
    print(db.get("B")) 
