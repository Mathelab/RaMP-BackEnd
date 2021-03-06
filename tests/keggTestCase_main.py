from KeggData import KeggData
from writeToSQL import writeToSQL
from IDconversion import IDconversion
from getStatistics import getStatistics
import time
import unittest
import csv

class TestKeggMain(unittest.TestCase):

    def testMain(self):
        kegg = KeggData() 
        
        sql = writeToSQL()
        idconvert = IDconversion()
        stat = getStatistics()
        # get database file
        kegg.getDatabaseFiles()
        
        print('get pathways')
        kegg.getPathways()
        kegg.getPathways_with_genes()
        print(len(kegg.pathwayDictionary))
        print('get metabolites')
        kegg.getMetabolites()
        
        
        print('get synonyms and chebi')
        kegg.getSynonymsAndCHEBI()
        print(len(kegg.metaboliteIDDictionary))
        print(kegg.metaboliteIDDictionary["C00002"])
        print(kegg.metaboliteIDDictionary["C00001"])

        print('get genes')
        kegg.getGenes()
        print(len(kegg.geneInfoDictionary))
        kegg.getGeneInfo()
        kegg.getPathwayLinkedToGene()

        kegg.write_myself_files(database='kegg')        
        idconvert.GeneConvert(kegg.geneInfoDictionary, "kegg")
        

        # Check duplicates
        kegg.write_myself_files('kegg')
        keggcompoundnum = sql.createRampCompoundID(kegg.metaboliteIDDictionary, "kegg", 0)
        kegggenenum = sql.createRampGeneID(kegg.geneInfoDictionary, "kegg", 0)

        keggnumbers = sql.write(
                 kegg.metaboliteCommonName,
                 kegg.pathwayDictionary, 
                 kegg.pathwayCategory,
                 kegg.metabolitesWithPathwaysDictionary,
                 kegg.metabolitesWithSynonymsDictionary,
                 kegg.metaboliteIDDictionary,
                 kegg.pathwaysWithGenesDictionary,
                 kegg.metabolitesLinkedToGenes,
                 kegg.geneInfoDictionary,
                 kegg.biofluidLocation,
                 kegg.biofluid,
                 kegg.cellularLocation,
                 kegg.cellular,
                 kegg.pathwayOntology,
                 kegg.exoEndoDictionary,
                 kegg.exoEndo,
                 kegg.tissueLocation,
                 kegg.tissue,
                 "kegg",
                 0,0)
        print('metaboliteIDdict number is ' + str(len(kegg.metaboliteIDDictionary)))
        print('GeneInfo number is ' + str(len(kegg.geneInfoDictionary)))
        print('PathwayDict number is ' + str(len(kegg.pathwayDictionary)))
        print('MetabolitesWithPath is ' + str(len(kegg.metabolitesWithPathwaysDictionary)))
        
        
        print("Compound:") 
        stat.analyteOverlaps(sql.rampCompoundIdInWhichDatabases, sql.rampCompoundIDdictionary, "Compound")
        print("\n")
        print("Gene:") 
        stat.analyteOverlaps(sql.rampGeneIdInWhichDatabases, sql.rampGeneIDdictionary, "Gene")
        


if __name__ == "__main__":
    unittest.main()