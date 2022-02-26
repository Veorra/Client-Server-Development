{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pymongo import MongoClient\n",
    "from bson.objectid import ObjectId\n",
    "\n",
    "class AnimalShelter(object):\n",
    "    \"\"\"Crud operations for Animal collection in MongoDB\"\"\"\n",
    "    def __init__ (self, username, password):\n",
    "        #This helps to initialize mongoclient to access the database\n",
    "        self.client = MongoClient('mongodb://%s:%s@localhost:55238' % (username, password))\n",
    "        self.database = self.client['AAC']\n",
    "        \n",
    "    #Complete this create method to implement the C in CRUD\n",
    "        def create(self, data):\n",
    "            if data is not None: # Checking data disctionary\n",
    "                insert = self.database.animals.insert(data) # insert the value of the data dictionary into animal table\n",
    "                if insert != 0: # if insert is successful\n",
    "                    return True\n",
    "                else:\n",
    "                    return False\n",
    "            else:\n",
    "                raise Exception (\"Nothing to save, data parameter is empty\")\n",
    "                \n",
    "    # Create method to implement the R in CRUD\n",
    "    def read(self, criteria = None):\n",
    "        if criteria:\n",
    "            #{'_id': False} just omits the unique ID of each row\n",
    "            \n",
    "            data = self.database.animals.find(criteria, {\"_id\": False})\n",
    "        else:\n",
    "            data = self.database.animals.find({}, {\"_id\": False})\n",
    "        return data\n",
    "    # Create method to impement the U in CRUD\n",
    "    def update (self, query, record):\n",
    "        #Verify that the record exists; if so, update accordingly\n",
    "        if record is not None:\n",
    "            # update the documents matching the query criteria and print number of documents updated in json format\n",
    "            update_result = self.database.animals.update_many(query, record)\n",
    "            result = \"Documents updated: \" + json.dumps(update_result.modified_count)\n",
    "            #print Documents updated \n",
    "            return result\n",
    "        else:\n",
    "            raise Exception(\"Record not found\")\n",
    "    \n",
    "    # Create method to implement the D in CRUD\n",
    "    def delete(self, data):\n",
    "        #Verify that the record to be deleted has been supplied\n",
    "        if data is not None:\n",
    "            # delete the documents matching data criteria and print number of documents deleted in the json format\n",
    "            delete_result = self.database.animals.delete_many(data)\n",
    "            result = \"Documents deleted: \" + json.dumps(delete_result.deleted_count)\n",
    "            #print Documents deleted\n",
    "            return result\n",
    "        else:\n",
    "            raise Eception (\"No record provided.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
