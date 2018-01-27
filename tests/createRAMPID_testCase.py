from hmdbData import hmdbData
from writeToSQL import writeToSQL
from reactomeData import reactomeData
from getStatistics import getStatistics
stat = getStatistics()

import unittest

class TestHMDBMain(unittest.TestCase):
     
    def testMain(self):
        
        sql = writeToSQL()
        hmdb = hmdbData()
        reactome = reactomeData()
        
        hmdb.metaboliteIDDictionary["HMDB00001"] = {"chebi_id": "NA", 
                           "drugbank_id": "NA", 
                           "drugbank_metabolite_id": "NA", 
                           "phenol_explorer_compound_id": "NA", 
                           "phenol_explorer_metabolite_id": "NA", 
                           "foodb_id": "FDB012119", 
                           "knapsack_id": "NA", 
                           "chemspider_id": "83153",
                           "kegg_id": "C14814",
                           "biocyc_id": "CPD-1823",
                           "bigg_id": "NA",
                           "wikipidia": "NA",
                           "nugowiki": "NA",
                           "metagene": "NA",
                           "metlin_id": "3741",
                           "pubchem_compound_id": "92105",
                           "het_id": "HIC",
                           "hmdb_id": ["HMDB00001"],
                           "CAS": "NA"}
        
        
        hmdb.metaboliteIDDictionary["HMDB00002"] = {"chebi_id": "NA", 
                           "drugbank_id": "NA", 
                           "drugbank_metabolite_id": "NA", 
                           "phenol_explorer_compound_id": "NA", 
                           "phenol_explorer_metabolite_id": "NA", 
                           "foodb_id": "FDB012119", 
                           "knapsack_id": "NA", 
                           "chemspider_id": "83153",
                           "kegg_id": "C14814",
                           "biocyc_id": "CPD-1823",
                           "bigg_id": "NA",
                           "wikipidia": "NA",
                           "nugowiki": "NA",
                           "metagene": "NA",
                           "metlin_id": "3741",
                           "pubchem_compound_id": "92105",
                           "het_id": "HIC",
                           "hmdb_id": ["HMDB00002"],
                           "CAS": "NA"}
        
        reactome.metaboliteIDDictionary["C14814"] = {"chebi_id": ["C14814"], 
                    "drugbank_id": "NA", 
                    "drugbank_metabolite_id": "NA", 
                    "phenol_explorer_compound_id": "NA", 
                    "phenol_explorer_metabolite_id": "NA", 
                    "foodb_id": "NA", 
                    "knapsack_id": "NA", 
                    "chemspider_id": "NA",
                    "kegg_id": "NA",
                    "biocyc_id": "NA",
                    "bigg_id": "NA",
                    "wikipidia": "NA",
                    "nugowiki": "NA",
                    "metagene": "NA",
                    "metlin_id": "NA",
                    "pubchem_compound_id": "NA",
                    "het_id": "NA",
                    "hmdb_id": "NA",
                    "CAS": "NA"}
        
        hmdbcompoundnum = sql.createRampCompoundID(hmdb.metaboliteIDDictionary, "hmdb", 0)
        reactomecompoundnum = sql.createRampCompoundID(reactome.metaboliteIDDictionary, "reactome", hmdbcompoundnum)
        print(list(sql.rampCompoundIDdictionary.values()))      
    
    def testMain2(self):
        hmdb = hmdbData()
        sql = writeToSQL()
        hmdb.getMetaboliteOtherIDs()
        num = sql.createRampCompoundID(hmdb.metaboliteIDDictionary, 'hmdb', 0)
        hmdb.check_path('../misc/test/hmdb/')
        with open('../misc/test/hmdb/rampIDToHMDBIDs.txt','wb') as f:
            for key,value in sql.rampCompoundIDdictionary.items():
                f.write(key.encode('utf-8') +b'\t' + value.encode('utf-8') +b'\n')
            
            
if __name__ == '__main__':
    test =TestHMDBMain().testMain2()
    
    