# Lumbar Spine Imaging Triage (`lumbar-pa-triage`)

## What?
Simplifies synthetic prior authorization requests for lumbar spine MRI imaging and evaluates them against clinical practice guidelines and local coverage determinations (LCDs). Considers patient age, regional jurisdiction, provider-directed conservative management duration, surgical history, physical exam findings, and red flag indicators to automatically generate standardized, single-line case summaries in `summaries.txt` useful for automatic insurance approval or defaulting to clinical adjudication.  

## Background & Clinical Rationale
This is my first use of python to streamline a common clinical, administrative, and political issue in the expensive world of back pain. Several payers, benefit management companies, and tech vendors deploy a more advanced version of this engine at industrial scale - I used this is as a way to understand basic principles (e.g. f-strings).

## Safety & Clinical Governance Design
The deterministic decision tree is designed around patient safety with both clinical and regulatory policy compliance:

1. **Red Flag Expedited Approvals:** red flags bypass all conservative logic. 
2. **Jurisdictional & LCD Exceptions:** applies region-specific policies (e.g., AK, AR, CA, HI, ID, MT, NV, ND, OR, SD, UT, WA, WY) allowing 4 weeks of provider-directed conservative care instead of the standard 6 weeks.
3. **Clinical Guideline Validation:** evaluates nuances with advanced back pain, including surgical history, prior plain films, and documented neurological exams before standard approval.
4. **No Automated Denials:** any case failing to meet complete approval criteria defaults to clinical adjudication(`route to MD - insufficient documentation`). 

## Limits
- `plain_film` and `neurological_exam` are inferred from free text, so any
  unexpected value is treated as documented.
- Criteria are hard-coded rather than loaded from source policy documents.

## How to Run
```bash
python3 triage.py