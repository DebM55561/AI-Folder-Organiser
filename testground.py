import pathlib
from pathlib import Path
import nltk
# nltk.download('stopwords')
import stopwords
from sklearn.cluster import KMeans
import re
from nltk.corpus import stopwords

#
def getFiles(path):
    files = []
    path = Path(path)
    for f in path.iterdir():
        if f.is_file():
            files.append(f.name)

    return files

# print(getFiles("/home/dan/Downloads"))
def preprocText(text):
    text = text.lower()
    text = re.sub(r'\.(pdf|docx|xlsx|csv|txt|zip|pptx|json|png|jpg|ipynb|py|xml|sql|tar|html|ai|h5|yaml|yml)', '', text)
    text = re.sub(r'[._\-\[\]]', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    # text = re.sub(r'\d+', '', text)
    stopword = set(stopwords.words('english'))
    words = text.split()
    filteredWords = []
    for word in words:
        if word not in stopword:
            filteredWords.append(word)
    return " ".join(filteredWords)

#
file_list = [
"annual_report.pdf","customer_data.csv","sales_summary.xlsx","project_plan.docx","meeting_notes.txt",
"invoice_2024.pdf","employee_records.xlsx","marketing_strategy.docx","budget_forecast.xlsx","training_manual.pdf",
"website_backup.zip","product_catalog.pdf","research_results.json","system_config.xml","presentation_slides.pptx",
"inventory_list.csv","contract_agreement.docx","financial_statement.pdf","user_feedback.txt","performance_review.docx",
"event_schedule.xlsx","database_dump.sql","application_log.txt","security_policy.pdf","design_mockup.png",
"architecture_diagram.jpg","press_release.docx","client_proposal.pdf","risk_assessment.docx","audit_report.pdf",
"content_calendar.xlsx","email_template.html","software_update.zip","api_documentation.pdf","brand_guidelines.pdf",
"operations_manual.docx","cashflow_statement.xlsx","tax_documents.pdf","support_tickets.csv","roadmap_overview.pptx",
"quality_checklist.docx","deployment_guide.pdf","analytics_dashboard.xlsx","service_contract.pdf","expense_report.xlsx",
"wireframe_layout.png","business_plan.docx","data_analysis.ipynb","code_snippets.py","server_backup.tar",
"mobile_app_design.fig","social_media_plan.docx","customer_survey.xlsx","lead_tracking.csv","partnership_agreement.pdf",
"workflow_diagram.vsdx","technical_specification.docx","cloud_migration_plan.pdf","incident_report.docx","feature_list.xlsx",
"pricing_model.xlsx","strategy_outline.docx","weekly_report.pdf","monthly_metrics.xlsx","year_end_summary.pdf",
"backup_archive.rar","training_schedule.xlsx","legal_notice.pdf","nda_template.docx","case_study.pdf",
"proposal_draft.docx","product_roadmap.xlsx","bug_report.txt","release_notes.docx","maintenance_log.txt",
"user_manual.pdf","policy_update.docx","market_analysis.pdf","sprint_backlog.xlsx","scrum_notes.txt",
"investment_portfolio.xlsx","shareholder_report.pdf","compliance_checklist.docx","prototype_design.stl","firmware_update.bin",
"source_code_backup.zip","content_strategy.docx","keyword_research.xlsx","ad_campaign_report.pdf","media_kit.pdf",
"customer_invoice.pdf","payment_receipt.pdf","subscription_list.csv","shipping_manifest.xlsx","order_history.csv",
"refund_requests.xlsx","helpdesk_log.txt","crm_export.csv","kpi_dashboard.xlsx","performance_metrics.pdf",
"onboarding_guide.pdf","training_materials.zip","web_analytics.csv","heatmap_results.png","conversion_report.pdf",
"seo_audit.xlsx","system_architecture.pdf","network_config.yaml","docker_compose.yml","requirements_list.txt",
"app_wireframe.sketch","photo_gallery.zip","video_script.docx","podcast_outline.docx","content_brief.docx",
"blog_draft.docx","newsletter_issue.pdf","editorial_calendar.xlsx","brand_assets.zip","logo_concepts.ai",
"customer_profiles.xlsx","persona_document.docx","ux_research.pdf","usability_test_results.xlsx","a_b_test_data.csv",
"changelog.txt","patch_notes.docx","release_schedule.xlsx","backup_schedule.xlsx","system_monitoring.log",
"cloud_costs.xlsx","capacity_plan.docx","disaster_recovery_plan.pdf","penetration_test_report.pdf","security_audit.xlsx",
"encryption_keys.txt","access_control_policy.pdf","compliance_report.pdf","internal_memo.docx","board_minutes.docx",
"quarterly_review.pdf","annual_budget.xlsx","tax_return_2024.pdf","payroll_summary.xlsx","benefits_overview.pdf",
"recruitment_plan.docx","candidate_list.xlsx","interview_notes.txt","offer_letter_template.docx","employee_handbook.pdf",
"shift_schedule.xlsx","timesheet_template.xlsx","procurement_list.csv","vendor_contract.pdf","supply_chain_report.xlsx",
"logistics_plan.docx","warehouse_inventory.xlsx","product_spec_sheet.pdf","manufacturing_plan.docx","quality_report.pdf",
"inspection_checklist.docx","field_service_log.txt","support_documentation.pdf","client_database.accdb","research_paper.docx",
"thesis_draft.docx","lab_results.xlsx","experiment_data.csv","simulation_output.dat","model_training_data.csv",
"ai_model_weights.h5","prediction_results.csv","data_pipeline_config.yaml","etl_process_log.txt","big_data_report.pdf",
"visualization_dashboard.pbix","tableau_report.twbx","powerbi_export.pdf","forecast_model.xlsx","trend_analysis.pdf",
"financial_projection.xlsx","revenue_breakdown.xlsx","expense_analysis.xlsx","profit_margin_report.pdf","cashflow_projection.xlsx",
"investment_summary.pdf","loan_application.docx","credit_score_report.pdf","insurance_policy.pdf","claim_form.docx",
"real_estate_listing.pdf","property_valuation.xlsx","rental_agreement.docx","lease_contract.pdf","tenant_records.xlsx",
"construction_plan.pdf","blueprint_design.dwg","site_inspection_report.pdf","safety_guidelines.pdf","environmental_impact_report.pdf"
]
# # print("filtered words: ", filteredWords)

processed_list = []

# for i in range(len(file_list)-150):
#     processed_list.append(preprocText(file_list[i]))
# #
# print(processed_list)
#
# # files = getFiles("/home/dan/Downloads")
# # # print(files)
# # processedList=files
# # for i in range(len(processedList)):
# #     x = preprocText(processedList[i])
# #     processedList[i] = x[0]
# #
# from sentence_transformers import SentenceTransformer
#
#
# from sklearn.decomposition import PCA
#
#
# model = SentenceTransformer('all-MiniLM-L6-v2')
# doc = processed_list
#
# embeddings = model.encode(doc, show_progress_bar=True)
#
# pca = PCA(n_components=50)
# x_reduced = pca.fit_transform(embeddings)
#
# kmeans = KMeans(n_clusters=10, n_init='auto')
# clusters = kmeans.fit_predict(x_reduced)
# #
# # print(clusters)
# #
# for i in range(len(processed_list)):
#     print(f"{processed_list[i]}: {clusters[i]}")
from PreProc import PreProc

# def get_top_terms_per_cluster(vectorizer, kmeans, n_terms=5):
#     # Get the coordinates of the cluster centers
#     order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
#     terms = vectorizer.get_feature_names_out()
#
#     for i in range(kmeans.n_clusters):
#         top_words = [terms[ind] for ind in order_centroids[i, :n_terms]]
#         print(f"Cluster {i} Keywords: {', '.join(top_words)}")



# get_top_terms_per_cluster(vectorizer, kmeans)
# print(vectorizer.get_feature_names_out())
# print(x.shape)


# print(processedList)


# print(processedList)
# newfile=[]
# for i in len(files):
#     proc = preprocText(files)
#
# print(newfile)

preproc = PreProc("/home/dan/Downloads")
if preproc is not None:
    print("not null")
#
files = preproc.preprocessing()
print(files)
for f in files:
    if f is not None:
        print(f)




