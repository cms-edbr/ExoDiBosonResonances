TH1D* getNSubjHisto(TFile* targetFile, double mass){
  char buffer[256];
  sprintf(buffer,"nsubj21_m%i",(int)mass);
  TH2D* histogram = targetFile->Get("histogram");
  int nMassBins = histogram->GetNbinsY();
  int nSubjBins = histogram->GetNbinsX();
  double widthMassBin = 50.0;
  int mainBin = (int)mass/widthMassBin;
  TH1D* projection = histogram->ProjectionX(buffer,mainBin-1,mainBin+2);
  projection->SetDirectory(0);
  return projection;
}

/// For this macro to work, you should have the file with the
/// signal and background histograms for nsubjetiness open.
/// Put the names of the histograms in the first two lines
/// of the macro.
TCanvas* compareHistos(TH1* signalHisto, TH1* backgroundHisto){
  TCanvas* cv = new TCanvas("cv","cv",1200,800);
  cv->Divide(3,2);

  int rebinFactor = 2;
  signalHisto->Rebin(rebinFactor);
  backgroundHisto->Rebin(rebinFactor);

  signalHisto->SetLineColor(kRed);
  signalHisto->SetMarkerColor(kRed);
  signalHisto->SetFillColor(kRed);
  signalHisto->SetFillStyle(3001);

  double bkgIntegral = backgroundHisto->Integral();
  signalHisto->SetTitle("");
  double sgnIntegral = signalHisto->Integral();
  
  double nBins = backgroundHisto->GetNbinsX();
  
  TGraph* ROC     = new TGraph(nBins);
  TGraph* S       = new TGraph(nBins);
  TGraph* B       = new TGraph(nBins);
  TGraph* SoverB  = new TGraph(nBins);
  TGraph* SoverSB = new TGraph(nBins); 
  TGraph* punzi   = new TGraph(nBins);

  ROC->SetTitle("");
  S->SetTitle("");
  B->SetTitle("");
  SoverB->SetTitle("");
  SoverSB->SetTitle("");
  punzi->SetTitle("");

  S->SetLineColor(kRed);
  S->SetMarkerColor(kRed);

  for(size_t i=1; i!=(nBins+1); ++i) {
    double thisB = backgroundHisto->Integral(1,i);
    double thisS = signalHisto->Integral(1,i);
    double thisSOverB = (thisB != 0) ? (thisS/thisB) : 0;
    double thisSOverSB = (thisB != 0) ? (thisS/sqrt(thisS+thisB)) : 0;
    double effSgn = thisS/sgnIntegral;
    double effBkg = thisB/bkgIntegral;
    double thisPunzi = effSgn/(1.0+sqrt(thisB));
    double binLowEdge = backgroundHisto->GetBinLowEdge(i);
    printf("binLowEdge = %g, eff Bkg = %g, eff Sgn = %g\n",binLowEdge,effBkg,effSgn);
    ROC->SetPoint(i-1,effSgn,1.0-effBkg);
    S->SetPoint(i-1,binLowEdge,effSgn);
    B->SetPoint(i-1,binLowEdge,effBkg);
    SoverB->SetPoint(i-1,binLowEdge,thisSOverB);
    SoverSB->SetPoint(i-1,binLowEdge,thisSOverSB);
    punzi->SetPoint(i-1,binLowEdge,thisPunzi);
  }

  cv->cd(1);
  signalHisto->Scale(1.0/sgnIntegral);
  backgroundHisto->Scale(1.0/bkgIntegral);
  signalHisto->Draw("HISTO");
  signalHisto->GetYaxis()->SetRangeUser(0,0.25);
  signalHisto->GetYaxis()->SetTitle("Normalized Distributions");
  backgroundHisto->Draw("HISTO SAMES");
  //cv->SaveAs("tau21.png");

  cv->cd(2);
  gPad->SetGridx();
  gPad->SetGridy();
  ROC->GetXaxis()->SetTitle("SIG efficiency");
  ROC->GetYaxis()->SetTitle("1.0 - BKG  efficiency");
  ROC->Draw("ALP");
  //cv->SaveAs("ROCcurve.png");
  
  cv->cd(3);
  S->Draw("ALP");
  B->Draw("LP");
  S->GetXaxis()->SetTitle("#tau_{21} upper threshold");
  S->GetYaxis()->SetTitle("Efficiency");
  //cv->SaveAs("efficiency.png");
  
  cv->cd(4);
  SoverB->Draw("ALP");
  SoverB->GetXaxis()->SetTitle("#tau_{21} upper threshold");
  SoverB->GetYaxis()->SetTitle("S / B");
  //cv->SaveAs("SoverB.png");
  
  cv->cd(5);
  SoverSB->Draw("ALP");
  SoverSB->GetXaxis()->SetTitle("#tau_{21} upper threshold");
  SoverSB->GetYaxis()->SetTitle("S / sqrt(S+B)");
  
  cv->cd(6);
  punzi->Draw("ALP");
  punzi->GetXaxis()->SetTitle("#tau_{21} upper threshold");
  punzi->GetYaxis()->SetTitle("#epsilon_{S} / (1.0+sqrt(B))");
  //cv->SaveAs("punzi.png");

  return cv;
}

void makeROCcurves(int massValue) {
  char buffer[256];
  sprintf(buffer,"CA8optimization/signal_%i.root",massValue);
  TFile* sgnFile = TFile::Open(buffer); 
  TFile* bkgFile = TFile::Open("CA8optimization/allBackgrounds.root"); 

  TH1* signalHisto = getNSubjHisto(sgnFile, massValue);
  TH1* backgroundHisto = getNSubjHisto(bkgFile, massValue);
  TCanvas* thisCanvas = compareHistos(signalHisto,backgroundHisto);
  bkgFile->Close();
  sgnFile->Close();
  sprintf(buffer,"optimization_%i.pdf",massValue);
  thisCanvas->SaveAs(buffer);
}

void ROCcurves(){
  makeROCcurves(600);
  makeROCcurves(700);
  makeROCcurves(800);
  makeROCcurves(900);
  makeROCcurves(1000);
  makeROCcurves(1100);
  makeROCcurves(1300);
  makeROCcurves(1400);
  makeROCcurves(1500);
  makeROCcurves(1700);
  makeROCcurves(1800);
  makeROCcurves(1900);
}