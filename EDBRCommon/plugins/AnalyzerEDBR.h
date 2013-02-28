#ifndef __AnalyzerEDBR__
#define __AnalyzerEDBR__

#include <Riostream.h>
#include <string>
#include <vector>

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "FWCore/Utilities/interface/Algorithms.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "DataFormats/Common/interface/TriggerResults.h"
#include "AnalysisDataFormats/CMGTools/interface/Muon.h"
#include "AnalysisDataFormats/CMGTools/interface/Electron.h"
#include "AnalysisDataFormats/CMGTools/interface/PFJet.h"
#include "AnalysisDataFormats/CMGTools/interface/CompoundTypes.h"
#include "AnalysisDataFormats/ExoDiBosonResonances/interface/CompoundTypesHZZLL.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "PhysicsTools/FWLite/interface/TFileService.h"
#include "AnalysisDataFormats/ExoDiBosonResonances/interface/EDBRCandidate.h"

#include "CommonTools/CandUtils/interface/CenterOfMassBooster.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "CommonTools/CandUtils/interface/cloneDecayTree.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"


#include "TMatrixD.h"
#include "TVectorD.h"
#include "TTree.h"
#include "TFile.h"
#include "TH1F.h"


using namespace std;


//template <typename T> 
class AnalyzerEDBR : public edm::EDAnalyzer{

 public:
  AnalyzerEDBR(const edm::ParameterSet &ps);


  virtual ~AnalyzerEDBR(){
  cout << "AnalyzerEDBR destructor..." << endl;
  outFile_->cd();
  outTree_->Write();
  outFile_->Close();
  }

  ///Method where the analysis is done.
 
  void beginRun(edm::Run const& iRun, edm::EventSetup const& eventSetup){
    bool aaa;
    hltConfig.init(iRun,eventSetup,"HLT",aaa);
  }

  void endRun(edm::Run const& iRun, edm::EventSetup const& eventSetup){

  }

  void analyze(edm::Event const& iEvent, edm::EventSetup const& eventSetup);
  

// /// //void analyze(edm::Event const& iEvent, edm::EventSetup const& eventSetup);



 private:
  bool debug_, isMC_,  treatVBFAsMultiple_,saveVBFCands_;            // flags
  std::string cat_;
  std::string outFileName_;
  std::string VType_;
  std::string cmgEDBRMu_, cmgEDBREle_;
  unsigned int Ngen_;
  double xsec_;
  int VpdgId_; 
  double VMass_;
  unsigned int fillGen_;

  void init();
  void initTree();
  void initDataMembers();
  void analyzeTrigger(edm::Event const& iEvent, edm::EventSetup const& eventSetup);
  void analyzeGenLevel(edm::Event const& iEvent, edm::EventSetup const& eventSetup);
  // void analyzeGeneric(edbr,int ih, bool goodKinFit);
  double deltaR(reco::LeafCandidate p1,reco::LeafCandidate p2);
  double deltaR(double phi1,double eta1,double phi2,double eta2);

   //////////////////////////////////////
   /////////////////////////////////////
   //////////////////////////////////////
   /////////////////////////////////////


  template < typename T > void analyzeGeneric(T edbr,int& ih){

 
   //example for the future
   //   if(edbr->getSelection("cuts_btags_btag2")){
   //  btag[ih] = 2;
   // }	

   MCmatch[ih] = edbr->getSelection("cuts_genMatch");
   deltaREDBR[ih] = 0.0;//deltaR(edbr->phi(),edbr->eta(),genEDBR.phi(),genEDBR.eta());




   // if(debug_)cout<<"Inside AnalyzerEDBR::analyzeGeneric "<<ih<<" "<<flush;
   reg[ih]=(edbr->leg2().getSelection("cuts_isSignal")? 1.0 : 0.0 );
   mzz[ih]=edbr->mass();
   ptmzz[ih]=edbr->pt();
  
   if(debug_)cout<<"Inside AnalyzerEDBR::analyzeGeneric mzz="<<mzz[ih]<<"  pT_mzz="<<ptmzz[ih] <<endl;

   hs[ih]     = edbr->costhetastar();
   h1[ih]     = edbr->helcosthetaZl1();
   h2[ih]     = edbr->helcosthetaZl2();
   phi[ih]    = edbr->helphiZl1();
   phiS1[ih]  = edbr->phistarZl1(); 
   LD[ih] = edbr->userFloat("LD");
  
 

   //   if(debug_)cout<<"AnalyzerEDBR::analyzeGeneric filling mLL" <<endl;
   mll[ih]=edbr->leg1().mass();
 
   ptZll[ih]=edbr->leg1().pt();
   ptZjj[ih]=edbr->leg2().pt();
   yZll[ih]=edbr->leg1().rapidity();
   yZjj[ih]=edbr->leg2().rapidity();
   phiZll[ih]=edbr->leg1().phi();
   phiZjj[ih]=edbr->leg2().phi();

   //   if(debug_)cout<<"AnalyzerEDBR::analyzeGeneric filling leptons" <<endl;

   bool highptLep1=true;
   if(edbr->leg1().leg2().pt()>edbr->leg1().leg1().pt())highptLep1=false;
   if(VType_=="W")highptLep1=true;//for ww case, we don't compare pt of lepton and neutrino
   
   if(highptLep1){
     ptlep1[ih]=edbr->leg1().leg1().pt();
     ptlep2[ih]=edbr->leg1().leg2().pt();
     etalep1[ih]=edbr->leg1().leg1().eta();
     etalep2[ih]=edbr->leg1().leg2().eta();
     philep1[ih]=edbr->leg1().leg1().phi();
     philep2[ih]=edbr->leg1().leg2().phi();
     isolep1[ih]=edbr->leg1().leg1().relIso();
     isolep2[ih]=edbr->leg1().leg2().relIso();
   }
   else{
     ptlep1[ih]=edbr->leg1().leg2().pt();
     ptlep2[ih]=edbr->leg1().leg1().pt();
     etalep1[ih]=edbr->leg1().leg2().eta();
     etalep2[ih]=edbr->leg1().leg1().eta();
     philep1[ih]=edbr->leg1().leg2().phi();
     philep2[ih]=edbr->leg1().leg1().phi();
     isolep1[ih]=edbr->leg1().leg2().relIso();
     isolep2[ih]=edbr->leg1().leg1().relIso();
   }


   deltaRleplep[ih]=deltaR(edbr->leg1().leg1().phi(),
			   edbr->leg1().leg1().eta(),
			   edbr->leg1().leg2().phi(),
			   edbr->leg1().leg2().eta());

   mt[ih] = sqrt( 2*edbr->leg1().leg1().pt()*edbr->leg1().leg2().pt()*( 1-cos(edbr->leg1().leg1().phi()-edbr->leg1().leg2().phi()) ) );
   nbtagsL[ih] = edbr->userFloat("nbtagsL");
   nbtagsM[ih] = edbr->userFloat("nbtagsM");
   nbtagsT[ih] = edbr->userFloat("nbtagsT");
   nbtagscleanL[ih] = edbr->userFloat("nbtagscleanL"); 
   nbtagscleanM[ih] = edbr->userFloat("nbtagscleanM"); 
   nbtagscleanT[ih] = edbr->userFloat("nbtagscleanT"); 
  

   //if(finalM_||sbM_||finalE_||sbE_){//with this if condition, presel will have PU weights==1

   // THESE WEIGHTS=1 FOR REAL DATA
   HLTSF = edbr->userFloat("HLTWeight");
   if(edbr->hasUserFloat("PUWeights")){
     //if(preselM_ || preselM1J_ ||preselE_ ||preselE1J_ ){
     //   std::cout<<"Event passes presel path"<<std::endl;
     PU  = edbr->userFloat("PUWeights");
     PUA = edbr->userFloat("PUWeights2012A");
     PUB = edbr->userFloat("PUWeights2012B");
   }
   else if(edbr->hasUserFloat("PUWeightsFullE")){
     //else if( finalE_ || sbE_|| finalE1J_ || sbE1J_){   
     if(!elePath_)std::cout<<"Warning from AnalyzerEDBR::analyzeGeneric Run "<<run<<" Event "<<nevent<<" : EDBR cand  has userfloat PUWeightsFullE but elePath_==false . This could be an indication of something not properly right."<<std::endl;
     
     PU  = edbr->userFloat("PUWeightsFullE");
     PUA = edbr->userFloat("PUWeights2012AFullE");
     PUB = edbr->userFloat("PUWeights2012BFullE");
   }
   else if(edbr->hasUserFloat("PUWeightsFullM")){
     //else if( finalM_ || sbM_|| finalM1J_ || sbM1J_){
     
     if(!muPath_)std::cout<<"Warning from AnalyzerEDBR::analyzeGeneric Run "<<run<<" Event "<<nevent<<" : EDBR cand  has userfloat PUWeightsFullM but muPath_==false . This could be an indication of something not properly right."<<std::endl;
     PU  = edbr->userFloat("PUWeightsFullM");
     PUA = edbr->userFloat("PUWeights2012AFullM");
     PUB = edbr->userFloat("PUWeights2012BFullM");
   }
   else{
     PU  = -99.0;
     PUA = -99.0;
     PUB = -99.0;
   }
   

  //  if(debug_)cout<<"AnalyzerEDBR::analyzeGeneric finishing Cand #" <<ih<<endl;
  
  }//end analyzeGeneric

  //////////////////////////////////////
  /////////////////////////////////////
  //////////////////////////////////////
  /////////////////////////////////////

  //functions specific for boosted and not-boosted topologies  
  template < typename T > void  analyzeSingleJet(T edbr,int& ih){
    //  if(debug_)cout<<"AnalyzerEDBR::analyzeSingleJet filling jet vars  " <<ih<<endl;

    if(debug_)std::cout<<"nXJets="<<edbr->userFloat("nXJets")<<" (it should be ==1) "<<endl;
    nXjets[ih]=1;//edbr->nJets();
    mzzNoKinFit[ih]=edbr->mass();
    mjj[ih]=edbr->leg2().prunedMass();
    mjjNoKinFit[ih]=mjj[ih];
    ptmzzNoKinFit[ih]=edbr->pt();
    ptjjNoKinFit[ih]=edbr->leg2().pt();
    ////fill jet kine vars: first jet vars refer to jet used for building EDBR,
    ////                    second jet vars are dummy
 
    bool highptJet1=true;
    if(highptJet1){
      ptjet1[ih]=edbr->leg2().pt();
      ptjet2[ih]=-99.0;
      etajet1[ih]=edbr->leg2().eta();
      etajet2[ih]=-99.0;
      phijet1[ih]=edbr->leg2().phi();
      phijet2[ih]=-99.0;
      
      
      betajet1[ih] = edbr->leg2().beta(); 
      betajet2[ih] = -1.0;
      puMvajet1[ih] = edbr->leg2().puMva("full"); 
      puMvajet2[ih] = -9999.0;
    }

    deltaRjetjet[ih]=0.0;

    //jet sub-structure 
    prunedmass[ih]=edbr->leg2().prunedMass();
    mdrop[ih]=edbr->leg2().mdrop();
    qjet[ih]= edbr->leg2().qjet();
    nsubj12[ih]=edbr->leg2().ntau12();
    nsubj23[ih]=edbr->leg2().ntau23();
    tau1[ih]=edbr->leg2().tau1();
    tau2[ih]=edbr->leg2().tau2();


    // dummy jet vars
    btag[ih]=-1;
    q1fl[ih]=-99.0;
    q2fl[ih]=-99.0;
    qgjet1[ih]=-99.0;
    qgjet2[ih]=-99.0;
    qgProduct[ih]=-99.0;
  }//end analyzeSingleJet();


  template < typename T > void  analyzeDoubleJet(T edbr,int& ih, bool & goodKinFit){


    if(edbr->leg2().mass()<VMass_-1 ||edbr->leg2().mass()>VMass_+1){
      cout<<"WARNING from AnalyzeEDBR::analyzeDoubleJet : KIN FIT badly converged!! M_jj="<<edbr->leg2()<<endl;
      goodKinFit = false;
    }

    if(debug_)std::cout<<"nXJets="<<edbr->userFloat("nXJets")<<" (it should be ==2) "<<endl;
    nXjets[ih]=int(edbr->userFloat("nXJets"));//edbr->nJets();
    mzzNoKinFit[ih]=edbr->userFloat("nokinfitMZZ");
    ptmzzNoKinFit[ih]=edbr->userFloat("nokinfitPTZZ");
    mjj[ih]=edbr->leg2().mass();
    mjjNoKinFit[ih]=edbr->userFloat("nokinfitMJJ");
    	//  double isomu1mod[nMaxCand], isomu2mod[nMaxCand]; // modified tracker iso for muons
	//  double isoele1trk[nMaxCand], isoele2trk[nMaxCand], isoele1calo[nMaxCand], isoele2calo[nMaxCand]; // modified isos for ele

    isomu1mod[ih]=edbr->userFloat("isomu1mod");
    isomu2mod[ih]=edbr->userFloat("isomu2mod");
    isoele1trk[ih]=edbr->userFloat("isoele1trk");
    isoele2trk[ih]=edbr->userFloat("isoele2trk");
    isoele1calo[ih]=edbr->userFloat("isoele1calo");
    isoele2calo[ih]=edbr->userFloat("isoele2calo");
    ptjjNoKinFit[ih]=edbr->userFloat("nokinfitPTJJ");
    etajjNoKinFit[ih]=edbr->userFloat("nokinfitEtaJJ");
    phijjNoKinFit[ih]=edbr->userFloat("nokinfitPhiJJ");
    if(debug_)cout<<"AnalyzerEDBR::analyzeDoubleJet filling jet vars  " <<ih<<endl;
    ////fill jet kine vars
    bool highptJet1=true;
    if(edbr->leg2().leg2().pt()>edbr->leg2().leg1().pt())highptJet1=false;
    if(highptJet1){
      ptjet1[ih]=edbr->leg2().leg1().pt();
      ptjet2[ih]=edbr->leg2().leg2().pt();
      etajet1[ih]=edbr->leg2().leg1().eta();
      etajet2[ih]=edbr->leg2().leg2().eta();
      phijet1[ih]=edbr->leg2().leg1().phi();
      phijet2[ih]=edbr->leg2().leg2().phi();
      
      betajet1[ih] = edbr->leg2().leg1().beta(); 
      betajet2[ih] = edbr->leg2().leg2().beta(); 
      puMvajet1[ih] = edbr->leg2().leg1().puMva("full"); 
      puMvajet2[ih] = edbr->leg2().leg2().puMva("full"); 
    }
    else{
      ptjet2[ih]=edbr->leg2().leg1().pt();
      ptjet1[ih]=edbr->leg2().leg2().pt();
      etajet2[ih]=edbr->leg2().leg1().eta();
      etajet1[ih]=edbr->leg2().leg2().eta();
      phijet2[ih]=edbr->leg2().leg1().phi();
      phijet1[ih]=edbr->leg2().leg2().phi();

      betajet2[ih] = edbr->leg2().leg1().beta(); 
      betajet1[ih] = edbr->leg2().leg2().beta(); 
      puMvajet2[ih] = edbr->leg2().leg1().puMva("full"); 
      puMvajet1[ih] = edbr->leg2().leg2().puMva("full");
    }

    deltaRjetjet[ih]=deltaR(edbr->leg2().leg1().phi(),
			    edbr->leg2().leg1().eta(),
			    edbr->leg2().leg2().phi(),
			    edbr->leg2().leg2().eta());

    //jet sub-structure is dummy for double jet
  //jet sub-structure 
    prunedmass[ih]=-99.0;
    mdrop[ih]=-999.0;
    qjet[ih]=-999.0;
    nsubj12[ih]=-999.0;
    nsubj23[ih]=-999.0;
    tau1[ih]=-999.0;
    tau2[ih]=-999.0;

    //#btags is dummy
    btag[ih]=-1;
    q1fl[ih]=-99.0;
    q2fl[ih]=-99.0;
    qgjet1[ih]=-99.0;
    qgjet2[ih]=-99.0;
    qgProduct[ih]=-99.0;


  
  //  if(finalM_||sbM_||finalE_||sbE_){
  //  if(readQGFromUserFloat_) qgProduct[ih] = edbr->userFloat("QG");
  //  else {  // pandolfi to be blamed for this
  //    edm::ProductID prodId = edbr->leg2().leg2().sourcePtr()->id(); //should be the same for both legs
  //    size_t index1 = edbr->leg2().leg1().sourcePtr()->key();
  //    size_t index2 = edbr->leg2().leg2().sourcePtr()->key();
  //    
  //    // QG LIKELIHOOD FROM JETS
  //    qgProduct[ih] = qgmap->get(prodId,index2) * qgmap->get(prodId,index1);
  //    if(edbr->leg2().leg1().pt()>edbr->leg2().leg2().pt()){
  //	qgjet1[ih] = qgmap->get(prodId,index1);
  //	qgjet2[ih] = qgmap->get(prodId,index2);
  //    } else {
  //	qgjet1[ih] = qgmap->get(prodId,index2);
  //	qgjet2[ih] = qgmap->get(prodId,index1);
  //   }
  //  }// end else recalculate qgProd
  //  }//end if finalM_||sbM_||finalE_||sbE_
 

  }//end analyzeDoubleJet();


  //////////////////////////////////////
  /////////////////////////////////////
  //functions specific for lepton flavors
  // void analyzeMuon(edm::RefToBase<cmg::DiMuonDiJetEDBR > edbr, int ih);
  template < typename T > void  analyzeMuon(T edbr, int ih){
    //nothing to be done
    //
    //
    if(debug_)cout<<"Inside AnalyzerEDBR::analyzeMuon"<<endl;

	lep[ih]=1;

    //dummy for muons 
    eleMVAId1[ih] = -1.0;
    eleMVAId2[ih] = -1.0;
  }//end analyzeMuon


  template < typename T > void analyzeElectron(T edbr, int ih){


    if(debug_)cout<<"Inside AnalyzerEDBR::analyzeElectron for cand#"<<ih<<" : "<<std::flush;
    bool highptLep1=true;
    if(edbr->leg1().leg2().pt()>edbr->leg1().leg1().pt())highptLep1=false;
	if(VType_=="W")highptLep1=true;//for ww case, we don't compare pt of lepton and neutrino
	lep[ih]=0;    
    
    if(highptLep1){
      eleMVAId1[ih] = edbr->leg1().leg1().mvaTrigV0(); 
      eleMVAId2[ih] = edbr->leg1().leg2().mvaTrigV0();
    } 
    else{
      eleMVAId1[ih] = edbr->leg1().leg2().mvaTrigV0(); 
      eleMVAId2[ih] = edbr->leg1().leg1().mvaTrigV0();
    }
    if(debug_)    std::cout<<"leg1.eleMVA="<<eleMVAId1[ih]<<"  leg2.eleMVA="<<eleMVAId2[ih]<<std::endl;
  }//end analyzeElectron


  template < typename T > int checkVBFTag(T edbr,int ih,bool vbfFound, bool& keepThisVBFCand){
  
    int vbfFlag=0;//not a VBF-tagged candidate by default
    if(edbr->vbfptr().isAvailable() )vbfFlag = 1;
    //if(edbr->getSelection("tag_vbfDoubleJet_vbf") || edbr->getSelection("tag_vbfSingleJet_vbf")  )vbfFlag = 1;
         
    if(!treatVBFAsMultiple_){//save only 1st VBF, skip all other vbf combinations associated to the same cand
      if(ih>0){//don't even bother if this is the very first candidate
	if(vbfFlag>0 && vbfFound  ){//this cand is vbf tagged and we have already found another vbf-tagged
	  
	  for(int tmpInd1=0;tmpInd1<ih;tmpInd1++){
	    if(VBFTag[tmpInd1]>0){
	      double mdiffTmp=edbr->mass()-mzz[tmpInd1];
	      if(mdiffTmp<0.01)keepThisVBFCand=false;
	    }
	  }//end loop on previous candidates
	}
      }//end if ih>0
    }//end if !treatVBFAsMultiple_
    
 
    return vbfFlag;
  }//end checkVBFTag

  template < typename T > void analyzeVBF(T edbr,int ih,int vbfFlag){

    VBFmJJ[ih]=-777.0;
    VBFdeltaEta[ih]=-777.0;
    VBFptjet1[ih]=-777.0;
    VBFptjet2[ih]=-777.0;
    VBFetajet1[ih]=-777.0;
    VBFetajet2[ih]=-777.0;
    VBFphijet1[ih]=-777.0;
    VBFphijet2[ih]=-777.0;

    if(vbfFlag>0){
      VBFmJJ[ih]=edbr->vbfptr()->mass();
      VBFptjet1[ih]=edbr->vbfptr()->leg1().pt();
      VBFptjet2[ih]=edbr->vbfptr()->leg2().pt();
      VBFetajet1[ih]=edbr->vbfptr()->leg1().eta();
      VBFetajet2[ih]=edbr->vbfptr()->leg2().eta();
      VBFphijet1[ih]=edbr->vbfptr()->leg1().phi();
      VBFphijet2[ih]=edbr->vbfptr()->leg2().phi();
      VBFdeltaEta[ih]=fabs(VBFetajet1[ih]-VBFetajet2[ih]);
    }

  }//end analyzeVBF

   //////////////////////////////////////
   // DATA MEMBERS


  edm::InputTag XEEColl_,XEELDMap_,XEEJColl_,XEEJLDMap_;
  edm::InputTag XMMColl_,XMMLDMap_,XMMJColl_,XMMJLDMap_;
    edm::InputTag  XQGMap_;

  const static int nMaxCand = 30;
  const static int nMaxTrig = 20;
  //  int nCands_;

  const static int metSignMax = 10;

  /// variables to be stored in the output tree
  TTree* outTree_;
  TFile* outFile_;

  std::vector<std::string> triggerNames_;
  int triggerRes[nMaxTrig];  

  //flags indicating whether the cand passed a certain cms.Path of the analysis
  bool preselM_, finalM_,sbM_;
  bool preselE_, finalE_,sbE_;
  bool preselM1J_, finalM1J_,sbM1J_;
  bool preselE1J_, finalE1J_,sbE1J_;
  bool anyPath_,muPath_,elePath_, singleJetPath_,doubleJetPath_;

  int nCands;
  double hs[nMaxCand], h1[nMaxCand], h2[nMaxCand], phi[nMaxCand], phiS1[nMaxCand], LD[nMaxCand]; // Helicity angles, and LD.
  double mzz[nMaxCand], mll[nMaxCand], mjj[nMaxCand]; // masses
  double ptmzz[nMaxCand];
  double ptlep1[nMaxCand], ptlep2[nMaxCand], etalep1[nMaxCand], etalep2[nMaxCand], philep1[nMaxCand], philep2[nMaxCand];  // lepton kinematics
  double ptjet1[nMaxCand], ptjet2[nMaxCand], etajet1[nMaxCand], etajet2[nMaxCand], phijet1[nMaxCand], phijet2[nMaxCand];  // jet kinematicse
  double  ptmzzNoKinFit[nMaxCand],  mzzNoKinFit[nMaxCand], mjjNoKinFit[nMaxCand],ptjjNoKinFit[nMaxCand],etajjNoKinFit[nMaxCand],phijjNoKinFit[nMaxCand];
  double deltaREDBR[nMaxCand];
  double ptZll[nMaxCand], ptZjj[nMaxCand], yZll[nMaxCand], yZjj[nMaxCand], deltaRleplep[nMaxCand], deltaRjetjet[nMaxCand];
  double phiZll[nMaxCand];//={init};
  double phiZjj[nMaxCand];//={init};
  double met, metSign;            // MET and its significance
  double btag[nMaxCand], lep[nMaxCand], reg[nMaxCand];    // b-tags, lep category, region (sig, sideband)
  double qgjet1[nMaxCand], qgjet2[nMaxCand], qgProduct[nMaxCand];    // QG likelihoods
  double betajet1[nMaxCand],betajet2[nMaxCand],puMvajet1[nMaxCand],puMvajet2[nMaxCand];//jet ID 
  double isolep1[nMaxCand], isolep2[nMaxCand], eleMVAId1[nMaxCand], eleMVAId2[nMaxCand];//lepton ID 
  double isomu1mod[nMaxCand], isomu2mod[nMaxCand]; // modified tracker iso for muons
  double isoele1trk[nMaxCand], isoele2trk[nMaxCand], isoele1calo[nMaxCand], isoele2calo[nMaxCand]; // modified isos for ele
  double HLTSF,PU,PUA,PUB,lumiw,genw,w,wA,wB;          // weight
  double MCmatch[nMaxCand];            // mc matching flag
 
  double qjet[nMaxCand],tau1[nMaxCand],tau2[nMaxCand],nsubj12[nMaxCand],nsubj23[nMaxCand];
  double mdrop[nMaxCand],prunedmass[nMaxCand];

  int VBFTag[nMaxCand];
  double VBFmJJ[nMaxCand],VBFdeltaEta[nMaxCand],VBFptjet1[nMaxCand],VBFptjet2[nMaxCand],VBFetajet1[nMaxCand],VBFetajet2[nMaxCand],VBFphijet1[nMaxCand],VBFphijet2[nMaxCand];

  double massGenX, ptGenX,yGenX, phiGenX;
  double massGenZll, ptGenZll,yGenZll, phiGenZll;
  double massGenZqq, ptGenZqq,yGenZqq, phiGenZqq;
  double ptGenq1,etaGenq1, phiGenq1,ptGenq2,etaGenq2, phiGenq2 ;
  double ptGenl1,etaGenl1, phiGenl1,ptGenl2,etaGenl2, phiGenl2 ;
  int pdgIdGenX,flavGenq1,flavGenq2,flavGenl1,flavGenl2;



  unsigned int nevent,run,ls, njets, nvtx,npu;
  int q1fl[nMaxCand], q2fl[nMaxCand];
  int nXjets[nMaxCand];//by how many jets is the hadronic V made
  //int jjfl[nMaxCand];
  bool readLDFromUserFloat_,  readQGFromUserFloat_;
  HLTConfigProvider hltConfig;

  //flag of the number of loose muons/electrons in one event
  int nLooseMu;
  int nLooseEle;

  //transvers mass of w
  double mt[nMaxCand];

  //number of btagged jets
  double nbtagsL[nMaxCand], nbtagscleanL[nMaxCand];
  double nbtagsM[nMaxCand], nbtagscleanM[nMaxCand];
  double nbtagsT[nMaxCand], nbtagscleanT[nMaxCand];

  //index of events in the cmgtuple, begin from 1
  int nEvt;

};//end class AnalyzerEDBR 




#endif
