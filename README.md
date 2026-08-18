# Lumbar Spine Prior Authorization Triage (`lumbar-pa-triage`)

## What It Does
This simple script ingests structured prior authorization requests for lumbar spine MRI imaging and evaluates them against clinical practice guidelines and local coverage determinations (LCDs). By considering patient age, regional jurisdiction, provider-directed conservative management duration, surgical history, physical exam findings, and red flag indicators, the engine automatically generates standardized, single-line case summaries in `summaries.txt` for automatic insurance approval or defaults to clinical adjudication.  

## Background & Clinical Rationale
This is my first use of python to streamline a common clinical, administrative, and political scenario in the expensive world of back pain. Several payers, benefit management companies, and tech vendors deploy a more advanced version of this engine at industrial scale, and I wanted to see if I could understand python principles by making the simple version.

## Safety & Clinical Governance Design
The deterministic decision tree is designed around patient safety with both clinical and regulatory policy compliance:

1. **Red Flag Expedited Approvals:** acute red-flag indicators bypass standard conservative care duration requirements and route to immediate approval.
2. **Jurisdictional & LCD Exceptions:** automatically applies region-specific policies (e.g., AK, AR, CA, HI, ID, MT, NV, ND, OR, SD, UT, WA, WY) allowing 4 weeks of provider-directed conservative care instead of the standard 6 weeks.
3. **Clinical Guideline Validation:** evaluates nuances with advanced back pain, including surgical history, prior plain films, and documented neurological exams before standard approvals.
4. **No Automated Denials:** any case failing to meet complete approval criteria is routed to physician review (`route to MD - insufficient documentation`). 

## How to Run
Use Python 3 and run the following in your terminal:

```bash
python3 triage.py