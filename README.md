<p><span style="color:red; font-weight:bold; font-size:18px;">Overview</span></p>

This project was inspired by a personal experience. I once received an email that looked important but also appeared suspicious. I could not determine whether it was safe to reply or click, and I spent considerable time verifying its authenticity through colleagues, online searches, and cross-checking. That experience revealed a broader issue: people process dozens of messages every day, and they need a way to quickly and effectively determine which ones can be trusted.
Our project addresses this challenge by developing a lightweight application that helps users instantly check suspicious emails, SMS, or social media messages. The application combines rule-based detection, AI-assisted analysis, and open threat intelligence databases to provide clear and explainable results.
<p><span style="color:red; font-weight:bold; font-size:18px;">Background / Problem</span></p>

<p>In 2024, Australians reported losses of <strong>$2.03&nbsp;billion</strong> to scams and more than <strong>494,000</strong> scam reports (National Anti-Scam Centre [NASC], 2024). Among the top five scam categories, <strong>phishing alone caused $84.5&nbsp;million</strong> in losses — showing that this threat remains widespread and damaging.</p>

<p>Phishing attacks and scam messages typically trick users into disclosing:</p>
<ul>
  <li>Account credentials</strong></li>
  <li>Financial information</strong></li>
  <li>Other sensitive data</strong></li>
</ul>

<p>Many people, especially older adults and those less familiar with digital technology, lack tools to quickly verify suspicious content.</p>

<p>Small and medium-sized enterprises (SMEs)</strong> face particular challenges:</p>
<ul>
  <li>Limited resources</li>
  <li>Insufficient employee training</li>
  <li>Lack of awareness or skills to identify phishing and social engineering attempts</li>
</ul>

<p>The cost of uncertainty is high:</p>
<ul>
  <li>Ignoring a legitimate message may cause harmful delays.</li>
  <li>Trusting a fraudulent one can lead to severe financial and reputational damage.</li>
</ul>

<p>Our mission is to give people clarity and confidence, transforming uncertainty into safe and informed decisions.</p>
 
<p align="center">
  <img src="https://i.imgur.com/wD2dtdxl.png" alt="Scam Losses and Reports in Australia (2024)" width="500"/>
  <br>
  <em>Figure 1: Scam losses, reports, and top scam types in Australia (2024)</em>
</p>
 
<p><span style="color:red; font-weight:bold; font-size:18px;">Application Architecture</span></p>
The app follows a hybrid detection pipeline:

1.	Input Layer: User pastes suspicious text or uploads a screenshot → OCR extracts text and URLs.

2.	Rule-based Engine: Detects urgent language, fake/mismatched domains, short links, suspicious TLDs.

3.	AI-assisted Analysis:

- NLP for language risk patterns (e.g., urgency, reward, threats).
- Classification Model: mrm8488/bert-tiny-finetuned-sms-spam-detection

4.	Threat Intelligence Check: Cross-check with open databases (PhishTank, APWG, URLhaus).
5.	Output Layer: Risk level (High/Medium/Low) + evidence points (e.g., “Non-official domain,” “Detected urgent phrase”) + recommended action.
The system is designed to be explainable, giving users evidence, not just a score.
<p align="center">
  <img src="https://i.imgur.com/00I2soI.png" alt="Workflow Diagram" width="600"/>
  <br>
  <em>Figure 2: Workflow Diagram</em>
</p>

<p align="center">
  <img src="https://i.imgur.com/pYijCYM.png" alt="AI Diagram Image" width="600"/>
  <br>
  <em>Figure 3: AI Diagram Image</em>
</p>
<p><span style="color:red; font-weight:bold; font-size:18px;">Prototype</span></p>
<p align="center">
  <img src="https://i.imgur.com/cwE4doB.png" alt="High-fidelity Prototype" width="600"/>
  <br>
  <em>Figure 4: High-fidelity Prototype</em>
</p>

<p align="center">
  <img src="https://i.imgur.com/7rwKlol.png" alt="Low-fidelity Prototype" width="600"/>
  <br>
  <em>Figure 5: Low-fidelity Prototype</em>
</p>

<p><span style="color:red; font-weight:bold; font-size:18px;">Web App</span></p>
<p align="center">
    <img src="https://i.imgur.com/TDkCcdX.png" alt="WebApp" width="600">
    <br>
    <em>Figure 6: Web App Front Page</em>
</p>
<p><span style="color:red; font-weight:bold; font-size:18px;">Dataset</span></p>
<strong>ABS Maps</strong>
Use in Project: Utilised as a supporting dataset for generating the heatmap. It provided geographical mapping information that allowed us to visualise phishing email distribution across regions.
<strong>2024 National Anti-Scam Centre Report</strong>
Use in Project: Served as a background reference. In particular, its reporting on financial losses from scams was used to contextualise the significance of the problem and support our analysis.
<strong>2023–2030 Australian Cyber Security Strategy</strong>
Use in Project: Applied as a background resource to highlight gaps in SME (Small and Medium Enterprise) investment in cybersecurity awareness and training. This strengthened the rationale and motivation for our project’s design.
<strong>PhishTank – Verified Phishing URL Archive</strong>
Use in Project: Provided an external open dataset of phishing URLs. These were cross-checked against emails and SMS samples to improve detection accuracy and ensure robust validation of malicious indicators.
<strong>URLhaus – Malicious URL Database</strong>
Use in Project: Used as an external malicious dataset. It enabled cross-validation of suspicious emails/SMS with known malware distribution links, thus improving detection accuracy and providing strong reasoning in identifying malicious activity.

<p><span style="color:red; font-weight:bold; font-size:18px;">Limitations</span></p>
•	Coverage: Open datasets don’t capture every scam; new phishing attempts may bypass rules.
•	Accuracy: AI models may produce false positives/negatives if trained on limited data.
•	Scope: Current design covers text + URLs; richer content (voice, video phishing) is not yet addressed.
•	Privacy trade-off: While designed for local-first analysis, server-side processing may raise data trust issues.


<p><span style="color:red; font-weight:bold; font-size:18px;">Future Development</span></p>
•	Integration with government databases (e.g., consumer protection, cybersecurity agencies).
•	Multi-language support to reach wider communities.
•	Community reporting system: Crowdsource new phishing samples to strengthen detection.
•	Browser extension & chatbot: Expand beyond the app, providing real-time scanning in daily workflows.
•	Continuous AI learning: Improve classification models with new phishing variants
