# EvictAware Human Verification Checklist
## Version 1.0 | Team Vision Forge | June 2026
### USAII Global AI Hackathon 2026 — Challenge Brief 4

---

## Purpose

This checklist exists because an AI generated the legal information in this application — and an AI can be confidently wrong about legal details. Every item below is a specific legal fact, phone number, URL, or statutory citation that must be checked against a primary official source by a human team member before the app is demonstrated to judges or submitted.

This checklist is also part of our Responsible AI story. We are showing judges that we did not blindly trust AI-generated legal content. We verified it.

---

## How to Use This Checklist

1. **Start with CRITICAL items.** These must be verified before any demo. An error in a CRITICAL item causes a user to take the wrong legal action at the worst possible moment.
2. **Complete HIGH items before submission.** Errors here reduce accuracy but are not catastrophic.
3. **Complete STANDARD items before production launch.** These affect completeness and credibility.
4. For each item: find the official source listed, look up the specific provision, and note what you found.
5. If an item does not match what is in our data files, **update the file immediately** and note the correction.
6. Sign each item you verify with your name and the date.

---

## Verification Sources

| Source | URL | What It Covers |
|---|---|---|
| California Legislative Information | https://leginfo.legislature.ca.gov | Every California Civil Code and CCP section — search by section number |
| California Courts Self-Help Eviction | https://www.courts.ca.gov/selfhelp-eviction.htm | Timeline figures, UD process, court forms |
| LawHelpCA.org | https://www.lawhelp.org/ca | Legal aid contact directory by county |
| California Civil Rights Department | https://calcivilrights.ca.gov | FEHA housing protections and protected classes |
| LA Housing Department (HCIDLA) | https://hcidla.lacity.gov | LA RSO coverage criteria |
| SF Rent Board | https://sfrb.org | SF Rent Ordinance coverage criteria |
| Oakland Rent Adjustment Program | https://www.oaklandca.gov/topics/rent-adjustment-program | Oakland Just Cause ordinance |
| California Department of Housing (HCD) | https://www.hcd.ca.gov | AB 1482 guidance, current rental assistance programs |
| Housing is Key | https://housing.ca.gov | Current CA ERAP/rental assistance status |
| Judicial Council Forms | https://www.courts.ca.gov/forms.htm | UD-105 and other eviction forms |

---

## CRITICAL Items — Verify Before Any Demo

These items, if wrong, cause a user to receive legally inaccurate guidance at their most vulnerable moment.

---

- [ ] **CRIT-001 — Three-Day Notice Statutory Authority**
  - **Claim in our data:** Three-Day Notice to Pay Rent or Quit is governed by California Civil Code Section 1161(2)
  - **Source to check:** https://leginfo.legislature.ca.gov — search Civil Code Section 1161
  - **What to look for:** Confirm Section 1161(2) specifically covers nonpayment of rent as a ground for unlawful detainer, that it requires a 3-day notice, and that it allows the tenant to pay within 3 days to cure.
  - **Priority:** CRITICAL
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **CRIT-002 — Three-Day Notice: Weekends and Court Holidays Excluded**
  - **Claim in our data:** The 3-day notice period excludes weekends and judicial holidays (court holidays)
  - **Source to check:** California Code of Civil Procedure Section 1161; also check CCP Section 12 and 12a for California rules on computing time periods
  - **What to look for:** Confirm that when computing the 3-day notice period, Saturdays, Sundays, and court holidays are excluded. This is the difference between a tenant thinking they have until Tuesday vs. Thursday.
  - **Priority:** CRITICAL
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **CRIT-003 — UD Response Deadline: 5 Business Days**
  - **Claim in our data:** After being served with an unlawful detainer summons, the tenant has 5 business days to file a written response (Answer)
  - **Source to check:** https://leginfo.legislature.ca.gov — search California Code of Civil Procedure Section 1167
  - **What to look for:** Confirm CCP 1167 is the correct section for the UD response deadline. Confirm the deadline is 5 days. Confirm whether "5 days" means business days (excluding weekends/holidays) or calendar days.
  - **Priority:** CRITICAL
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **CRIT-004 — Illegal Lockout Statute: Civil Code 789.3**
  - **Claim in our data:** Illegal lockouts, utility shutoffs as eviction tactic, and removal of personal property are prohibited by California Civil Code Section 789.3
  - **Source to check:** https://leginfo.legislature.ca.gov — search Civil Code Section 789.3
  - **What to look for:** Confirm CC 789.3 covers all three of these actions (lockout, utility shutoff, property removal). Confirm the statutory damages formula — specifically the amount per day and the minimum damages amount. Confirm whether attorney fees are awarded under this section.
  - **Note:** Our data cites $100/day, $1,000 minimum — confirm these figures against current statute.
  - **Priority:** CRITICAL
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **CRIT-005 — Priya's Demo: Fresno Legal Aid Phone Number**
  - **Claim in our data:** Central California Legal Services Fresno intake: (559) 570-1200
  - **Source to check:** https://www.centralcallegal.org — navigate to Contact page
  - **What to look for:** Confirm this phone number is answered by Central California Legal Services for tenant rights/eviction intake. Confirm it is still active. Note current hours. This is the exact number judges will see in the live demo.
  - **Priority:** CRITICAL — this number appears in the primary demo
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **CRIT-006 — Writ of Possession 5-Day Pre-Lockout Notice**
  - **Claim in our data:** After a Writ of Possession is issued and served, the sheriff gives the tenant 5 days before executing the lockout
  - **Source to check:** California Code of Civil Procedure Section 715.010 et seq.; also check California Courts Self-Help at courts.ca.gov/selfhelp-eviction.htm
  - **What to look for:** Confirm that there is a mandatory notice period between writ service and sheriff lockout. Confirm the exact number of days. Confirm whether this is 5 calendar days or business days.
  - **Priority:** CRITICAL — this figure appears in the demo's "you do not have to leave tonight" messaging
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **CRIT-007 — Notice of Belief of Abandonment: CC 1951.3 and 15-Day Response**
  - **Claim in our data:** Notice of Belief of Abandonment is governed by California Civil Code Section 1951.3; the tenant has 15 days to respond
  - **Source to check:** https://leginfo.legislature.ca.gov — search Civil Code Section 1951.3
  - **What to look for:** Confirm CC 1951.3 is the correct section. Confirm the response period is 15 days. Confirm what form the tenant's response must take (written? Any specific form?). Confirm what happens if the tenant responds within 15 days (landlord cannot treat as abandonment).
  - **Priority:** CRITICAL — misclassifying this notice causes catastrophic wrong action (Keisha test scenario)
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **CRIT-008 — Harassment Prohibition: Civil Code 1940.2**
  - **Claim in our data:** Landlord harassment including threatening communications is prohibited by California Civil Code Section 1940.2
  - **Source to check:** https://leginfo.legislature.ca.gov — search Civil Code Section 1940.2
  - **What to look for:** Confirm CC 1940.2 is the correct section for landlord harassment prohibition. Confirm what specific conduct is listed as prohibited (threatening calls, texts, intimidation). Confirm whether there is a private right of action for the tenant and what damages are available.
  - **Priority:** CRITICAL — directly relevant to Priya's landlord's threatening text message
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **CRIT-009 — Retaliatory Eviction: Civil Code 1942.5 and 180-Day Presumption**
  - **Claim in our data:** Retaliatory eviction is prohibited by California Civil Code Section 1942.5; a notice within 180 days of a protected act creates a legal presumption of retaliation
  - **Source to check:** https://leginfo.legislature.ca.gov — search Civil Code Section 1942.5
  - **What to look for:** Confirm CC 1942.5 is the correct section. Confirm the 180-day presumption period. Confirm the burden-shifting framework (landlord must prove non-retaliation). Confirm what protected activities are listed. Confirm available damages.
  - **Priority:** CRITICAL
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **CRIT-010 — AB 1482 Applicability: Tenant Protection Act of 2019**
  - **Claim in our data:** AB 1482 (Tenant Protection Act of 2019), codified in Civil Code 1946.2 and 1947.12, requires just cause for eviction for tenants who have lived in a unit for 12 months or more (with applicable exemptions)
  - **Source to check:** https://leginfo.legislature.ca.gov — search Civil Code Sections 1946.2 and 1947.12; also check HCD guidance at hcd.ca.gov
  - **What to look for:** Confirm the 12-month threshold for just-cause requirement. Confirm what properties are exempt from AB 1482 (single-family homes with proper notice, condos, buildings built within the last 15 years, etc.). Confirm relocation assistance requirement for no-fault just cause terminations. Confirm whether this applies to month-to-month tenancies.
  - **Priority:** CRITICAL — affects both James demo scenario and any AB 1482 reference in the app
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **CRIT-011 — Current Status of California Emergency Rental Assistance**
  - **Claim in our data:** housing.ca.gov is the portal for California emergency rental assistance; a program was active as of last update
  - **Source to check:** https://housing.ca.gov and https://www.hcd.ca.gov — look for any active rental assistance programs
  - **What to look for:** As of June 2026, is California currently accepting applications for any emergency rental assistance program? What is the current program name? What is the correct intake URL? Does application to the program create any protection against UD proceedings while the application is pending?
  - **Priority:** CRITICAL — referring a tenant to a closed program wastes critical time during a 3-day window
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **CRIT-012 — DV Hotline Number**
  - **Claim in our data:** National Domestic Violence Hotline: 1-800-799-7233; text START to 88788
  - **Source to check:** https://www.thehotline.org
  - **What to look for:** Confirm these contact details are current as of 2026. Confirm availability (24/7). These appear in our highest-urgency hard stop.
  - **Priority:** CRITICAL
  - **Verified by:** _____________________________ **Date:** _____________

---

## HIGH Items — Verify Before Submission

Errors here reduce accuracy or completeness but do not produce immediately harmful wrong guidance.

---

- [ ] **HIGH-001 — 30-Day vs. 60-Day Notice Threshold: 1-Year Tenancy**
  - **Claim in our data:** Tenants who have lived in a unit less than 1 year receive a 30-day notice; 1 year or more receive a 60-day notice
  - **Source to check:** California Civil Code Section 1946.1; https://leginfo.legislature.ca.gov
  - **What to look for:** Confirm the 1-year threshold for 60-day notice. Confirm how the 1 year is calculated (from move-in date? From lease start?). Confirm this applies to month-to-month tenancies.
  - **Priority:** HIGH
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **HIGH-002 — 90-Day Notice: Section 8 / HUD Housing**
  - **Claim in our data:** A 90-day notice is required for certain Section 8 / HUD-subsidized housing situations
  - **Source to check:** 24 CFR 247.4 (federal HUD regulations); also check California state law overlay
  - **What to look for:** Confirm which specific housing program types (project-based Section 8, HUD public housing, Housing Choice Voucher) require 90-day notice. Confirm whether the 90-day requirement is federal, state, or both.
  - **Priority:** HIGH
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **HIGH-003 — Discriminatory Eviction: FEHA Protected Classes**
  - **Claim in our data:** Protected classes under FEHA housing provisions include race, color, religion, sex, gender, gender identity, sexual orientation, marital status, national origin, ancestry, familial status, source of income, disability, citizenship, primary language, and immigration status
  - **Source to check:** California Government Code Section 12955; https://calcivilrights.ca.gov
  - **What to look for:** Confirm the complete current protected class list. Source of income and immigration status protections have been subject to legislative changes — confirm current status for both.
  - **Priority:** HIGH
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **HIGH-004 — Los Angeles RSO Coverage Criteria**
  - **Claim in our data:** LA RSO covers rental units built before October 1978 in the City of Los Angeles
  - **Source to check:** https://hcidla.lacity.gov — RSO section; Los Angeles Municipal Code Section 151
  - **What to look for:** Confirm the October 1978 construction date cutoff. Confirm other coverage criteria and exemptions. Confirm whether condo conversions, single-family homes, and other unit types are exempt. This affects the James demo scenario.
  - **Priority:** HIGH
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **HIGH-005 — San Francisco Rent Ordinance Coverage Criteria**
  - **Claim in our data:** SF Rent Ordinance covers most units built before June 13, 1979 (with exceptions)
  - **Source to check:** https://sfrb.org — Rent Ordinance coverage section
  - **What to look for:** Confirm the June 1979 construction date. Confirm exemptions (owner-occupied buildings with fewer than a certain number of units, new construction, etc.). Confirm whether SF tenants have additional rights before an eviction compared to state law.
  - **Priority:** HIGH
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **HIGH-006 — Oakland Just Cause Ordinance: OMC Section 8.22.300**
  - **Claim in our data:** Oakland has a Just Cause for Eviction Ordinance — Oakland Municipal Code Section 8.22.300
  - **Source to check:** https://www.oaklandca.gov/topics/rent-adjustment-program — Oakland Just Cause section; Oakland Municipal Code
  - **What to look for:** Confirm OMC 8.22.300 is the correct citation for Oakland Just Cause. Confirm which units are covered. Confirm what just cause reasons are allowed in Oakland and whether they are more restrictive than AB 1482.
  - **Priority:** HIGH
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **HIGH-007 — Fresno: No Local Rent Ordinance Confirmed**
  - **Claim in our data:** The City of Fresno does NOT have a local rent stabilization ordinance as of last verified data
  - **Source to check:** City of Fresno Municipal Code (fresno.gov); also check whether Fresno enacted any tenant protection ordinance in 2024-2026
  - **What to look for:** Search Fresno Municipal Code for any rent control, rent stabilization ordinance, or just cause eviction ordinance. This is important because Fresno is Priya's city — if Fresno has enacted local protections, it affects the primary demo scenario.
  - **Priority:** HIGH — directly affects primary demo accuracy
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **HIGH-008 — AB 1482 Relocation Assistance Amount**
  - **Claim in our data:** For no-fault just cause terminations under AB 1482, the landlord may be required to pay relocation assistance equal to one month's rent
  - **Source to check:** California Civil Code Section 1946.2; https://leginfo.legislature.ca.gov
  - **What to look for:** Confirm the relocation assistance amount and formula. Confirm when the landlord must pay it. Confirm whether the tenant must request it or it is automatic. This affects the James demo scenario.
  - **Priority:** HIGH
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **HIGH-009 — LAFLA Los Angeles Phone Number**
  - **Claim in our data:** Legal Aid Foundation of Los Angeles intake: (800) 399-4529
  - **Source to check:** https://lafla.org — Contact page
  - **What to look for:** Confirm this phone number is active and reaches LAFLA tenant rights intake as of 2026. Note current hours.
  - **Priority:** HIGH — appears in James demo scenario
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **HIGH-010 — UD Timeline: 20 Days to Hearing After Filing**
  - **Claim in our data:** A court hearing is typically held within approximately 20 days of the UD being filed if the tenant responds
  - **Source to check:** California Code of Civil Procedure Section 1170.5; also check California Courts website for current Fresno and Los Angeles Superior Court UD scheduling timelines
  - **What to look for:** Confirm the statutory UD hearing timeline. Note that actual scheduling depends on court backlog — the statutory minimum and current real-world timelines in high-volume courts like Fresno and LA may differ. Document both.
  - **Priority:** HIGH
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **HIGH-011 — Three-Day Notice to Cure: Cure Period Calculation**
  - **Claim in our data:** A Three-Day Notice to Cure or Quit gives the tenant 3 days to cure the lease violation
  - **Source to check:** California Civil Code Section 1161(3); https://leginfo.legislature.ca.gov
  - **What to look for:** Confirm CC 1161(3) governs the cure-or-quit notice. Confirm the 3-day cure period and whether weekends and holidays are excluded from the cure period calculation the same way they are excluded from the pay-or-quit calculation.
  - **Priority:** HIGH
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **HIGH-012 — California Civil Rights Department Name and URL**
  - **Claim in our data:** The agency formerly known as DFEH is now the California Civil Rights Department at calcivilrights.ca.gov
  - **Source to check:** https://calcivilrights.ca.gov
  - **What to look for:** Confirm this is the current name and URL. Confirm the agency handles FEHA housing discrimination complaints.
  - **Priority:** HIGH
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **HIGH-013 — Writ of Possession Statutory Authority**
  - **Claim in our data:** Writ of Possession execution in residential evictions is governed by California Code of Civil Procedure Section 715.010 et seq.
  - **Source to check:** https://leginfo.legislature.ca.gov — search CCP 715.010
  - **What to look for:** Confirm CCP 715.010 et seq. governs residential writ of possession execution. Confirm the process described in our data (sheriff execution, 5-day notice) matches the statutory text.
  - **Priority:** HIGH
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **HIGH-014 — UD-105 Court Form URL**
  - **Claim in our data:** The Answer to Unlawful Detainer form is UD-105, available at courts.ca.gov/documents/ud105.pdf
  - **Source to check:** https://www.courts.ca.gov/forms.htm — search UD-105
  - **What to look for:** Confirm UD-105 is the current Judicial Council form for a tenant's Answer to an unlawful detainer. Confirm the form is current (check the revision date on the form). Note the direct PDF URL.
  - **Priority:** HIGH — referenced in Derek and Priya action plans
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **HIGH-015 — Sacramento Tenant Protection and Relief Act**
  - **Claim in our data:** Sacramento has enacted a Tenant Protection and Relief Act with additional just-cause eviction protections
  - **Source to check:** City of Sacramento Municipal Code; also check Sacramento city government website (cityofsacramento.org)
  - **What to look for:** Confirm this ordinance exists and is still in effect as of 2026. Confirm which units are covered. This affects the Maria test scenario (Test Scenario 2).
  - **Priority:** HIGH
  - **Verified by:** _____________________________ **Date:** _____________

---

## STANDARD Items — Verify Before Production Launch

These affect completeness, credibility, and user trust. Not critical for the hackathon demo but important before any real-world deployment.

---

- [ ] **STD-001 — San Jose Apartment Rent Ordinance**
  - **Claim in our data:** San Jose has a local Apartment Rent Ordinance
  - **Source to check:** City of San Jose website (sanjoseca.gov); Santa Clara County legal aid
  - **What to look for:** Confirm the ordinance exists and is current as of 2026. Confirm which units are covered. Find the correct agency to contact for unit coverage verification.
  - **Priority:** STANDARD
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **STD-002 — Remaining County Legal Aid Phone Numbers (All 14 Beyond Fresno)**
  - **Counties to verify:** Los Angeles (LAFLA), San Diego, Orange, Riverside, San Bernardino, Sacramento, Alameda (Bay Area Legal Aid and Centro Legal), Santa Clara, Kern, San Joaquin, Stanislaus, Contra Costa, San Francisco (Bay Area Legal Aid and Tenderloin Housing Clinic), Ventura
  - **Source to check:** https://www.lawhelp.org/ca — search each county
  - **What to look for:** For each county, confirm: (a) organization name is current, (b) phone number is active and reaches intake, (c) website URL is active, (d) languages served are current.
  - **Priority:** STANDARD
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **STD-003 — Readability Level Validation**
  - **Claim in our data:** All EvictAware output targets Grade 7 reading level (Flesch-Kincaid 6.0–8.0)
  - **Action to take:** Run sample output from the AI through a Flesch-Kincaid readability calculator (e.g., readable.io or the built-in tool in Microsoft Word). Sample at least 3 full action plan outputs.
  - **What to look for:** Confirm all sample outputs score between 6.0 and 8.0 on Flesch-Kincaid Grade Level. If any output scores above 8.0, identify the sentences causing the score increase and revise the system prompt.
  - **Priority:** STANDARD
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **STD-004 — Housing is Key URL and Current Program Name**
  - **Claim in our data:** housing.ca.gov is the current portal for California rental assistance
  - **Source to check:** https://housing.ca.gov
  - **What to look for:** Confirm the URL resolves. Note the current program name as of 2026. Note whether applications are open. Update ai_config.json system prompt references if the program name or URL has changed.
  - **Priority:** STANDARD
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **STD-005 — LawHelpCA.org URL and Structure**
  - **Claim in our data:** lawhelp.org/ca is the current URL for the California legal aid directory
  - **Source to check:** https://www.lawhelp.org/ca
  - **What to look for:** Confirm the URL is active. Confirm the directory is organized by county and issue type. Confirm it can be used on a mobile phone (Priya will be on her phone).
  - **Priority:** STANDARD
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **STD-006 — Prohibition Against Removing Tenant Property After Lockout: CCP 1174**
  - **Claim in our data:** After a lawful lockout, landlord's obligations regarding abandoned property are governed in part by CCP Section 1174
  - **Source to check:** https://leginfo.legislature.ca.gov — search CCP 1174
  - **What to look for:** Confirm CCP 1174 is the relevant section for post-lockout property handling. Confirm the process the landlord must follow. Note any notice requirements to the tenant about their abandoned property.
  - **Priority:** STANDARD
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **STD-007 — HCIDLA Los Angeles Contact: Phone and URL**
  - **Claim in our data:** HCIDLA (LA Housing Department) phone: (866) 557-7368; URL: hcidla.lacity.gov
  - **Source to check:** https://hcidla.lacity.gov
  - **What to look for:** Confirm the phone number reaches HCIDLA RSO inquiries. Confirm the URL is active. This number appears in the James demo scenario.
  - **Priority:** STANDARD (HIGH if James scenario is used in demo)
  - **Verified by:** _____________________________ **Date:** _____________

---

- [ ] **STD-008 — California Courts Self-Help URL**
  - **Claim in our data:** courts.ca.gov/selfhelp-eviction.htm is the current URL for California Courts eviction self-help
  - **Source to check:** https://www.courts.ca.gov/selfhelp-eviction.htm
  - **What to look for:** Confirm URL is active. Confirm the page contains: UD court forms, instructions for tenants, and the county court locator. This URL appears in multiple action plans.
  - **Priority:** STANDARD
  - **Verified by:** _____________________________ **Date:** _____________

---

## Verification Sign-Off

Before any judge demo or submission, the following team member(s) must sign off:

| Item Category | Team Member | Date Completed | Notes |
|---|---|---|---|
| All CRITICAL items | | | |
| All HIGH items | | | |
| Fresno phone number specifically (for live demo) | | | |
| AB 1482 provisions (for James scenario) | | | |
| DV hotline (for hard stop) | | | |

---

## Our Responsible AI Commitment

This checklist is not just a quality assurance document. It is a demonstration that Team Vision Forge treats the accuracy of legal information as a non-negotiable ethical obligation — not a nice-to-have.

The AI generated the first draft of every data file in this project. The team verified or flagged every legal claim against official primary sources. Where we found uncertainty, we added [VERIFY] markers rather than confident wrong information.

A renter in crisis who receives incorrect legal information from this app may make a wrong decision about their housing. That is not acceptable. This checklist is how we prevent that.

---

*EvictAware Human Verification Checklist v1.0 — Team Vision Forge — June 2026*
*This document should be updated whenever a data file is updated.*
