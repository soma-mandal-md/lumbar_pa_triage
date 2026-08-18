import csv

# 1. Define the triage standing order for lumbar PA cases
def check_case(case):
    # Safety rule: Check for red flags first
    if case["red_flag"]:
        return "approve - red flag"
    # 2. LCD exception
    elif case["LCD"] or (case["jurisdiction"] in ["AK", "AR", "CA", "HI", "ID", "MT", "NV", "ND", "OR", "SD", "UT", "WA", "WY"] and case["weeks_provider_conservative"] >= 4):
        return "approve - LCD exception"    
    # 3. Standard with surgery
    elif case["prior_lumbar_surgery"] and case["plain_film"] and case["neurological_exam"] and case["weeks_provider_conservative"] >= 6:
        return "approve - plain film, neuro exam, and duration met"
    # 4. Standard without surgery
    elif not case["prior_lumbar_surgery"] and case["neurological_exam"] and case["weeks_provider_conservative"] >= 6:
        return "approve - duration and neuro exam met"
    # 5. Route to MD: Insufficient documentation
    else:
        return "route to MD - insufficient documentation"

# 2. Read input CSV and write directly to output text file
input_file = "triagecases.csv"
output_file = "summaries.txt"

# Open both files at the same time using a single 'with' statement
with open(input_file, mode="r", encoding="utf-8") as infile, \
     open(output_file, mode="w", encoding="utf-8") as outfile: 
    
    # DictReader uses the first row of your CSV (headers) as key names 
    reader = csv.DictReader(infile) 
    
    for row in reader: 
        # Convert raw CSV string inputs into numbers and booleans 
        case_data = { 
            "case_id": row["case_id"],
            "age": int(row["age"]), 
            "weeks_provider_conservative": int(row["weeks_provider_conservative"]), 
            "red_flag": row["red_flag"].strip().lower() == "true", 
            "LCD": row["LCD"].strip().lower() == "true",
            "jurisdiction": row["jurisdiction"].strip().upper(),
            "prior_lumbar_surgery": row["prior_lumbar_surgery"].strip().lower() == "true",
            "plain_film": row["plain_film"].strip().lower() not in ["false", "none", ""],
            "neurological_exam": row["neurological_exam"].strip().lower() not in ["false", "none", ""],
        }
        
        # Run triage decision 
        decision = check_case(case_data) 

        # Format a detailed clinical summary line using an f-string
        summary_line = (f"{case_data['case_id']}: {case_data['age']}yo ({case_data['jurisdiction']}), "
                        f"{case_data['weeks_provider_conservative']} wks PT documented. "
                        f"[Red flag: {case_data['red_flag']}, LCD: {case_data['LCD']}, "
                        f"Prior Surg: {case_data['prior_lumbar_surgery']}] "
                        f"-> {decision}\n")

        # Write the formatted string to summaries.txt
        outfile.write(summary_line)

print("Processing complete! Open summaries.txt to review the QA decisions.")